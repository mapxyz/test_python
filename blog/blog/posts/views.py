from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from ..posts.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CreateNewsForm
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    return render(request, 'index.html')


# Create your views here.
def manager(request):
    current_user = request.user
    news = News.objects.filter(user_id=current_user).order_by('-created_at').all()
    return render(request, 'manager.html', {
        'news': _pagintanor(request, news),
    })


def list(request):
    news = News.objects.order_by('-created_at').all()
    return render(request, 'list.html', {
        'news': _pagintanor(request, news),
        'current_user': request.user
    })


def assing(request):
    current_user = request.user
    subscribers_ids = Subscription.objects.filter(user_id=current_user).values('subscription_user_id')
    news = News.objects.filter(user_id__in=subscribers_ids).order_by('-created_at').all()
    return render(request, 'list.html', {
        'news': _pagintanor(request, news),
        'current_user':request.user
    })


def edite(request, id):
    news = News.objects.get(id=id)
    if request.method == "POST":
        form = CreateNewsForm(request.POST, instance=news)
        if form.is_valid():
            post = form.save(commit=False)
            post.user_id = request.user
            post.save()
            return redirect('view', id=post.pk)

    else:
        form = CreateNewsForm(instance=news)

    return render(request, 'create.html', {'id': id, 'CreateNewsForm': form})


def create(request):
    if request.method == "POST":
        form = CreateNewsForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user_id = request.user
            post.save()
            return redirect('view', id=post.pk)

    else:
        form = CreateNewsForm()
    return render(request, 'create.html', {'CreateNewsForm': form})


def delete(request, id):
    news = News.objects.get(id=id).delete()
    return redirect('manager')


def view(request, id):
    news = News.objects.get(id=id)
    return render(request, 'view.html', {'news': news})


def setread(request):
    try:
        if request.method == 'GET':
            news_id = request.GET.get('news_id', None)
            if request.user.id and news_id:
                Read.objects.create(user_id=request.user,
                                            news_id=News.objects.get(id = news_id)).save()
                return JsonResponse({'status': True})
    except:
        pass
    return JsonResponse({'status': False})

def setassing(request):
    try:
        if request.method == 'GET':
            user_id = request.GET.get('user_id', None)
            if request.user.id and user_id:
                Subscription.objects.create(user_id=request.user,
                                            subscription_user_id=User.objects.get(id = user_id)).save()
                return JsonResponse({'status': True})
    except:
        pass
    return JsonResponse({'status': False})


def unsetassing(request):
    try:
        if request.method == 'GET':
            user_id = request.GET.get('user_id', None)
            if request.user.id and user_id:
                Subscription.objects.filter(user_id=request.user,
                                            subscription_user_id=User.objects.get(id =user_id)).delete()
                return JsonResponse({'status': True})
    except:
        pass
    return JsonResponse({'status': False})


def _pagintanor(request, items):
    paginator = Paginator(items, 25)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        news = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        news = paginator.page(paginator.num_pages)
    return news
