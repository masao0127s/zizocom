#!/usr/bin/env python
# coding: utf-8
# Create your models here.

#from random import choice

from django.db import models
from django.contrib.auth import models as auth_models
from django.utils.translation import ugettext_lazy as _
#from datetime import datetime, date


MAX_LENGTH = 512
MODULE_TREE = type('', (), {})().__module__.split('.')
APP_LABEL = MODULE_TREE[MODULE_TREE.index('models') - 1]


## @note corresponding to Profile in the application
class ZizoUser (auth_models.User):
    point = models.IntegerField(_(u'point'), default=0)
    level = models.IntegerField(_(u'level'), default=1)

    class Meta:
        app_label = APP_LABEL

    def __unicode__(self):
        return self.username


class Activity (models.Model):
    datetime = models.DateTimeField(_(u'date'), auto_now_add=True)
    user = models.ForeignKey(
        ZizoUser,
        verbose_name=_(u"zizo user")
    )
    zizo_id = models.IntegerField(_(u'zizo id'), default=0)
    act_type = (('CH', 'check in'), ('MS', 'send message'), ('AC', 'accept'),)
    json = models.TextField(_(u'message json'), blank=True)
    get_point = models.IntegerField(_(u'get point'), default=0)

    class Meta:
        app_label = APP_LABEL
        verbose_name_plural = _(u'activities')

    def __unicode__(self):
        return str(self.id)


class ToDoList (models.Model):
    zizo_id = models.IntegerField(_(u'zizo id'), default=0)
    input_date = models.DateTimeField(_(u'input date'), auto_now_add=True)

    target = models.ForeignKey(
        ZizoUser,
        verbose_name=_(u"zizo user")
    )
    # owner = models.ForeignKey(
    #     User,
    #     verbose_name=_(u"user")
    # )

    message = models.TextField(_(u'message json'), blank=True)
    msg_type = models.IntegerField(_(u'msg type'), default=1)
    done = models.BooleanField(_(u'done'), default=False)

    class Meta:
        app_label = APP_LABEL
        verbose_name_plural = _(u'todolist')

    def __unicode__(self):
        return str(self.id)
