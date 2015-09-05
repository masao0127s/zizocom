#!/usr/bin/env python
# coding: utf-8
from django.contrib import admin
from django.db.models import get_models
from django.contrib.admin.sites import AlreadyRegistered
from django.contrib.auth.forms import PasswordResetForm
from django.utils.html import format_html

from models import *

class ZizoUserAdmin (admin.ModelAdmin):

	list_display = (
		'id',
		'username',
		'point',
		'level',
	)


class ActivityAdmin (admin.ModelAdmin):

	list_display = (
		'datetime',
		'zizo_id',
		'act_type',
		'json',
		'get_point',
	)

	def user(self, obj):
		return '%s' % (obj.user.id)


class ToDoListAdmin (admin.ModelAdmin):

	list_display = (
		'zizo_id',
		'input_date',
		'message',
		'done',
	)

	def target(self, obj):
		return '%s' % (obj.user.id)


admin.site.register(ZizoUser, ZizoUserAdmin)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(ToDoList, ToDoListAdmin)
