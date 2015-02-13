from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from ecvitae.apps.cvitae.models import Author


class AuthorInline(admin.StackedInline):
    model = Author
    can_delete = False
    verbose_name_plural = 'authors'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (AuthorInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)