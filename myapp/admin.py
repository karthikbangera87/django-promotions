from django.contrib import admin

from .models import myapp
# Register your models here.

class myappAdmin(admin.ModelAdmin):
	list_display = ['email','timestamp','updated']
	class Meta:
		model = myapp

admin.site.register(myapp,myappAdmin)