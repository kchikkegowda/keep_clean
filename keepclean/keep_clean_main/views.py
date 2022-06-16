from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

#index page
def index(request):
    template = loader.get_template('index.html')
    context = {
        'latest_question_list': 'test',
    }
    return HttpResponse(template.render(context, request))

#about page
def about(request):
    template = loader.get_template('about.html')
    context = {
        'latest_question_list': 'test',
    }
    return HttpResponse(template.render(context, request))

def service(request):
    template = loader.get_template('service.html')
    context = {
        'latest_question_list': 'test',
    }
    return HttpResponse(template.render(context, request))

def portfolio(request):
    template = loader.get_template('portfolio.html')
    context = {
        'latest_question_list': 'test',
    }
    return HttpResponse(template.render(context, request))

def contact(request):
    template = loader.get_template('contact.html')
    context = {
        'latest_question_list': 'test',
    }
    return HttpResponse(template.render(context, request))