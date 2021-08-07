from django.contrib import admin
from .models import  *

# Register your models here.
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
class QuoteUserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'quote_id')
admin.site.register(Quote, QuoteAdmin)
admin.site.register(QuoteUser, QuoteUserAdmin)