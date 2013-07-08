from django.contrib import admin
from models import Foo

class FooAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'dob',)
    list_filter = ('name','dob',)
    search_fields = ('last_name',)
    #fields = ()
    #exclude = (,)



admin.site.register(Foo, FooAdmin)

