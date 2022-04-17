from django.contrib import admin
from .models import User, Character
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list = ('username', 'email')

class CharacterAdmin(admin.ModelAdmin):
    list = ('id', 'name', 'rarity', 'element', 'weapon', 'region')

admin.site.register(User,UserAdmin)
admin.site.register(Character, CharacterAdmin)