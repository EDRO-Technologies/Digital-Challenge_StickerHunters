from django.contrib import admin
from .models import Form, User

# Register your models here.
class formAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "factory",
        "Change",
        "duration",
        "data",
        "team",
        "message",
        "incident",
        "status"
    )


class UserAdmine(admin.ModelAdmin):
    list_display = (
        "name",
        "password"
    )

admin.site.register(Form, formAdmin)
admin.site.register(User, UserAdmine)
