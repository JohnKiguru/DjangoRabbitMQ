from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('quotes', views.QuoteViewSet, basename='quotes')
router.register('quoteusers', views.QuoteUserViewSet, basename='qouteusers')

urlpatterns = [
    path('', include(router.urls)),
    path('quotes/<int:pk>/like', views.like, name='like'),

]
