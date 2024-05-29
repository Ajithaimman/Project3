from django.contrib import admin
from .models import Food,FoodSharing

class FoodAdmin(admin.ModelAdmin):
    list_display=('name','quantity','image')

class FoodSharingAdmin(admin.ModelAdmin):
    list_display=('fname','foodname','mobile','location','quantity','foodtype')

admin.site.register(Food,FoodAdmin)
admin.site.register(FoodSharing,FoodSharingAdmin)


