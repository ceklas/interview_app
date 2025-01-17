# interview_app/urls.py
from django.urls import path, include

urlpatterns = [
    path('', include('app.urls')),  # 'app/' yerine direkt root path'e bağlıyoruz
]