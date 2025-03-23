import os
from datetime import datetime
from django.core.files import File
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'stroll_group_project.settings')


import django
django.setup()
from stroll.models import *

def populate():
    
    walks = [
        {'thumbnail':'population_thumbnails/govan.jpg',
        'title':'Govan walk',
        'description':'Walking around govan, took photos of the river',
        'area':'Govan',
        'tags':'govan,river',
        'difficulty':3,
        'slug':'a'},

        {'thumbnail':'population_thumbnails/milngavie.jpg',
        'title':'Milngavie walk',
        'description':'The neighbourhood seems nice',
        'area':'Milngavie',
        'tags':'milngavie,nice',
        'difficulty':2,
        'slug':'a'},

        {'thumbnail':'population_thumbnails/town.jpg',
        'title':'City centre walk',
        'description':'There are many places to eat',
        'area':'Town',
        'tags':'city centre,town,shops',
        'difficulty':4,
        'slug':'a'},
    ]

    questions = [
        {'title':'What are some good walks around Govan?',
        'text':'Heard about this neighbourhood, is there anything to do around there?'},

        {'title':'Can anyone recommend some shoes for long walks?',
        'text':"current shoes aren't fit for the task"},

        {'title':'Where can I go for more nature walks?',
        'text':'Ideally a place with many fields and trees please'},
    ]

    walk_comments = [
        {'text':'nice walk'},

        {'text':'There is another way you can take, has some interesting shops.'},

        {'text':"try going to glasgow green, it's not too far"},
    ]

    question_comments = [
        {'text':'Try going along the river'},

        {'text':'any quality hiking shoes/boots will be enough'},

        {'text':'here: *link to walk in nature*'},
    ]

    # ellie1:
    #   walk: city centre; question: hiking boots
    #   walk comment: nice walk -> Govan; question comment: link -> nature
    #
    # kevin2:
    #   walk: Milngavie; question: nature walk
    #   walk comment: glasgow green -> city centre; question comment: river -> Govan
    #
    # scott3:
    #   walk: Govan; question: Govan
    #   walk comment: shops -> Milngavie; question comment: hiking boots -> hiking boots

    users = [

        {'username':'ellie1',
        'description':'casual walker',
        'email':'ellie@gmail.com',
        'date_of_birth':'2005-08-14',
        'profile_picture':'population_profile_pictures/ellie1.jpg',
        'total_likes':12_300,
        'total_views':20_891,
        'is_moderator':False,
        'walks':[walks[2]],
        'questions':[questions[1]],
        'comments':[walk_comments[0], question_comments[2]],
        'commented_on':[walks[0], questions[2]]},

        {'username':'kevin2',
        'description':'intermediate walker',
        'date_of_birth':'1979-10-12',
        'email':'kevin@gmail.com',
        'profile_picture':'population_profile_pictures/kevin2.jpg',
        'total_likes':12,
        'total_views':125,
        'is_moderator':False,        
        'walks':[walks[1]],
        'questions':[questions[2]],
        'comments':[walk_comments[2], question_comments[0]],
        'commented_on':[walks[2], questions[0]]},

        {'username':'scott3',
        'description':'pro walker',
        'date_of_birth':'1965-01-05',
        'email':'scott@gmail.com',
        'profile_picture':'population_profile_pictures/scott3.jpg',
        'total_likes':25,
        'total_views':344,
        'is_moderator':True,
        'walks':[walks[0]],
        'questions':[questions[0]],
        'comments':[walk_comments[1], question_comments[1]],
        'commented_on':[walks[1], questions[1]]}
    ]
        

    for user in users:
        u = add_user(user['username'], user['description'], user['is_moderator'],
                     user['date_of_birth'], user['profile_picture'], user['total_likes'],
                     user['total_views'], user['email'])
        u[0].refresh_from_db()
        u[1].refresh_from_db()
        
        for walk in user['walks']:
            w = add_walk(u[0], walk['title'], walk['description'], walk['area'],
                         walk['tags'], walk['difficulty'], walk['thumbnail'])
            w.refresh_from_db()
        
        for question in user['questions']:
            q = add_question(u[1], question['title'], question['text'])
            q.refresh_from_db()

        for w in Walk.objects.all():
            if w.title == user['commented_on'][0]['title']:
                wq = add_walk_comment(u[1], w, user['comments'][0]['text'])
                wq.refresh_from_db()

        for q in Question.objects.all():
            if q.title == user['commented_on'][1]['title']:
                qc = add_question_comment(u[1], q, user['comments'][1]['text'])
                qc.refresh_from_db()

    for up in UserProfile.objects.all():
        for w in Walk.objects.filter(user=up.user):
            for wc in WalkComment.objects.filter(walk=w):
                print(f'- {up}: Walk, {w}: {wc} comment made by {wc.user}')

        for q in Question.objects.filter(user=up):
            for qc in QuestionComment.objects.filter(question=q):
                print(f'- {up}: Question, {q}: {qc} comment made by {qc.user}')


def add_user(username, description, is_moderator, date_of_birth, profile_picture, total_likes,
             total_views, email):
    
    u = User.objects.get_or_create(username=username)[0]
    u.set_password('123')
    u.email = email

    up = UserProfile.objects.get_or_create(user=u)[0]
    up.description = description
    up.is_moderator = is_moderator
    up.total_likes = total_likes
    up.total_views = total_views
    up.date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d").date()
    
    image_path = os.path.join("media", profile_picture)
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            up.profile_picture.save(os.path.basename(profile_picture), File(img_file))

    u.save()
    up.save()
    return (u, up)

def add_walk(user, title, description, area, tags, difficulty, thumbnail):
    w = Walk.objects.get_or_create(user=user, title=title, description=description)[0]
    w.area = area
    w.tags = tags
    w.difficulty = difficulty

    image_path = os.path.join("media", thumbnail)
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            w.thumbnail.save(os.path.basename(thumbnail), File(img_file))

    w.save()
    return w

def add_question(user, title, text):
    q = Question.objects.get_or_create(user=user, title=title, text=text)[0]
    q.save()
    return q

def add_walk_comment(user, walk, text):
    wc = WalkComment.objects.get_or_create(user=user, walk=walk, text=text)[0]
    wc.save()
    return wc

def add_question_comment(user, question, text):
    qc = QuestionComment.objects.get_or_create(user=user, question=question, text=text)[0]
    qc.save()
    return qc
    

if __name__ == '__main__':
    print('Starting Stroll population script...')
    populate()