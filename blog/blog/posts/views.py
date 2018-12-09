from django.shortcuts import render
from django.http import HttpResponse
from ..posts.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CreateNewsForm
from django.shortcuts import redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')





# Create your views here.
def manager(request):
    current_user = request.user
    news = News.objects.filter(user_id=current_user).all()
    return render(request, 'manager.html', {
        'news':_pagintanor(request, news),
    })


def create(request):
    if request.method == "POST":
        form = CreateNewsForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user_id = request.user
            post.save()
            #return redirect('view', pk=post.pk)
    else:
        form = CreateNewsForm()
    return render(request, 'create.html', {'CreateNewsForm': CreateNewsForm})


def view(request, id):
    news = News.objects.filter(id=id).one()
    return render(request, 'view.html', {'news': news})

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