from django.urls import path
from django.urls import include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('hello-viewset',views.HelloViewSets,basename='hello-viewset')
router.register('profile',views.UserProfileViewSets )
router.register('login',views.LoginViewSet,basename='login')
router.register('feed',views.ProfileFeedItmeViewSet)


urlpatterns= [
    path('hello-view/',views.HelloApiViews.as_view()),     
    path('',include(router.urls)),
]