from django.db import models
from django.contrib.auth.models import User
from menu.models import Food
from django.utils.translation import gettext_lazy as _



class Comment(models.Model):

    food = models.ForeignKey(Food , on_delete = models.CASCADE)
    name = models.CharField(max_length = 35)
    body = models.TextField(_('نظر') , blank = False, null = False)
    date_added = models.DateTimeField(_('تاریخ اضافه شدن') , auto_now_add = True)
    active = models.BooleanField(default = False)


    def __str__(self):
        return 'Comment {} by {}'.format(self.body , self.name)

