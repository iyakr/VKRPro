from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *
from django.conf.urls import include

# router = DefaultRouter()
# router.register('users/', UserViewSet)

urlpatterns = [
    path('', ProfileUser.as_view()),
    path('reg/', RegUser.as_view()),
    path('red/<int:pk>/', RedactProfile.as_view()),
    # path('check/', CheckPerm.as_view()),


]
