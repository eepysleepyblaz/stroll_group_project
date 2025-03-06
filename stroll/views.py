from django.shortcuts import render, redirect
from django.http import HttpResponse

def home(request):
    context_dict = {}
    context_dict["popular_walks"] = ["Walk 1", "Walk 2", "Walk 3", "Walk 4", "Walk 5"]
    return render(request, 'stroll/home.html', context=context_dict)

def about(request):
    return render(request, 'stroll/about.html')

def signup(request):
    return render(request, 'stroll/signup.html')

def create_walk(request):
    return render(request, 'stroll/create_walk.html')

def login(request):
    return render(request, 'stroll/login.html')

def my_profile(request):
    return render(request, 'stroll/my_profile.html')

def edit_profile(request):
    return render(request, 'stroll/edit_profile.html')

def my_walks(request):
    return render(request, 'stroll/my_walks.html')

def my_questions(request):
    return render(request, 'stroll/edit_profile.html')

def search_walks(request):
    return render(request, 'stroll/search_walks.html')

def show_walk(request):
    return render(request, 'stroll/walk.html')

def questions(request):
    return render(request, 'stroll/questions.html')

def show_question(request):
    return render(request, 'stroll/show_question.html')