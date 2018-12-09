"""blog URL Configuration

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
from blog.posts import views, auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login/', auth_views.auth, name='login'),
    path('blog/manager/', views.manager, name='manager'),
    path('blog/list/', views.list, name='list'),
    path('blog/assing/', views.assing, name='assing'),
    path('post/create/', views.create, name='create'),
    path('post/view/<int:id>', views.view, name='view'),
    path('post/delete/<int:id>', views.delete, name='delete'),
    path('post/edite/<int:id>', views.edite, name='edite'),
    path('assing/set', views.setassing, name='setassing'),
    path('assing/unset', views.unsetassing, name='unsetassing'),
]
