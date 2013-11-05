from django.contrib import admin
from models import *

class JobAdmin(admin.ModelAdmin):
    search_fields = ['name']
admin.site.register(Job, JobAdmin)

class SkillAdmin(admin.ModelAdmin):
    search_fields = ['name']
admin.site.register(Skill, SkillAdmin)

class PersonAdmin(admin.ModelAdmin):
    search_fields = ['firstname', 'lastname']
    filter_horizontal = ("skills",)
admin.site.register(Person, PersonAdmin)

