# -*- coding: UTF-8 -*-
__author__ = 'shangye'
__date__ = '4/6/21 11:02 AM'

import xadmin
from .models import EmailVerifyRecord, Banner, UserProfile
from xadmin import views


class BaseSetting(object):
    # 主题功能
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    # 页面左上角标题
    site_title = '幕学后台管理系统'
    # 底部title
    site_footer = '幕学在线网'
    # 列表折起
    menu_style = 'accordion'


class EmailVerifyRecordAdmin(object):

    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):

    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']



# 注册模型管理类
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
# 主题
xadmin.site.register(views.BaseAdminView, BaseSetting)
# 标题设置
xadmin.site.register(views.CommAdminView, GlobalSetting)
