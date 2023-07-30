from django.urls import path
from . import views




urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('<slug:slug>/', views.PostListView.as_view(), name='post_list'),
]