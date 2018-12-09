from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class News(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length = 160)
    text = models.TextField() #RichTextUploadingField() #
    user_id = models.ForeignKey(User, on_delete=None)
    created_at = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return str(self.id)  + " " +str(self.title)

    class Meta:
        verbose_name = 'Посты'
        verbose_name_plural = 'Посты'
        ordering = ["-title"]

    def getAssing(self):
        return Subscription.objects.get(subscription_user_id = self.user_id)

    def getDateFormatted(self):
        return self.created_at.strftime("%Y-%m-%d %H:%M:%S")

    def getLink(self):
        return '/post/view/' + str(self.id)


class Subscription(models.Model):
    id = models.AutoField(primary_key=True)
    subscription_user_id = models.ForeignKey(User, on_delete = None, related_name = 'subscription_user')
    user_id = models.ForeignKey(User, on_delete = None)

    class Meta:
        verbose_name = 'Подписки на ленты'
        verbose_name_plural = 'Подписки на ленты'


