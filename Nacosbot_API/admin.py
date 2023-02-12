from django.contrib import admin
from Nacosbot_API.models import *

# Register your models here.
class LocationAdmin(admin.ModelAdmin):
    list_display = ('location', 'province', 'image',)
    search_fields = ('location', 'province',)
    ordering = ('location', 'province',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class LevelAdmin(admin.ModelAdmin):
    list_display = ('level',)
    search_fields = ('level',)
    ordering = ('level',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class ClassesAdmin(admin.ModelAdmin):
    list_display = ('title','level',)
    search_fields = ('title','level',)
    ordering = ('title','level',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Classes, ClassesAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Level, LevelAdmin)
