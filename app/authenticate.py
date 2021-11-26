from django.shortcuts import redirect
from app.models import User, Admin
from django.contrib import messages
from django.db.models import Q


class Authenticate:
	def valid_user(function):
		def wrap(request):
			try:
				User.objects.get(Q(password=request.session['password']) & Q(user_name=request.session['user_name']))
				return function (request)
			except:
				messages.warning(request,"Invalid username or password")
				return redirect('/login')
		return wrap


	def valid_admin(function):
		def wrap(request):
			try:
				Admin.objects.get(Q(username=request.session['username']) & Q(password=request.session['password']))
				return function (request)
			except:
				messages.warning(request,"Invalid username or password")
				return redirect('/adminlogin')
		return wrap
