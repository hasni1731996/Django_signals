from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(User_profile)
class CommonInfoAdmin(admin.ModelAdmin):
    fields = ('name', 'age','home_group')
admin.site.register(Student,CommonInfoAdmin)
admin.site.register(Place)
admin.site.register(Restaurant)