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
         'image1':'population_thumbnails/george_square.jpg',
        'title':'Govan walk',
        'description':'Walking around govan, took photos of the river',
        'area':'Govan',
        'likes':54,
        'views':260,
        'tags':'govan,river',
        'difficulty':3,
        'map_coordinates':'55.87047957263414,-4.299474367998468:55.870118396129584,-4.300654539965021:55.8697210980949,-4.300869116686212:55.86811081998383,-4.3002269758135565:55.86696701310203,-4.302930642500568:55.867243937858554,-4.3039204644154:55.86722587760855,-4.304574923415034:55.866997113714696,-4.304950432677119:55.86664192499892,-4.304961161513178:55.86643723850104,-4.305218653578608:55.86594765646106,-4.305232843662976:55.86599581869407,-4.305833658482312:55.86507320225439,-4.308116622775701:55.864018111323304,-4.310292298708496:55.863575580667074,-4.311046546857013:55.863048754810535,-4.311564760612221:55.86211553011516,-4.309547739433022:55.86176099025806,-4.308306304295213:55.861026429639274,-4.309250441868455:55.859418192512614,-4.309500984134309:55.85979151099995,-4.309050373019807:55.85909804950205,-4.305438263729433:55.86051511722765,-4.304134020217143:55.86010567858044,-4.302567610152446:55.86170728165541,-4.301730760939799:',
        'length':2611,},

        {'thumbnail':'population_thumbnails/milngavie.jpg',
         'image1':'population_thumbnails/hospital.jpg',
        'title':'Milngavie walk',
        'description':'The neighbourhood seems nice',
        'area':'Milngavie',
        'likes':1893,
        'views':5845,
        'tags':'milngavie,nice',
        'difficulty':2,
        'map_coordinates':'55.89070209215165,-4.326006698608391:55.89734367953969,-4.319826889038079:55.90829750406234,-4.32624925601597:55.91435885725265,-4.3214427374612825:55.91791825797361,-4.322301044346048:55.9260252142379,-4.315391992174451:55.93439157824028,-4.316765283190076:55.93837250385503,-4.317537043562125:55.93834245858048,-4.31815931605358:55.94051647120524,-4.320054016805552:55.94100398609752,-4.318460729473423:55.94145463180274,-4.317634609096836:55.94194215861572,-4.31833136762447:55.94275329746196,-4.318899995935627:55.94305972327176,-4.31908238614864:55.94310178152705,-4.3183957406408275:55.944039526233766,-4.317637295053253:55.945681560667516,-4.3170719657686485:',
        'length':6676},

        {'thumbnail':'population_thumbnails/town.jpg',
         'image1':'population_thumbnails/buchanan_street.jpg',
        'title':'City centre walk',
        'description':'There are many places to eat',
        'area':'Town',
        'likes':53878,
        'views':104953,
        'tags':'city centre,town,shops',
        'difficulty':4,
        'map_coordinates':'55.864814645858175,-4.273504037960225:55.86479658447859,-4.273654241665059:55.864567806276646,-4.273579139812642:55.8646340316842,-4.272849578960591:55.863177046636,-4.272452612026387:55.8631529637794,-4.270982761486226:55.86288214696901,-4.268448558605062:55.86176492101188,-4.258342392743515:55.85864012887004,-4.259455867610145:55.85835109985388,-4.256859489283729:55.85751030930412,-4.249340239260224:55.85872665155361,-4.248889628145722:55.85888320769095,-4.249919596407441:55.85943114920384,-4.249747935030488:55.85941910661627,-4.249361696932343:55.85988274354265,-4.249211493227509:55.859894785986484,-4.249415341112641:55.86065662485796,-4.249125662539033:55.86092757354435,-4.2516040236687935:55.86167417792462,-4.25119632789853:55.86187238780644,-4.252401751238494:55.862305578147044,-4.252295779046113:55.862460604629646,-4.253404501508073:55.8634961724381,-4.252996805737809:55.86415666528009,-4.252889882846809:55.86431319953641,-4.254220258518195:55.86543034269678,-4.263206891495026:55.86399269375848,-4.263784159711395:55.86319796829471,-4.264020194104705:55.86308959538082,-4.262561072400604:55.86373982832909,-4.262282122663055:',
        'length':4299,},

        {'thumbnail':'population_thumbnails/partick.jpg',
         'image1':'population_thumbnails/bridge.jpg',
        'title':'Partick walk to university',
        'description':'Lots of pubs and shops',
        'area':'Partick, University',
        'likes':357,
        'views':4630,
        'tags':'partick,shops,pubs,university',
        'difficulty':7,
        'map_coordinates':'55.87002755653818,-4.295302244312018:55.87005163513266,-4.297791334277838:55.87077398602456,-4.300795408374518:55.87082214227296,-4.31272587407276:55.87327672865446,-4.313786029815674:55.87320449882518,-4.317948818206787:55.870709203774744,-4.318666675242501:55.870697164683236,-4.316606738719064:55.8696136311635,-4.316585281046945:55.86916816972535,-4.315748431834298:55.86923918175563,-4.3081986383485145:55.869435868069594,-4.306687678829113:55.869122840213976,-4.304284419551769:55.86909876104366,-4.303254451290051:55.86967665701093,-4.3008082766684685:55.868075382504884,-4.30022429350646:55.86813558198892,-4.298336018359976:55.86786626169952,-4.295105223909605:55.86678264919653,-4.290427451387632:55.86625287208084,-4.2892258217489605:55.86790238159561,-4.2878525307333355:55.87196656935269,-4.285074735924104:55.87276630804169,-4.291445307178425:55.87275426958792,-4.29631619874947:55.87188749110705,-4.295200399799275:55.87114108302303,-4.295050196094441:55.87106884922127,-4.297174505634236:55.870189993871485,-4.297389082355427:',
        'length':5950,},
    ]

    questions = [
        {'question':'What are some good walks around Govan?',
         'likes':6410,
         'views':8748,
         'comment_count':1},

        {'question':'Can anyone recommend some shoes for long walks?',
         'likes':5989,
         'views':15699,
         'comment_count':1},

        {'question':'Where can I go for more nature walks?',
         'likes':84,
         'views':374,
         'comment_count':1},
         
         {'question':'Where can I go for more nature walks?',
         'likes':84,
         'views':374,
         'comment_count':0},
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

    users = [

        {'username':'ellie1',
        'description':'casual walker',
        'email':'ellie@gmail.com',
        'date_of_birth':'2005-08-14',
        'profile_picture':'population_profile_pictures/ellie1.jpg',
        'total_likes':walks[2]['likes'] + questions[1]['likes'],
        'total_views':walks[2]['views'] + questions[1]['views'],
        'is_moderator':False,
        'walks':[walks[2],walks[3]],
        'questions':[questions[1], questions[3]],
        'comments':([walk_comments[0]], [question_comments[2]]),
        'commented_on':([walks[0]], [questions[2]])},

        {'username':'kevin2',
        'description':'intermediate walker',
        'date_of_birth':'1979-10-12',
        'email':'kevin@gmail.com',
        'profile_picture':'population_profile_pictures/kevin2.jpg',
        'total_likes':walks[1]['likes'] + questions[2]['likes'],
        'total_views':walks[1]['views'] + questions[2]['views'],
        'is_moderator':False,        
        'walks':[walks[1]],
        'questions':[questions[2]],
        'comments':([walk_comments[2]], [question_comments[0]]),
        'commented_on':([walks[2]], [questions[0]])},

        {'username':'scott3',
        'description':'pro walker',
        'date_of_birth':'1965-01-05',
        'email':'scott@gmail.com',
        'profile_picture':'population_profile_pictures/scott3.jpg',
        'total_likes':walks[0]['likes'] + questions[0]['likes'],
        'total_views':walks[0]['views'] + questions[0]['views'],
        'is_moderator':True,
        'walks':[walks[0]],
        'questions':[questions[0]],
        'comments':([walk_comments[1]], [question_comments[1]]),
        'commented_on':([walks[1]], [questions[1]])}
    ]
        

    for user in users:
        add_user(user['username'], user['description'], user['is_moderator'],
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
            if walk.title == users[0]['commented_on'][0][0]['title'] and user_profile.user.username == 'ellie1':
                add_walk_comment_helper(user_profile, walk, 0, users)
            
            elif walk.title == users[1]['commented_on'][0][0]['title'] and user_profile.user.username == 'kevin2': 
                add_walk_comment_helper(user_profile, walk, 1, users)

            elif walk.title == users[2]['commented_on'][0][0]['title'] and user_profile.user.username == 'scott3': 
                add_walk_comment_helper(user_profile, walk, 2, users)



        for question in Question.objects.all():
            if question.question == users[0]['commented_on'][1][0]['question'] and user_profile.user.username == 'ellie1':
                add_question_comment_helper(user_profile, question, 0, users)

            elif question.question == users[1]['commented_on'][1][0]['question'] and user_profile.user.username == 'kevin2':
                add_question_comment_helper(user_profile, question, 1, users)

            elif question.question == users[2]['commented_on'][1][0]['question'] and user_profile.user.username == 'scott3':
                add_question_comment_helper(user_profile, question, 2, users)



    for user_profile in UserProfile.objects.all():
        for walk in Walk.objects.filter(user=user_profile.user):
            for walk_comment in WalkComment.objects.filter(walk=walk):
                print(f'- {user_profile}:\n     Walk: {walk}\n     Comment: {walk_comment} comment made by {walk_comment.user}\n')

        for question in Question.objects.filter(user=user_profile):
            for question_comment in QuestionComment.objects.filter(question=question):
                print(f'- {user_profile}:\n     Questoin: {question}\n     Comment: {question_comment} comment made by {question_comment.user}\n')


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
    w = add_walk_helper(user_profile.user, walks)
    q = add_question_helper(user_profile, questions)


def add_walk_helper(user, walks):
    for walk in walks:
        add_walk(user, walk['title'], walk['description'], walk['area'],
                    walk['tags'], walk['difficulty'], walk['thumbnail'], walk['image1'], walk['likes'], walk['views'], walk['map_coordinates'], walk['length'])
        
def add_question_helper(user_profile, questions):
    for question in questions:
        add_question(user_profile, question['question'], question['likes'], question['views'],
                     question['comment_count'])



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

def add_walk(user, title, description, area, tags, difficulty, thumbnail, image1, likes, views, map_coordinates, length):
    w = Walk.objects.get_or_create(user=user, title=title, description=description)[0]
    w.area = area
    w.tags = tags
    w.likes = likes
    w.views = views
    w.difficulty = difficulty
    w.map_coordinates = map_coordinates
    w.length = length

    image_path = os.path.join("media", thumbnail)
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            w.thumbnail.save(os.path.basename(thumbnail), File(img_file))

    image_path = os.path.join("media", image1)
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            w.gallery_image_1.save(os.path.basename(image1), File(img_file))

    w.save()
    return w

def add_question(user, question, likes, views, comment_count):
    q = Question.objects.get_or_create(user=user, question=question)[0]
    q.likes = likes
    q.views = views
    q.comment_count = comment_count
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