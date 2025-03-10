import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'stroll_group_project.settings')


import django
django.setup()
from stroll.models import *

def populate():
    
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
        'password':'1234',
        'is_moderator':False,
        'walks':[walks[2]],
        'questions':[questions[1]],
        'comments':[walk_comments[0], question_comments[2]],
        'commented_on':[walks[0], questions[2]]},

        {'username':'kevin2',
        'description':'intermediate walker',
        'password':'12345',
        'is_moderator':False,        
        'walks':[walks[1]],
        'questions':[questions[2]],
        'comments':[walk_comments[2], question_comments[0]],
        'commented_on':[walks[2], questions[0]]},

        {'username':'scott3',
        'description':'pro walker',
        'password':'123456',
        'is_moderator':True,
        'walks':[walks[0]],
        'questions':[questions[0]],
        'comments':[walk_comments[1], question_comments[1]],
        'commented_on':[walks[1], questions[1]]},
    ]

    for user in users:
        u = add_user(user['username'],
                     user['description'], user['password'],
                     user['is_moderator'])
        
        for walk in user['walks']:
            w = add_walk(u, walk['title'], walk['description'])
        
        for question in user['questions']:
            q = add_question(u, question['title'], question['text'])

        for w in Walk.objects.all():
            if w.title == user['commented_on'][0]['title']:
                add_walk_comment(u, w, user['comments'][0]['text'])

        for q in Question.objects.all():
            if q.title == user['commented_on'][1]['title']:
                add_question_comment(u, q, user['comments'][1]['text'])

    for u in User.objects.all():
        for w in Walk.objects.filter(user=u):
            for wc in WalkComment.objects.filter(walk=w):
                print(f'- {u}: Walk, {w}: {wc} comment made by {wc.user}')

        for q in Question.objects.filter(user=u):
            for qc in QuestionComment.objects.filter(question=q):
                print(f'- {u}: Question, {q}: {qc} comment made by {qc.user}')


def add_user(username, description, password, is_moderator):
    u = User.objects.get_or_create(username=username)[0]
    u.description = description
    u.password = password
    u.is_moderator = is_moderator
    u.save()
    return u

def add_walk(user, title, description):
    w = Walk.objects.get_or_create(user=user, title=title, description=description)[0]
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