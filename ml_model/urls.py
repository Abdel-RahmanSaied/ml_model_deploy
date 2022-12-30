from django.urls import path , include
from .views import *
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("model" , ModelResult , basename="Model Result")

urlpatterns = []
urlpatterns +=router.urls


'''
# pip install django-rest-passwordreset
# pip install sendgrid-django
# https://www.getpostman.com/collections/9863284535b81a393c7a
'''