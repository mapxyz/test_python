from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class News(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length = 160)
    text = models.TextField() #RichTextUploadingField() #
    user_id = models.ForeignKey(User, on_delete=None)

    def __str__(self):
        return str(self.id)  + " " +str(self.title)

    class Meta:
        verbose_name = 'Посты'
        verbose_name_plural = 'Посты'
        ordering = ["-title"]

    def getLink(self):
        return '/post/view/' + str(self.id)


class Subscription(models.Model):
    id = models.AutoField(primary_key=True)
    subscription_user_id = models.ForeignKey(User, on_delete = None, related_name = 'subscription_user')
    user_id = models.ForeignKey(User, on_delete = None)

    class Meta:
        verbose_name = 'Подписки на ленты'
        verbose_name_plural = 'Подписки на ленты'


