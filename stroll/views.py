from django.shortcuts import render, redirect
from django.http import HttpResponse

def home(request):
    # Variables needed for home template:
    # Array of popular walks
    # Current code just for test
    context_dict = {}
    context_dict["popular_walks"] = [{"thumbnail": "a photo", "name": "my first walk", "area": "partick", "tags": "hi,hello,good".split(","), 
                                      "difficulty": 1, "description": "Thuis is my really cool walk"},
                                      {"thumbnail": "another photo", "name": "my last walk", "area": "govan", "tags": "goodbye,fairwell,bad".split(","), 
                                      "difficulty": 4, "description": "Thuis is my really bad walk"},
                                      {"thumbnail": "a picture", "name": "my new walk", "area": "leith", "tags": "i,regret,this".split(","), 
                                      "difficulty": 10, "description": "Thuis is not fun"}]
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