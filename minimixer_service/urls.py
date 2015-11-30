"""minimixer_service URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.contrib import admin
from rest_framework.authtoken import views
from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter
from minimixer_manager import views

# Register URL routers for viewsets.
router = DefaultRouter()
router.register(r'neworder', views.NewOrderViewSet)
router.register(r'recipes', views.AllRecipeViewSet)
router.register(r'myrecipes', views.MyRecipeViewSet)
router.register(r'drinks', views.DrinkViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'ingredients', views.IngredientViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^users/register', 'minimixer_manager.views.create_auth'),
    url(r'^api-token-auth/', 'rest_framework.authtoken.views.obtain_auth_token'),
    url(r'^tempurature/', 'minimixer_manager.views.get_temp'),
    url(r'^startled/', 'minimixer_manager.views.start_led'),
    url(r'^stopled/', 'minimixer_manager.views.stop_led'),
    url(r'^order/$', views.OrderManager.as_view()),
    #url(r'^neworder/', views.NewOrder.as_view()),
    #url(r'getorder', views.GetOrder.as_view())
]
