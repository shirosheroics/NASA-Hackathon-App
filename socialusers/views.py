from django.shortcuts import render, redirect 
from .models import Article, Camp, Hazerd, Profile, Quest, Task, Material, Maped 
from .forms import SignupForm, SigninForm ,ArticleForm
from django.contrib.auth import login, authenticate, logout

# Create your views here.

def home(request):
    stories = Article.objects.all()
    quests = Quest.objects.all()
    hazards = Hazerd.objects.all()
    context = {
        'stories' : stories,
        'quests' : quests,
        'hazards' : hazards,
    }

    return render(request,'home.html',context)


def list(request):
    stories = Article.objects.all()
    context = {
        'stories':stories,
    }
    return render(request,'list.html', context)


def detail(request, article_id):
    story = Article.objects.get(id = article_id)
    context = {
        'story': story
    }
    return render(request,'detail.html',context)

def my_profile(request):
    profile = Profile.objects.get(owner=request.user)
    context = {
        'profile':profile,
    }
    return render(request,'profile.html',context)


def profile(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    context = {
        'profile':profile,
    }
    return render(request,'profile.html',context)

def create(request):
    if request.user.is_anonymous:
        return redirect('signin')
    form = ArticleForm()
    if request.method == "POST":
        form = RestaurantForm(request.POST, request.FILES)
        if form.is_valid():
            restaurant = form.save(commit=False)
            restaurant.owner = request.user
            restaurant.save()
            return redirect('list')
    context = {
        "form":form,
    }
    return render(request, 'create.html', context)

def maps(request):
    maps = Maped.objects.all()
    context = {
        'maps':maps,
    }
    return render(request,'map.html', context)


def map_detail(request, map_id):
    map_ = Maped.objects.get(id = map_id)
    camps = camps.objects.all()
    context = {
        'map': map_,
        'camps': camps,
    }
    return render(request,'map_detail.html',context)

def camp_detail(request, map_id, camp_id):
    hazards = Hazerd.objects.all()
    camp = Camp.objects.get(id = camp_id)
    context = {
        'camp': camp,
        'hazards': hazards,
    }
    return render(request,'cap_detail.html',context)

def quests(request):
    quests = Quest.objects.all()
    context = {
        'quests':quests,
    }
    return render(request,'quests.html', context)


def quest_detail(request, quest_id):
    quest = Quest.objects.get(id = quest_id)
    tasks = Task.objects.all()
    materials = Material.objects.all()
    stories = Article.objects.all()

    context = {
        'quest': quest,
        'tasks' : tasks,
        'materials' : materials,
        'stories' : stories,
    }
    return render(request,'quest_detail.html',context)

def no_access(request):
    return render(request, 'no_access.html')

def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            user.set_password(user.password)
            user.save()

            login(request, user)
            return redirect("list")
    context = {
        "form":form,
    }
    return render(request, 'signup.html', context)

def signin(request):
    form = SigninForm()
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                return redirect('list')
    context = {
        "form":form
    }
    return render(request, 'signin.html', context)

def signout(request):
    logout(request)
    return redirect("signin")