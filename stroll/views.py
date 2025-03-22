from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from stroll.forms import UserForm, UserProfileForm
from stroll.models import *

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
    invalid = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True
        else:
            invalid = True
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    
    return render(request, 'stroll/signup.html', context = {'user_form': user_form,
                                                            'profile_form':profile_form,
                                                             'registered': registered,
                                                             'invalid':invalid})

@login_required
def create_walk(request):
    form = CreateWalkForm()

    if request.method == 'POST':
        form = CreateWalkForm(request.POST)
        print(request.POST.get('map_coordinates'))
        print(request.POST.get('length'))
        

        if form.is_valid():
            new_walk = form.save(commit=False)
            new_walk.user = request.user
            new_walk.save()

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

@login_required
def my_profile(request):
    user = request.user
    try:
        current_user_profile = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        current_user_profile = None

    walks = Walk.objects.filter(user=current_user_profile).order_by('-date_published')

    context_dict = {}
    context_dict['profile_picture'] = current_user_profile.profile_picture if current_user_profile  else "ERROR: NO USERNAME VALUE GIVEN"
    context_dict['total_likes'] = current_user_profile.total_likes if current_user_profile  else "ERROR: NO LIKES VALUE GIVEN"
    context_dict['total_views'] = current_user_profile.total_views if current_user_profile  else "ERROR: NO VIEWS VALUE GIVEN"
    context_dict['recent_walks'] = walks
        
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
    return render(request, 'stroll/my_questions.html')

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

def show_walk(request, walk_id):
    walk = Walk.objects.get(id=walk_id)

    context_dict = {'walk':walk}
    context_dict['tags'] = walk.tags.split(",")
    
    #context_dict = {"user": "emi", "thumbnail": "walk_hill", "photo1": "photo", "name": "my first walk", "length": "100km", "area": "partickwwwwwwwwwwwwwwww", "tags": "hi,hello,good".split(","), 
                                      #"difficulty": 1, "description": "Thuis is my really cool walkssssssssssssssss ssssssssssssssssssssssss ssssssssssssssssssssssssssssssssssss sssssssssssssssssssssssssssss sssssssssssssssssssssssssssss sssssssssssssssssssssssssssssssssssssssssssssssssssssssssss", "slug": "a"}
    context_dict['comments'] = [{"text": "Good job", "date_published": "13/20/24", "user": "jules", "profile_picture": "photo"}, {"text": "Good job2", "date_published": "13/20/242", "user": "jules2", "profile_picture": "photo"}]
    return render(request, 'stroll/walk.html', context=context_dict)

def questions(request):
    context_dict = {}
    context_dict['questions'] = [{"user": "John", "date_published":"12-21-2520", "title": "how do i walk", "likes": 50, "text": "how do i walk with my legs", "views": 100, "slug": "a"},
                                 {"user": "John", "date_published":"12-21-2520", "title": "yooo haso has has f asjfasks   jasfjk  ajsfkja   ajsdfassa aaaas ", "likes": 35, "text": "how do i walk with my legs", "views":500, "slug": "a"},
                                 {"user": "John", "date_published":"12-21-2520", "title": "yooo haso has has f asjfasks   jasfjk  ajsfkja   ajsdfassa aaaas ", "likes": 100, "text": "how do i walk with my legs", "views":500, "slug": "a"}]

    return render(request, 'stroll/questions.html', context=context_dict)

def show_question(request, question_slug):
    return render(request, 'stroll/show_question.html')
