from django.contrib import admin
from .models import User, Contributors, Projects, Issues, Comments

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'active')
    search_fields = ('first_name', 'last_name', 'email', 'active')

class ContributorsAdmin(admin.ModelAdmin):
    list_display = ('project', 'user', 'permission', 'role', 'active')
    search_fields = ('project', 'user', 'permission', 'role', 'active')

class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'type', 'author', 'active')
    search_fields = ('title', 'description', 'type', 'author', 'active')

class IssuesAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'tag', 'priority', 'status', 'author','date_created', 'active')
    search_fields = ('title', 'description', 'tag', 'priority','status', 'author','date_created', 'active')

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('description', 'author_user_id', 'issue_id', 'date_created', 'active')
    search_fields = ('description', 'author_user_id', 'issue_id', 'date_created', 'active')

admin.site.register(User, UserAdmin)
admin.site.register(Contributors, ContributorsAdmin)
admin.site.register(Projects, ProjectsAdmin)
admin.site.register(Issues, IssuesAdmin)
admin.site.register(Comments, CommentsAdmin)