from django.contrib import admin
from ..posts.models import *
#from catalog.pages.forms import PageForm



@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
  pass

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
  pass
