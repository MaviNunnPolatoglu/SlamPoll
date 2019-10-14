from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from .forms import CreateForm
from .models import Poll
from .decorators import poll_must_exist
from django.utils.decorators import method_decorator
import random


class Create(View):
    def get(self, request):
        ctx = {}
        ctx['form'] = CreateForm()
        return render(request, 'slampoll/create.html', ctx)

    def post(self, request):
        ctx = {}
        form = CreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        ctx['form'] = form
        return render(request, 'slampoll/create.html', ctx)


@method_decorator([poll_must_exist], name='dispatch')
class Overview(View):
    def get(self, request, poll_name):
        ctx = {}
        ctx['poll_name'] = poll_name
        return render(request, 'slampoll/overview.html', ctx)


def home(request):
    ctx = {
        'last_question': random.randint(10, 1000),
        'names': ['mavi', 'marc', 'reto'],
        'nr_polls': Poll.objects.all().count()
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