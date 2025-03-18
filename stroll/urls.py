from django.urls import path
from stroll import views

app_name = 'stroll'

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('signup/', views.signup, name='signup'),
    path('create-walk/', views.create_walk, name='create_walk'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('my-profile/', views.my_profile, name='my_profile'),
    path('my-profile/edit-profile/', views.edit_profile, name='edit_profile'),
    path('my-profile/my-walks', views.my_walks, name='my_walks'),
    path('my-profile/my-questions/', views.my_questions, name='my_questions'),
    path('search-walks/', views.search_walks, name='search_walks'),
    path('walk/<slug:walk_name_slug>/', views.show_walk, name='show_walk'),
    path('questions/', views.questions, name='questions'),
    path('questions/<slug:question-slug>', views.show_question, name='show_question'),
]