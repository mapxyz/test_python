# Generated by Django 2.1.4 on 2018-12-09 10:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='user_id',
            field=models.ForeignKey(default=0, on_delete=None, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
