from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('quiz_app.urls')),
    path('history/', include('quiz_app.urls'))
]
