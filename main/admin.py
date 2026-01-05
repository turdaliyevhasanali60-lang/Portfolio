from django.contrib import admin
from main.models import *

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('profile_image', 'full_name', 'telegram_link')
    search_fields = ('full_name',)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'level',)
    search_fields = ('name',)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon',)
    search_fields = ('title', 'icon')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image',)
    search_fields = ('title', 'description',)

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role',)
    search_fields = ('name',)

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('photo', 'name', 'profession', 'message',)
    search_fields = ('name','message',)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('created_at',)

@admin.register(Results)
class ResultsAdmin(admin.ModelAdmin):
    list_display = ('happy_clients', 'completed_projects',)
    search_fields = ('happy_clients', 'completed_projects',)

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'school', 'year')
    search_fields = ('degree', 'school')