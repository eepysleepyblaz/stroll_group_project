from django.contrib import admin
from django.urls import path
from django.urls import include
from stroll import views

urlpatterns = [
    path('', views.home, name='home'),
    path('stroll', include('stroll.urls')),
    path('admin/', admin.site.urls),
]
