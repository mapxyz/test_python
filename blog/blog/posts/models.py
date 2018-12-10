from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.core.mail import send_mass_mail

# Create your models here.

class News(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=160)
    text = models.TextField()  # RichTextUploadingField() #
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return str(self.id) + " " + str(self.title)

    class Meta:
        verbose_name = 'Посты'
        verbose_name_plural = 'Посты'
        ordering = ["-title"]

    def getAssing(self):
        return Subscription.objects.get(subscription_user_id=self.user_id)

    def getRead(self):
        return Read.objects.get(news_id=self.id)

    def getDateFormatted(self):
        return self.created_at.strftime("%Y-%m-%d %H:%M:%S")

    def getLink(self):
        return '/post/view/' + str(self.id)

    def save(self, *args, **kwargs):
        super(News, self).save(args, kwargs)
        send_mass_mail(Subscription.getToNews(self,'Добавлена новая новость'))

    def delete (self, *args, **kwargs):
        send_mass_mail(Subscription.getToNews(self, 'Удалена новость'))
        super(News, self).delete(args, kwargs)

class Subscription(models.Model):
    id = models.AutoField(primary_key=True)
    subscription_user_id = models.ForeignKey(User, on_delete=None, related_name='subscription_user')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Подписки на ленты'
        verbose_name_plural = 'Подписки на ленты'

    def getToNews(model_news, header):
        users = Subscription.objects.filter(subscription_user_id=model_news.user_id).all()
        datatuple = ()
        msg = '<a href="%s">%s</a>' % ('/post/view/'+str(model_news.id),model_news.title)
        for user in users:
            datatuple.append((header, msg, 'no@reply.ru',[user.user_id.email]))
        return datatuple


class Read(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    news_id = models.ForeignKey(News, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Прочитанные новости'
        verbose_name_plural = 'Прочитанные новости'