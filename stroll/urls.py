from django.urls import path
from stroll import views

app_name = 'stroll'

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('signup/', views.signup, name='signup'),
    path('create-walk/', views.create_walk, name='create_walk'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('my-profile/', views.my_profile, name='my_profile'),
    path('my-profile/edit-profile/', views.edit_profile, name='edit_profile'),
    path('my-profile/my-walks/', views.my_walks, name='my_walks'),
    path('my-profile/my-questions/', views.my_questions, name='my_questions'),
    path('search-walks/', views.search_walks, name='search_walks'),
    path('walk/<str:id>/', views.show_walk, name='show_walk'),
    path('questions/', views.questions, name='questions'),
    path('questions/<int:id>', views.show_question, name='show_question'),
    path('like_walk/', views.LikeWalkView.as_view(), name='like_walk'),
    path('like_question/', views.LikeQuestionView.as_view(), name='like_question'),
    path('delete_walk/', views.DeleteWalkView.as_view(), name='delete_walk'),
    path('delete_question/', views.DeleteQuestionView.as_view(), name='delete_question'),
    path('delete_question_comment/', views.DeleteQuestionCommentView.as_view(), name='delete_question_comment'),
    path('delete_walk_comment/', views.DeleteWalkCommentView.as_view(), name='delete_walk_comment'),
]