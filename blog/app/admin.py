from django.contrib import admin
from .models import Registration,Blog

class RegistrationAdmin(admin.ModelAdmin):
    list_display = "firstname", "lastname", "email", "password","user_name"

class BlogAdmin(admin.ModelAdmin):
    list_display = "id","title", "post", "date", "username"

# Register your models here.
admin.site.register(Registration, RegistrationAdmin)
admin.site.register(Blog, BlogAdmin)