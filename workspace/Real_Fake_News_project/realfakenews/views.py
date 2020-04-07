from django.shortcuts import render
from django.http import HttpResponse
from .models import Story
from django.shortcuts import render
from django.http import Http404


def index(request):
    latest_story_list = Story.objects.order_by('-pub_date')
    context = {'latest_story_list': latest_story_list}
    return render(request, 'realfakenews/index.html', context)


def detail(request, story_id):
    try:
        story = Story.objects.get(pk=story_id)
    except Story.DoesNotExist:
        raise Http404("Story does not exist")
    return render(request, 'realfakenews/detail.html', {'story': story})

