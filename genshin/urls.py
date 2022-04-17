from django.urls import path, include
from rest_framework import routers
from genshin import api
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'characters', api.CharacterView, 'character')
router.register(r'users', api.UserView, 'user')

urlpatterns = [
    path('api/', include(router.urls)),
] 