import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'stroll_group_project.settings')


import django
django.setup()
from stroll.models import *

def populate():
    users = [
        {'username':'ellie1',
        'date_of_birth':'2000-10-12',
        'description':'casual walker',
        'password':'1234',
        'is_moderator':False,
        'walks':walks[2],
        'questions':questions[1]},

        {'username':'kevin2',
        'date_of_birth':'1982-03-09',
        'description':'intermediate walker',
        'password':'12345',
        'is_moderator':False,        
        'walks':walks[1],
        'questions':questions[2]},

        {'username':'scott3',
        'date_of_birth':'1970-05-03',
        'description':'pro walker',
        'password':'123456',
        'is_moderator':True,
        'walks':walks[0],
        'questions':questions[0]},
    ]
    
    walks = [
        {'title':'Govan walk',
        'description':'Walking around govan, took photos of the river'},

        {'title':'Milngaive walk',
        'description':'The neighbourhood seems nice'},

        {'title':'City centre walk',
        'description':'There are many places to eat'},
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

        {'text':'There is another way you can take, has some cool shops.'},

        {'text':"try going to glasgow green, it's not too far"},
    ]

    question_comments = [
        {'text':'Try going along the river'},

        {'text':'any quality hiking shoes/boots will be enough'},

        {'text':'here: *link to walk in nature*'},
    ]

    def add_user(username, date_of_birth, description, password, is_moderator):
        u = User.objects.get_or_create(username=username, date_of_birth=date_of_birth)[0]
        u.description = description
        u.password = password
        u.is_moderator = is_moderator
        u.save()
        return u
    
    def add_walk(title, description):
        w = Walk.objects.get_or_create(title=title, description=description)[0]
        w.save()
        return w
    
    def add_question(title, text):
        q = Question.objects.get_or_create(title=title, text=text)[0]
        q.save()
        return q
    
    def add_walk_comment(text):
        wc = WalkComment.objects.get_or_create(text=text)[0]
        wc.save()
        return wc
    
    def add_question_comment(text):
        qc = QuestionComment.objects.get_or_create(text=text)[0]
        qc.save()
        return qc
    
