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
        {'question':'What are some good walks around Govan?'},

        {'question':'Can anyone recommend some shoes for long walks?'},

        {'question':'Where can I go for more nature walks?'},
    ]

    walk_comments = [
        {'comment':'nice walk'},

        {'comment':'There is another way you can take, has some interesting shops.'},

        {'comment':"try going to glasgow green, it's not too far"},
    ]

    question_comments = [
        {'comment':'Try going along the river'},

        {'comment':'any quality hiking shoes/boots will be enough'},

        {'comment':'try walking east along river clyde'},
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
        'comments':([walk_comments[0]], [question_comments[2]]),},

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
        'comments':([walk_comments[2]], [question_comments[0]]),},

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
        'comments':([walk_comments[1]], [question_comments[1]]),}
    ]
        

    for user in users:
        u = add_user(user['username'], user['description'], user['is_moderator'],
                     user['date_of_birth'], user['profile_picture'], user['total_likes'],
                     user['total_views'], user['email'])
        
    for user_profile in UserProfile.objects.all():
        if user_profile.user.username == 'ellie1':
            add_walk_and_question(user_profile, 0, users)
                
        elif user_profile.user.username == 'kevin2':
            add_walk_and_question(user_profile, 1, users)

        elif user_profile.user.username == 'scott3':
            add_walk_and_question(user_profile, 2, users)


    for user_profile in UserProfile.objects.all():
        for walk in Walk.objects.all():
            if walk.user == user_profile.user and user_profile.user.username == 'ellie1':
                add_walk_comment_helper(user_profile, walk, 0, users)
            
            elif walk.user == user_profile.user and user_profile.user.username == 'kevin2':
                add_walk_comment_helper(user_profile, walk, 1, users)

            elif walk.user == user_profile.user and user_profile.user.username == 'scott3':
                add_walk_comment_helper(user_profile, walk, 2, users)



        for question in Question.objects.all():
            if question.user == user_profile and user_profile.user.username == 'ellie1':
                add_question_comment_helper(user_profile, question, 0, users)

            elif question.user == user_profile and user_profile.user.username == 'kevin2':
                add_question_comment_helper(user_profile, question, 1, users)

            elif question.user == user_profile and user_profile.user.username == 'scott3':
                add_question_comment_helper(user_profile, question, 2, users)



    for user_profile in UserProfile.objects.all():
        for walk in Walk.objects.filter(user=user_profile.user):
            for walk_comment in WalkComment.objects.filter(walk=walk):
                print(f'- {user_profile}:\n     Walk: {walk}:\n     {walk_comment} comment made by {walk_comment.user}')

        for question in Question.objects.filter(user=user_profile):
            for question_comment in QuestionComment.objects.filter(question=question):
                print(f'- {user_profile}:\n     Walk: {question}:\n     {question_comment} comment made by {question_comment.user}')


def add_question_comment_helper(user_profile, question, user_index, users):
    question_comments = users[user_index]['comments'][1]

    for comment in question_comments:
        add_question_comment(user_profile, question, comment['comment'])

def add_walk_comment_helper(user_profile, walk, user_index, users):
    walk_comments = users[user_index]['comments'][0]
    for comment in walk_comments:
        add_walk_comment(user_profile, walk, comment['comment'])

def add_walk_and_question(user_profile, user_index, users):
    walks = users[user_index]['walks']
    questions = users[user_index]['questions']
    add_walk_helper(user_profile.user, walks)
    add_question_helper(user_profile, questions)


def add_walk_helper(user, walks):
    for walk in walks:
        add_walk(user, walk['title'], walk['description'], walk['area'],
                    walk['tags'], walk['difficulty'], walk['thumbnail'])
        
def add_question_helper(user_profile, questions):
    for question in questions:
        add_question(user_profile, question['question'])



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

def add_question(user, question):
    q = Question.objects.get_or_create(user=user, question=question)[0]
    q.save()
    return q

def add_walk_comment(user, walk, comment):
    wc = WalkComment.objects.get_or_create(user=user, walk=walk, comment=comment)[0]
    wc.save()
    return wc

def add_question_comment(user, question, comment):
    qc = QuestionComment.objects.get_or_create(user=user, question=question, comment=comment)[0]
    qc.save()
    return qc
    

if __name__ == '__main__':
    print('Starting Stroll population script...')
    populate()