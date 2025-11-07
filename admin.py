from django.contrib import admin
from .models import Comment


@admin.register(Comment)

class CommentAdmin(admin.ModelAdmin):

    list_display = ['name' , 'food' , 'body' , 'active']
    list_editable = ['active',]
    actions = ['approve_comments']

    def approve_comments(self , request , queryset):
        queryset.update(active = True)