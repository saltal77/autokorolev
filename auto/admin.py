#-*- coding: utf-8 -*-


from django.contrib import admin
from .models import *

class InterestAdmin(admin.ModelAdmin):
    list_display = ['name',]

class TypeOfWorksAdmin(admin.ModelAdmin):
    list_display = ['type',]

class ServiceItemsAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']

class CommentsAdmin(admin.ModelAdmin):
    list_display = ['author','date', 'flag',]

class AdressAdmin(admin.ModelAdmin):
    list_display = ['name']

class ServiceListAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']

class ServiceListTOAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']

class ImageOfWorksAdmin(admin.ModelAdmin):
    list_display = ['name', 'text', 'date']


admin.site.register(Interest, InterestAdmin)
admin.site.register(TypeOfWorks, TypeOfWorksAdmin)
admin.site.register(ServiceItems, ServiceItemsAdmin)
admin.site.register(Comments, CommentsAdmin)
admin.site.register(Adress, AdressAdmin)
admin.site.register(ServiceListTO, ServiceListTOAdmin)
admin.site.register(ServiceList, ServiceListAdmin)
admin.site.register(ImageOfWorks, ImageOfWorksAdmin)

