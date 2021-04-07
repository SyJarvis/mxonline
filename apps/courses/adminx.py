# -*- coding: UTF-8 -*-
__author__ = 'shangye'
__date__ = '4/6/21 1:06 PM'

from .models import Course, Lesson, CourseResource, Video
import xadmin


class CourseAdmin(object):
    # 展示哪些字段
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students']
    # 搜索哪些字段
    search_fields = ['name', 'desc', 'detail', 'degree', 'students']
    # 过滤哪些字段
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students']


class LessonAdmin(object):
    # 章节
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course', 'name', 'add_time']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']
    search_fields = ['course', 'name', 'download']
    list_filter = ['course', 'name', 'download', 'add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)