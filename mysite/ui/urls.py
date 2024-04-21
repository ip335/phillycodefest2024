from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('get_question_audio_url/', get_question_audio_url, name='question_audio_url'),
    path('get_answer_url/', get_answer_url, name='answer_url'),
    path('test/', test, name='test')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
