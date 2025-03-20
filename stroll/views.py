from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from stroll.forms import UserForm


from stroll.forms import CreateWalkForm

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
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            if 'picture' in request.FILES:
                user.picture = request.FILES['picture']

            user.save()

            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    
    return render(request, 'stroll/signup.html', context = {'user_form': user_form,
                                                             'registered': registered})

@login_required
def create_walk(request):
    form = CreateWalkForm()

    if request.method == 'POST':
        form = CreateWalkForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return redirect('/stroll/')
        else:
            print(form.errors)
    
    return render(request, 'stroll/create_walk.html', {'form':form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        #not used currently
        stay_logged_in = request.POST.get('stay_logged_in')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('stroll:home'))
            else:
                return HttpResponse("Your Stroll account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'stroll/login.html')

@login_required
def user_logout(request):
    logout(request)

    return redirect(reverse('stroll:home'))

def my_profile(request):
    context_dict = {}
    context_dict['profile_picture'] = "photo"
    context_dict['total_likes'] = 50
    context_dict['total_views'] = 100
    context_dict['recent_walks'] = [{"thumbnail": "walk_hill", "name": "my first walk", "area": "partickwwwwwwwwwwwwwwww", "tags": "hi,hello,good".split(","), 
                                      "difficulty": 1, "description": "Thuis is my really cool walkssssssssssssssss ssssssssssssssssssssssss ssssssssssssssssssssssssssssssssssss sssssssssssssssssssssssssssss sssssssssssssssssssssssssssss sssssssssssssssssssssssssssssssssssssssssssssssssssssssssss", "slug": "a"},
                                      {"thumbnail": "walk_hill", "name": "my last walk", "area": "govan", "tags": "goodbye,fairwell,bad".split(","), 
                                      "difficulty": 4, "description": "Thuis is my really bad walk", "slug": "a"},
                                      ]
    return render(request, 'stroll/my_profile.html', context=context_dict)

def edit_profile(request):
    return render(request, 'stroll/edit_profile.html')

def my_walks(request):
    context_dict = {}
    context_dict["search_results"] = [{"thumbnail": "walk_hill", "name": "my first walk", "area": "partickwwwwwwwwwwwwwwww", "tags": "hi,hello,good".split(","), 
                                      "difficulty": 1, "description": "Thuis is my really cool walkssssssssssssssss ssssssssssssssssssssssss ssssssssssssssssssssssssssssssssssss sssssssssssssssssssssssssssss sssssssssssssssssssssssssssss sssssssssssssssssssssssssssssssssssssssssssssssssssssssssss", "slug": "a"},
                                      {"thumbnail": "walk_hill", "name": "my last walk", "area": "govan", "tags": "goodbye,fairwell,bad".split(","), 
                                      "difficulty": 4, "description": "Thuis is my really bad walk", "slug": "a"},
                                      {"thumbnail": "walk_hill", "name": "my new walk", "area": "leith", "tags": "i,regret,this".split(","), 
                                      "difficulty": 10, "description": "Thuis is not fun", "slug": "a"},
                                      ]
    return render(request, 'stroll/my_walks.html', context=context_dict)

def my_questions(request):
    context_dict = {}
    context_dict['questions'] = [{"user": "John", "date_published":12-21-2520, "title": "how do i walk", "likes": 35, "text": "how do i walk with my legs", "views": 100, "slug": "a"},
                                 {"user": "John", "date_published":12-21-2520, "title": "yooo haso has has f asjfasks   jasfjk  ajsfkja   ajsdfassa aaaas ", "likes": 35, "text": "how do i walk with my legs", "views":500, "slug": "a"}]

    return render(request, 'stroll/my_questions.html', context=context_dict)

def search_walks(request):
    context_dict = {}
    context_dict["search_results"] = [{"thumbnail": "walk_hill", "name": "my first walk", "area": "partickwwwwwwwwwwwwwwww", "tags": "hi,hello,good".split(","), 
                                      "difficulty": 1, "description": "Thuis is my really cool walkssssssssssssssss ssssssssssssssssssssssss ssssssssssssssssssssssssssssssssssss sssssssssssssssssssssssssssss sssssssssssssssssssssssssssss sssssssssssssssssssssssssssssssssssssssssssssssssssssssssss", "slug": "a"},
                                      {"thumbnail": "walk_hill", "name": "my last walk", "area": "govan", "tags": "goodbye,fairwell,bad".split(","), 
                                      "difficulty": 4, "description": "Thuis is my really bad walk", "slug": "a"},
                                      {"thumbnail": "walk_hill", "name": "my new walk", "area": "leith", "tags": "i,regret,this".split(","), 
                                      "difficulty": 10, "description": "Thuis is not fun", "slug": "a"},
                                      ]
    return render(request, 'stroll/search_walks.html', context=context_dict)

def show_walk(request, walk_name_slug):
    
    context_dict = {"user": "emi", "thumbnail": "walk_hill", "photo1": "photo", "name": "my first walk", "length": "100km", "area": "partickwwwwwwwwwwwwwwww", "tags": "hi,hello,good".split(","), 
                                      "difficulty": 1, "description": "Thuis is my really cool walkssssssssssssssss ssssssssssssssssssssssss ssssssssssssssssssssssssssssssssssss sssssssssssssssssssssssssssss sssssssssssssssssssssssssssss sssssssssssssssssssssssssssssssssssssssssssssssssssssssssss", "slug": "a"}
    context_dict['comments'] = [{"text": "Good job", "date_published": "13/20/24", "user": "jules", "profile_picture": "photo"}]
    return render(request, 'stroll/walk.html', context=context_dict)

def questions(request):
    context_dict = {}
    context_dict['questions'] = [{"user": "John", "date_published":"12-21-2520", "title": "how do i walk", "likes": 35, "text": "how do i walk with my legs", "views": 100, "slug": "a"},
                                 {"user": "John", "date_published":"12-21-2520", "title": "yooo haso has has f asjfasks   jasfjk  ajsfkja   ajsdfassa aaaas ", "likes": 35, "text": "how do i walk with my legs", "views":500, "slug": "a"}]
    return render(request, 'stroll/questions.html', context=context_dict)

def show_question(request, question_slug):
    context_dict = {'text': 'blah blah blah lbahb bhal', "user": "emi", "date_published":"12-325-23"}
    return render(request, 'stroll/question.html', context=context_dict)