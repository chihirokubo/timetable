from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from ..forms import LoginForm, RegisterForm
from index.models import User
from hashlib import sha1
import datetime

""" 新規登録チェック """
def CreateAdminUser(request, Data):
    # もし、メールアドレスが既に登録されていたらエラーを返す
    if User.objects.filter(email = Data['email']):
        url = ''
    else:
        # ここで新規登録処理
        now = datetime.datetime.now()
        UserData = User(
            name = Data['name'],
            email = Data['email'],
            password = sha1(Data['password'].encode('utf-8')).hexdigest(),
        )
        UserData.save()
        user = User.objects.all().filter(name = Data['name']).first()
        request.session['user_id'] = user.id
        url = '/'

    return url

""" ログインチェック """
def Login(request, Data):
    user = User.objects.all().filter(email = Data['email']).first()
    password = sha1(Data['password'].encode('utf-8')).hexdigest()
    if user and password == user.password:
        request.session['user_id'] = user.id
        request.session['redirect_flag'] = 0
        request.session['redirect_delete_flag'] = 0
        url = '/'
    else:
        url = ''
        
    return url
