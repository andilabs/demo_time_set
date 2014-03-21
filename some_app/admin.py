from django.contrib import admin
from some_app.models import DemoClass


class DemoClassAdmin(admin.ModelAdmin):
    list_display = ['title', 'timestamp_from', 'timestamp_to']


admin.site.register(DemoClass, DemoClassAdmin)
