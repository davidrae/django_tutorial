from django.contrib import admin
from models import Foo
from models import Emailer

class FooAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'dob',)
    list_filter = ('name','dob',)
    search_fields = ('last_name',)
    #fields = ()
    #exclude = (,)

'''class EmailerAdmin(admin.ModelAdmin):
    list_display = ('sender_name', 'subject', 'sender_email',)
    list_filter = ('sender_name','subject',)
    search_fields = ('subject',)'''

admin.site.register(Foo, FooAdmin)

