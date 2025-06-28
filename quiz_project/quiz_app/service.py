import requests
import sqlite3
import json
import time
from . import config

API_KEY = config.API_KEY
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

def initialize_database():
    conn = sqlite3.connect('questions.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY, 
            key TEXT UNIQUE, 
            value TEXT
        )
    ''')
    conn.commit()
    conn.close()

def key_exists(cursor, key):
    cursor.execute("SELECT COUNT(*) FROM questions WHERE key = ?", (key,))
    return cursor.fetchone()[0] > 0

def generate_question(text):
    initialize_database()
    conn = sqlite3.connect('questions.db')
    cursor = conn.cursor()

    prompt = (
        f"Create a practice text with multiple choice questions on the following text:\n"
        f"{text}\n\n"
        f"Each question should be on a different line. Each question should have 4 possible answers.\n"
        f"After each set of options, write the correct answer as 'Answer: X'"
    )

    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    max_retries = 3
    for attempt in range(max_retries):
        response = requests.post(GEMINI_URL, headers=headers, data=json.dumps(payload))

        if response.status_code == 200:
            try:
                data = response.json()
                questions = data["candidates"][0]["content"]["parts"][0]["text"]
                break
            except (KeyError, IndexError):
                raise Exception("Unexpected Gemini response format")
        elif response.status_code == 503:
            print(f"Gemini is overloaded (Attempt {attempt+1}). Retrying...")
            time.sleep(2 ** attempt)
        else:
            raise Exception(f"Gemini API error: {response.status_code} - {response.text}")
    else:
        raise Exception("Gemini API failed after multiple retries.")

    # Generate a unique key
    base_key = ''.join(text.strip().split()[:2])
    key = base_key
    index = 1
    while key_exists(cursor, key):
        key = f"{base_key}{index}"
        index += 1

    # Save the result
    cursor.execute("INSERT INTO questions (key, value) VALUES (?, ?)", (key, questions))
    conn.commit()
    conn.close()

    return questions

def print_all_questions():
    initialize_database()
    conn = sqlite3.connect('questions.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM questions")
    rows = cursor.fetchall()
    conn.close()
    return rows
