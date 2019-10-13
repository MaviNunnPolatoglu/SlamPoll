from django.shortcuts import render, HttpResponse
import random

# Create your views here.
def home(request):
    ctx = {
        'last_question': random.randint(10, 1000),
        'names': ['mavi', 'marc', 'reto']
    }
    return render(request, 'slampoll/home.html', ctx)

def bio(request):
    ctx = {}
    return render(request, 'slampoll/aboutus.html', ctx)

def question(request, question_nr):
    ctx = {
        'q_nr': question_nr
    }
    return render(request, 'slampoll/question.html', ctx)