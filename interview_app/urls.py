# interview_app/urls.py
from django.urls import path, include

urlpatterns = [
    path('app/', include('app.urls')),  # 'app' uygulamasının URL'lerini dahil ettik
]