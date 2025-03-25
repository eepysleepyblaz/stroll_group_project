from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views import View
from django.utils.decorators import method_decorator

from stroll.forms import *
from stroll.models import *

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

    def toInt(string):
        if string != "":
            return int(string)
        else:
            return string

    context_dict = {}

    form = SearchWalkForm()
    if request.method == 'POST':
        title = area = description = tags = min_length = max_length = min_difficulty = max_difficulty = search = ""
        level = request.POST['form-level']

        if level == 'simple':
            search = request.POST['search']
            
            context_dict["search_results"] = (Walk.objects.filter(title__icontains=search) |
                                              Walk.objects.filter(area__icontains=search) |
                                              Walk.objects.filter(description__icontains=search) |
                                              Walk.objects.filter(tags__icontains=search))


        elif level == 'advanced':
            title = request.POST['title']
            area = request.POST['area']
            description = request.POST['description']
            tags = request.POST['tags']

            min_length = toInt(request.POST['min_length'])
            max_length = toInt(request.POST['max_length'])
            min_difficulty = toInt(request.POST['min_difficulty'])
            max_difficulty = toInt(request.POST['max_difficulty'])

            kwargdict = {'title__icontains': title,
                    'area__icontains': area,
                    'description__icontains': description,
                    'tags__icontains': tags,}
            if min_length:
                kwargdict['length__gte'] = min_length/1000
            if max_length:
                kwargdict['length__lte'] = max_length/1000
            
            if min_difficulty:
                kwargdict['difficulty__gte'] = min_difficulty

            if max_difficulty:
                kwargdict['difficulty__lte'] = max_difficulty

            context_dict["search_results"] = Walk.objects.filter(**kwargdict)
            

    context_dict['form'] = form
    return render(request, 'stroll/search_walks.html', context=context_dict)

def show_walk(request, id):
    form = WalkCommentForm()
    if request.method == 'POST':
        form = WalkCommentForm(request.POST)
        
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.comment = request.POST.get('comment')
            new_comment.user = UserProfile.objects.get(user_id=request.user.id)
            new_comment.walk = Walk.objects.get(id=id)

            new_comment.save()

        else:
            print(form.errors)

    walk = Walk.objects.get(id=id)
    comments = WalkComment.objects.filter(walk_id=id)[::-1]

    context_dict = {'walk':walk}
    context_dict['photos'] = [x for x in [walk.gallery_image_1, walk.gallery_image_2, walk.gallery_image_3, walk.gallery_image_4] if x != ""]
    context_dict['map_coordinates'] = walk.map_coordinates
    context_dict['comments'] = comments
    context_dict['form'] = form
   
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
    questions = Question.objects.all()[::-1]
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
    context_dict['comments'] = QuestionComment.objects.filter(question_id=id)[::-1]

    return render(request, 'stroll/show_question.html', context=context_dict)

class LikeWalkView(View):
    @method_decorator(login_required)
    def get(self, request):
    
        walk_id = request.GET['walk_id']
        try:
            walk = Walk.objects.get(id=int(walk_id))

        except Walk.DoesNotExist:
            return HttpResponse(-1)
        except ValueError:
            return HttpResponse(-1)
        
        walkUser = UserProfile.objects.get(user=walk.user)
        
        walk.likes = walk.likes + 1
        walkUser.total_likes += 1
        walk.save()
        walkUser.save()

        return HttpResponse(walk.likes)

class LikeQuestionView(View):
    @method_decorator(login_required)
    def get(self, request):
    
        question_id = request.GET['question_id']
        try:
            question = Question.objects.get(id=int(question_id))

        except Question.DoesNotExist:
            return HttpResponse(-1)
        except ValueError:
            return HttpResponse(-1)
        
        questionUser = question.user

        question.likes = question.likes + 1
        questionUser.total_likes += 1
        question.save()
        questionUser.save()

        return HttpResponse(question.likes)