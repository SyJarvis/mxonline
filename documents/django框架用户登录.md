Pycharm小技巧

Ctrl + R	替换

```
from django.views.generic.base import View
from django.shortcuts import render
```





### django框架用户登录

使用到的方法

```
from django.shortcuts import render	返回html模板，传递参数
from django.contrib.auth import authenticate, login, logout
```

```
return render(request, "login.html", {"msg": "用户名或密码错误"})

# 验证用户是否已经注册
authenticate(username=user_name, password=pass_word)

# 用户登录，建立session会话
login(request, user)

# 用户登出，删除session会话
logout(request, user)
```



#### 验证用户是否已经注册

views.py

```
class CustomBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(username=username)
            if user.check_password(password):
                return user

        except Exception as e:
            return None
```

settings.py

```
AUTHENTICATION_BACKENDS = (
    'users.views.CustomBackend',
)
```



视图函数

views.py

```
def user_login(request):
    if request.method == "POST":
        user_name = request.POST.get("username", "")
        pass_word = request.POST.get("password", "")
        user = authenticate(username=user_name, password=pass_word)
        if user is not None:
            login(request, user)
            return render(request, "index.html")
        else:
            return render(request, "login.html", {"msg": "用户名或密码错误"})
    elif request.method == "GET":
        return render(request, 'login.html', {})
```





使用类写视图对象

```
from django.views.generic.base import View

类方法有这些
http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
```

使用

```

```





forms文件可以用来校验前端传过来的参数

forms.py

```
# -*- coding: UTF-8 -*-
__author__ = 'shangye'
__date__ = '4/7/21 8:49 PM'

from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)

```

views.py

```
 request.POST是一个字典
 
 login_form = LoginForm(request.POST)
 if login_form.is_valid():
 	pass
```

forms文件定义的变量名与html文件里的名字要保持一致，不然django是不做验证的





#### cookie和session的机制



cookie就是本地存储方式

key/value形式存储，一个文本



HTTP是一种无状态的协议

#### 无状态请求

用户发送请求给服务器，请求１和请求２是没有联系的





#### 有状态请求

用户发送请求给服务器，发送请求1，然后服务器发现没有id，分配一个id=1,

然后浏览器会把id=1保存到本机文件，为了安全，会保存域里的．

用户操作浏览器再次请求的时候，请求2中带上cookie中的id=1

服务器看到id是1，取出1的信息



django的login函数会建立一个session会话，将session数据保存到数据库，

因为不能把用户名和密码都保存在本地，这样不安全，所以引入了session机制



session机制

根据用户名和密码，生成一个随机字符串，并且这个字符串是有过期时间的





