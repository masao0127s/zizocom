# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name=b'User',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, primary_key=True, to_field='id', serialize=False, to=settings.AUTH_USER_MODEL)),
                (b'point', models.IntegerField(default=0, verbose_name='point')),
                (b'level', models.IntegerField(default=1, verbose_name='level')),
            ],
            options={
            },
            bases=(b'auth.user',),
        ),
    ]
