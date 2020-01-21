from django.urls import path
from django.urls import include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('hello-viewset',views.HelloViewSets,'hello-viewset')
router.register('profile',views.UserProfileViewSets )


urlpatterns= [
    path('hello-view/',views.HelloApiViews.as_view()),     
    path('',include(router.urls)),
]