from django.urls import path
from django.contrib.auth import views as auth_views
from video_app.views import index, process_media, contact_us, about_us, privacy_policy

urlpatterns = [
    path('', index, name='home'),
    path('process-media/', process_media, name='process_media'),
    path('contact-us/', contact_us, name='contact_us'),
    path('about-us/', about_us, name='about_us'),
    path('privacy-policy/', privacy_policy, name='privacy_policy'),
]
