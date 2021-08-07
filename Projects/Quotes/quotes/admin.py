from django.contrib import admin
from .models import *
# Register your models here.
class QuotesAdmin(admin.ModelAdmin):
    list_display = ('title',  'likes')
admin.site.register(Quote, QuotesAdmin)