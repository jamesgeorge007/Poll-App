from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def index(request):

    return HttpResponse('<h1>This is the polls index!</h1>')

def details(request, question_id):

    return HttpResponse('You\'re looking at question %s.' %question_id)

def results(request, question_id):

    return HttpResponse('You\'re looking at the results of question %s' %question_id)

def vote(request, question_id):

    return HttpResponse('You\'re voting on question %s.' %question_id)
