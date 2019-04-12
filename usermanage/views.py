from django.shortcuts import render,redirect,HttpResponseRedirect
from django.db import models
from usermanage import models
import time,datetime
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.sessions.models import Session
# Create your views here.


# def login(req):
#     if req.method == "POST":
#         u = req.POST.get('username')
#         p = req.POST.get('password')
#         c = models.Administrator.objects.filter(username=u, password=p).count()
#         if c:
#             response = redirect('/index/')
#             timeout = datetime.datetime.utcnow()+datetime.timedelta(seconds=3)
#             #response.set_cookie(key='user_id', value='611576', domain='test.com', path='/', expires=timeout, secure=False, httponly=False)
#             response.set_signed_cookie(key='user_id', value='611576', domain='test.com', path='/', expires=timeout,
#                                 secure=False, httponly=False)
#             #设置domain只能设置二级域名
#             #secure=False表示https安全使用的
#             #httponly表示只能进行http传输不能修改
#             #expires表示失效时间
#             #设置加密的cookie
#             return response
#             # cookies = '611576'
#             # return render(req, 'login.html', {'cookie': cookies})
#     else:
#         cookies = '611578'
#         return render(req, 'login.html', {'cookie': cookies})


# def index(req):
#     cookie = req.COOKIES.get('user_id')
#     return render(req, 'index.html', {'cookie': cookie})


# def nocookie(req):
#     cookie = req.COOKIES.get('user_id')
#     return render(req, 'nocookie.html', {'cookie': cookie})
#
#
# def login(req):
#     message = '默认值'
#     coo = req.COOKIES.get('sessionid')
#     print(coo)
#     if req.method == 'POST':
#         u = req.POST.get('username')
#         p = req.POST.get('password')
#         obj = models.Administrator.objects.filter(username=u, password=p)
#         c = obj.count()
#         if c:
#             print('################')
#             req.session['is_login'] = True #只有在这里设置了seesion才会在数据库存在
#             req.session['user_id'] = obj[0].id
#             print(type(obj)) #<class 'django.db.models.query.QuerySet'>
#             print(type(obj[0])) #<class 'usermanage.models.Administrator'>
#             print(type(obj.values('id'))) #<class 'django.db.models.query.QuerySet'>
#             # sess = req.session
#             # s = Session.objects.first()
#             # print(sess)  # <django.contrib.sessions.backends.db.SessionStore object at 0x052A2730> session对象
#             # print(s.session_data)  # NzFmNWRmMmNhZDI2YmE3NzhhMGNmZjU4NzAzZTMyYjFlMmZkNTk3Mjp7ImlzX2xvZ2luIjp0cnVlLCJ1c2VyX2lkIjoxfQ==  session值
#             # print(s.get_decoded())  # {'is_login': True, 'user_id': 1} seesion解密后的值
#             return redirect('/index/')
#         else:
#             message='设置seesion失败'
#     return render(req, 'login.html', {'cookie':  message})
#
#
# def index(req):
#     s = req.session['is_login']
#     print(req.session['is_login'])
#     return render(req, 'index.html', {'cookie': "seeion is %s"%s})
#
#
# def operate_session(req):
#     s1=Session.objects.get(pk='infp6edy94scjxsmtvbz0so5w835n2kr') #获取session的值seesion_data
#     print(s1.get_decoded())#解码seesion_data
#     s2 = Session.objects.get(pk='l8j4n5e7jmmxm1go75ybkn1r2aidxmax')
#     print(s2.get_decoded())
#     sess = req.session.get('is_login',None) #获取seesion值
#     print(req.COOKIES.get('sessionid')) #这里放到cookie里面的值就是session的id
#     #del req.session['user_id'] #删除seesion
#     # 所有 键、值、键值对
#     req.session.keys()#所有的键
#     req.session.values()#所有的值
#     print(req.session.items())#所有键值对
#     req.session.clear_expired() #清除过期的
#     req.session.delete("session_key") #清除所有的键值对
#     print(req.session.items())  # 所有键值对
#     return render(req, 'operate_session.html', {'session': 'session is %s'%sess})
#
#
# from django.contrib import auth
# def login_view(req):
#     if req.method == 'POST':
#         username=req.POST.get('username')
#         password=req.POST.get('password')
#         user = auth.authenticate(username=username, password=password)
#         if user is not None and user.is_active:
#             auth.login(req, user)
#             return HttpResponseRedirect("/account/loggedin/")
#     return render(req, 'login_view.html')
#
#
# def auth(fun):
#     def inner(request, *args, **kwargs):
#         is_login = request.session.get('is_login')
#         if is_login:
#             return fun(request, *args, **kwargs)
#         else:
#             return redirect('/login/')
#     return inner
#
# @auth
# def handle_classes(request):
#     user_id = request.session.get('user_id')
#     return render(request, 'class.html', {'userid': user_id})


def user_register(request):
    pass