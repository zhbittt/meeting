from django.contrib import admin
from web.models import *


@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'password')


@admin.register(MeetingRoom)
class MeetingRoomAdmin(admin.ModelAdmin):

    list_display = ('title',)



