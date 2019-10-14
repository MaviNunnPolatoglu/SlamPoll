from django.urls import path, include
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    path('create', Create.as_view(), name='create'),
    path('', home, name='home'),
    path('<slug:poll_name>/overview', Overview.as_view()),
    path('about_us', bio, name='aboutus'),
    path('question/<int:question_nr>', question, name='question')
]