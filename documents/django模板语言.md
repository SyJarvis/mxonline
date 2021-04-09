# django模板语言



使用普通的方式

index.html

```
<script src="/js/jquery.min.js" type="text/javascript"></script>
<script src="/js/jquery-migrate-1.2.1.min.js" type="text/javascript"></script>

<a style="color:white" class="fr loginbtn" href="/login/">登录</a>
```

login前面加/号表示根目录下/login



#### 使用模板语言

index.html

静态文件

```
{% load staticfiles %}
<link rel="stylesheet" type="text/css" href="{% static 'css/reset.css' %}">
```



url路由，视图函数

```
<a style="color:white" class="fr loginbtn" href="{% url 'login' %}">登录</a>
```



django验证码

```
<img src="/captcha/image/2f3f82e5f7a054bf5caa93b9b0bb6cc308fb7011/" alt="captcha" class="captcha" /> <input id="id_captcha_0" name="captcha_0" type="hidden" value="2f3f82e5f7a054bf5caa93b9b0bb6cc308fb7011" /> <input autocomplete="off" id="id_captcha_1" name="captcha_1" type="text" />
```

show master status;



grant replication slave on *.* to 'slave'@'%' identified by 'mysql0220';

flush privileges;