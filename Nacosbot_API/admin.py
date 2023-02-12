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

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title','level','code','unit','desc')
    search_fields = ('title_title','level__level','code','unit','desc')
    ordering = ('unit','title','code')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class LecturerAdmin(admin.ModelAdmin):
    list_display = ('name','title','pics')
    search_fields = ('name','title__title',)
    ordering = ('name','title',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class CoursesToLecturerAdmin(admin.ModelAdmin):
    list_display = ('lecturer','course')
    search_fields = ('lecturer__name','course__title',)
    ordering = ('lecturer','course',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class MaterialAdmin(admin.ModelAdmin):
    list_display = ('file','level','semester')
    search_fields = ('level__level','semester__semester',)
    ordering = ('level','semester',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Classes, ClassesAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Level, LevelAdmin)
admin.site.register(Title)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lecturer, LecturerAdmin)
admin.site.register(CoursesToLecturer, CoursesToLecturerAdmin)
admin.site.register(Semester)
admin.site.register(Material)
