import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'stroll_group_project.settings')


import django
django.setup()
from stroll.models import *

def populate():
    users = [
        {'username':'ellie1',
        'date_of_birth':'12/10/2000',
        'description':'casual walker',
        'password':'1234',
        'is_moderator':'false',},

        {'username':'kevin2',
        'date_of_birth':'9/3/1982',
        'description':'intermediate walker',
        'password':'12345',
        'is_moderator':'false',},

        {'username':'scott3',
        'date_of_birth':'3/5/1970',
        'description':'pro walker',
        'password':'123456',
        'is_moderator':'true',}
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
        'text':'Ideally a place whit many fields and trees please'},
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

