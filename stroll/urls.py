from django.urls import path
from stroll import views

app_name = 'stroll'

urlpatterns = [
    path('', views.home, name='home'),
]