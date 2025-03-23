from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from stroll.forms import *
from stroll.models import *

from stroll.forms import CreateWalkForm

def home(request):
    # Variables needed for home template:
    # Array of popular walks
    # Current code just for test
    context_dict = {}
    context_dict["popular_walks"] = Walk.objects.order_by('-likes')[:3]

    return render(request, 'stroll/home.html', context=context_dict)

def about(request):
    context_dict = {}
    #Always give three popular walks just make them None type if not not enough
    context_dict["popular_walks"] = Walk.objects.order_by('-likes')[:3]
    return render(request, 'stroll/about.html', context=context_dict)

def signup(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_picture' in request.FILES:
                profile.profile_picture = request.FILES['profile_picture']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    
    return render(request, 'stroll/signup.html', context = {'user_form': user_form,
                                                            'profile_form':profile_form,
                                                             'registered': registered,})

@login_required
def create_walk(request):
    form = CreateWalkForm()
    if request.method == 'POST':
        form = CreateWalkForm(request.POST, request.FILES)
        print(request.POST.get('map_coordinates'))
        print(request.POST.get('length'))
        
        if form.is_valid():
            new_walk = form.save(commit=False)
            new_walk.user = request.user

            if 'thumbnail' in request.FILES:
                new_walk.thumbnail = request.FILES['thumbnail']

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

    if user.is_superuser:
        context_dict = {}
        context_dict['username'] = user.username + ' (superuser)'

    if user.is_superuser == False:

        try:
            current_user_profile = UserProfile.objects.get(user=user)
        except UserProfile.DoesNotExist:
            current_user_profile = None

        walks = Walk.objects.filter(user=current_user_profile.user).order_by('-date_published')

        if current_user_profile == None:
            context_dict = {}
            context_dict['username'] = 'None type user'
        
        else:
            context_dict = {}

            if current_user_profile.is_moderator:
                context_dict['username'] = current_user_profile.user.username + ' (moderator)'
            else:
                context_dict['username'] = current_user_profile.user.username

            context_dict['email'] = current_user_profile.user.email
            context_dict['date_of_birth'] = current_user_profile.date_of_birth
            context_dict['profile_picture'] = current_user_profile.profile_picture 
            context_dict['total_likes'] = current_user_profile.total_likes 
            context_dict['total_views'] = current_user_profile.total_views 

            if len(walks) != 0:
                context_dict['walks'] = walks
            else:
                context_dict['walks'] = None
            
    return render(request, 'stroll/my_profile.html', context=context_dict)

def edit_profile(request):
    return render(request, 'stroll/edit_profile.html')

def my_walks(request):
    context_dict = {}
    context_dict["walks"] = Walk.objects.filter(user=request.user)
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

def show_walk(request, id):
    walk = Walk.objects.get(id=id)
    comments = WalkComment.objects.filter(walk_id=id)

    context_dict = {'walk':walk}
    context_dict['photos'] = [x for x in [walk.gallery_image_1, walk.gallery_image_2, walk.gallery_image_3, walk.gallery_image_4] if x != ""]
    context_dict['map_coordinates'] = walk.map_coordinates
    context_dict['comments'] = comments
   
    return render(request, 'stroll/show_walk.html', context=context_dict)

def questions(request):
    form = QuestionForm()
    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES)
        
        if form.is_valid():
            new_question = form.save(commit=False)
            new_question.question = request.POST.get('question')
            new_question.user = UserProfile.objects.get(user_id=request.user.id)

            new_question.save()

        else:
            print(form.errors)
            
    context_dict = {}
    questions = Question.objects.all()
    context_dict['questions'] = questions
    context_dict['form'] = form
    return render(request, 'stroll/questions.html', context=context_dict)

def show_question(request, id):
    form = QuestionCommentForm()
    if request.method == 'POST':
        form = QuestionCommentForm(request.POST, request.FILES)
        
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.comment = request.POST.get('comment')
            new_comment.user = UserProfile.objects.get(user_id=request.user.id)
            new_comment.question = Question.objects.get(id=id)

            new_comment.save()

        else:
            print(form.errors)

    context_dict = {}
    context_dict['question'] = Question.objects.get(id=id)
    print(context_dict['question'].id)
    context_dict['comments'] = QuestionComment.objects.filter(question_id=id)

    return render(request, 'stroll/show_question.html', context=context_dict)
