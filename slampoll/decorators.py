from .models import Poll
from django.contrib import messages
from django.shortcuts import render


def poll_must_exist(function=None):
    def decorator(func):
        def inner(request, *args, **kwargs):
            poll_name = str(kwargs.get('poll_name', None)).lower()
            if Poll.objects.filter(name=poll_name).exists():
                return function(request, *args, **kwargs)
            messages.info(request, f'There exists no poll with name {poll_name}. Maybe a typo?')
            return render(request, 'slampoll/error.html', {})
        return inner
    if function:
        return decorator(function)
    return decorator