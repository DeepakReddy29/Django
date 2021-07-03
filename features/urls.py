from django.urls import path
from django.urls.resolvers import URLPattern
from features import views

urlpatterns = [
    path('$/', views.index, name = 'Info')
]