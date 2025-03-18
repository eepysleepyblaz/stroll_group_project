from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

def home(request):
    # Variables needed for home template:
    # Array of popular walks
    # Current code just for test
    context_dict = {}
    context_dict["popular_walks"] = [{"thumbnail": "walk_hill", "name": "my first walk", "area": "partickwwwwwwwwwwwwwwww", "tags": "hi,hello,good".split(","), 
                                      "difficulty": 1, "description": "Thuis is my really cool walkssssssssssssssss ssssssssssssssssssssssss ssssssssssssssssssssssssssssssssssss sssssssssssssssssssssssssssss sssssssssssssssssssssssssssss sssssssssssssssssssssssssssssssssssssssssssssssssssssssssss", "slug": "a"},
                                      {"thumbnail": "walk_hill", "name": "my last walk", "area": "govan", "tags": "goodbye,fairwell,bad".split(","), 
                                      "difficulty": 4, "description": "Thuis is my really bad walk", "slug": "a"},
                                      {"thumbnail": "walk_hill", "name": "my new walk", "area": "leith", "tags": "i,regret,this".split(","), 
                                      "difficulty": 10, "description": "Thuis is not fun", "slug": "a"},
                                      ]
    return render(request, 'stroll/home.html', context=context_dict)

def about(request):
    context_dict = {}
    #Always give three popular walks just make them None type if not not enough
    context_dict["popular_walks"] = [{"thumbnail": "photo", "name": "my last walk", "area": "govan", "tags": "goodbye,fairwell,bad".split(","), 
                                      "difficulty": 4, "description": "Thuis is my really bad walk", "slug": "a"}]
    return render(request, 'stroll/about.html', context=context_dict)

def signup(request):
    return render(request, 'stroll/signup.html')

def create_walk(request):
    return render(request, 'stroll/create_walk.html')

def login(request):
    return render(request, 'stroll/login.html')

def logout(request):
    return render(request, 'stroll/logout.html')

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
    context_dict = {}
    context_dict['questions'] = [{"user": "John", "date_published":12-21-2520, "title": "how do i walk", "likes": 35, "text": "how do i walk with my legs", "views": 100, "slug": "a"},
                                 {"user": "John", "date_published":12-21-2520, "title": "yooo haso has has f asjfasks   jasfjk  ajsfkja   ajsdfassa aaaas ", "likes": 35, "text": "how do i walk with my legs", "views":500, "slug": "a"}]
    return render(request, 'stroll/questions.html', context=context_dict)

def show_question(request):
    return render(request, 'stroll/show_question.html')