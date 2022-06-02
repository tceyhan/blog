from django.contrib import admin
from .models import User, UserProfile

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'date_joined',)    
    search_fields = ['username', 'first_name']

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'profile_pic')
    search_fields = ['user']

admin.site.register(User, UserAdmin)
admin.site.register(UserProfile)


