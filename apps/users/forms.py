# -*- coding: UTF-8 -*-
__author__ = 'shangye'
__date__ = '4/7/21 8:49 PM'

from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)


