from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about_us', bio, name='aboutus'),
    path('question/<int:question_nr>', question, name='question')
]