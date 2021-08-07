from django.urls import path
from .import views
urlpatterns = [
    path('', views.products, name='home'),
    path('<int:pk>/like', views.like, name='like')
]