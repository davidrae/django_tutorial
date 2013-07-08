from django.contrib import admin
from models import Foo

class FooAdmin(admin.ModelAdmin):
	list_display = ('name', 'last_name',)


admin.site.register(Foo, FooAdmin)