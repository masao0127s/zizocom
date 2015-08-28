# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        (b'z_server', b'0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name=b'Activity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                (b'datetime', models.DateTimeField(auto_now_add=True, verbose_name='date')),
                (b'user', models.ForeignKey(to=b'z_server.User', to_field='user_ptr', verbose_name='user')),
                (b'zizo_id', models.IntegerField(default=0, verbose_name='zizo id')),
                (b'json', models.TextField(verbose_name='message json', blank=True)),
                (b'get_point', models.IntegerField(default=0, verbose_name='get point')),
            ],
            options={
                'verbose_name_plural': 'activities',
            },
            bases=(models.Model,),
        ),
    ]
