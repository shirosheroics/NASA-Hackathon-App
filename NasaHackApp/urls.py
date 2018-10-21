"""NasaHackApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from socialusers import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('list/', views.list, name='list'),
    path('list/detail/<int:article_id>/', views.detail, name='story-detail'),
    
    path('profiles/', views.profiles, name='profiles'),
    path('profile/<int:user_id>/', views.profile, name='profile'),
    path('my-profile/', views.my_profile, name='my-profile'),
    path('create/', views.create, name='create'),
    
    path('maps/',views.maps ,name='maps'),
    path('map/<int:map_id>/',views.map_detail ,name='map-detail'),
    path('map/<int:map_id>/camp/<int:camp_id>/',views.camp_detail ,name='camp-detail'),

    path('quests/', views.quests, name='quests'),
    path('quest-detail/<int:quest_id>/', views.quest_detail, name='quest-detail'),

    path('signup/',views.signup ,name='signup'),
    path('signin/',views.signin ,name='signin'),
    path('signout/',views.signout ,name='signout'),
    path('no-access/',views.no_access ,name='no-access'),

]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)