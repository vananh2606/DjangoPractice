from django.shortcuts import render
from . import machine_learning_model

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def form(request):
    return render(request, 'form.html')

def result(request):
    user_input = request.GET["user_input"]
    user_input = machine_learning_model.mulitplier(user_input)
    return render(request, 'result.html', {'form_input':user_input})