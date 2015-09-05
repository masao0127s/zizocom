#!/usr/bin/env python
# coding: utf-8
# Create your views here.

from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404

from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
#from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404
from django.core.urlresolvers import reverse

from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout

import logging
logger = logging.getLogger('zizo')
import traceback

from django.core.management import call_command
import urllib
import urllib2

from models import *
from config import *

import json
import commands.generate_json

CH_POINT = 3

# 新規登録
# @csrf_exempt
# def registration(request):
# 	# ID,PWの希望を受け取る
# 	if request.method == 'GET':
# 		usr_id = request.GET['id']
# 		pw = request.GET['password']
# 		# 同じIDがないか検索
# 		serch = ZizoUser.objects.get(username=usr_id)
# 		# 同じIDがなければDBに格納してOKだよと返す
# 		if serch is None:
# 			new_usr = ZizoUser.objects.create(
# 				username = usr_id,
# 				password = password,
# 				)
# 			new_usr.save()
# 			response = HttpResponse()
# 			response['msg'] = 'OK'
# 			# そのIDを次の情報入力のところに引き渡す？
# 		# 同じIDがあれば違うダメだよと返す
# 		else:
# 			response = HttpResponse()
# 			response['msg'] = 'NG'

# 	return render_to_response(
# 		'registration.html'
# 		context_instance = RequestContext(request, {})
# 	)



# その人へのメッセージを送る
@csrf_exempt
def sendmsg(request):
	# 来たIDでメッセージを検索
	if request.method == 'GET':
		usr_id = request.GET['User']
		zizo_id = 1
		# zizo_id = request.GET['zizo_id']

		msg_list = ToDoList.objects.filter(username=usr_id)
		if msg_list is not None:
			# ヒットしたメッセージを古い順にソート
			msg_list = sorted(msg_list, key=lambda x: input_date)
			# ひとつずつ送信
			for obj in msg_list:
				# response = HttpResponse()
				# response['msg'] = obj.message
				# Doneをつける
				obj.done = True
				obj.save()

	return render_to_response(
		'z_server/sendmsg.html',
		context_instance = RequestContext(request, {})
	)

# チェックイン
# @csrf_exempt
# def checkin(request):
# 	# うけとり
# 	if request.method == 'GET':
# 		usr_id = request.GET['id']
# 		zizo_id = request.GET['zizo_id']
# 		# データ格納
# 		usr = ZizoUser.objects.get(username=usr_id)
# 		new_act = Activity.objects.create(
# 			user = usr,
# 			zizo_id = zizo_id,
# 			act_type = 'CH',
# 			get_point = CH_POINT,
# 		)
# 		new_act.save()

# 		# ウェルカムメッセージの送信
# 		welcome = WELCOME_MSG[randint(1, 5)]
# 		response = HttpResponse()
# 		response['msg'] = welcome

# 		# sendmsgに飛ばす
# 		sendmsg(usr_id)

# 	return render_to_response(
# 		'checkin.html'
# 		context_instance = RequestContext(request, {})
# 	)

# メッセージ受信
@csrf_exempt
def getmsg(request):
	# うけとり
	if request.method == 'GET':
		usr_id = request.GET['User']
		# wish = request.GET['wish']
		target = request.GET['NayamiUser']
		# trouble = request.GET['trouble']
		message = request.GET['NayamiStr']
		# zizo_id = request.GET['zizo_id']
		zizo_id = 1

		target_usr = ZizoUser.objects.get(username=target)

		# ToDoListにする
		new_todo = ToDoList.objects.create(
			zizo_id = zizo_id,
			target = target_usr,
			message = message,
		)
		new_todo.save()

		user = ZizoUser.objects.get(username=usr_id)
		# json形式にする
		# json = generate_json(user_id, zizo_id, wish, target, trouble, message)
		# activityにいれる
		#new_act = Activity.objects.create(
		#	user = user,
		#	zizo_id = zizo_id,
		#	act_type = 'MS',
		#	# json = json,
		#	get_point = 0,
		#)
		#new_act.save()

	return render_to_response(
		'z_server/getmsg.html',
		context_instance = RequestContext(request, {})
	)
