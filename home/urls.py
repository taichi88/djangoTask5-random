from django.urls import path
from .views import (HouseCreateView, HouseListView, HouseDetailView, HouseUpdateView, HouseDeleteView, UserCreateView, UserListView, UserDetailView, UserUpdateView, UserDeleteView)

urlpatterns = [
    path('house/new/', HouseCreateView.as_view(), name='house_create'),
    path('house/list/', HouseListView.as_view(), name='house_list'),
    path('house/<int:pk>/', HouseDetailView.as_view(), name='house_detail'),
    path('house/<int:pk>/edit/', HouseUpdateView.as_view(), name='house_edit'),
    path('house/<int:pk>/delete', HouseDeleteView.as_view(), name='house_delete'),


    path('user/new/', UserCreateView.as_view(), name='User_create'),
    path('user/list/', UserListView.as_view(), name='user_list'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('user/<int:pk>/edit', UserUpdateView.as_view(), name='user_edit'),
    path('user/<int:pk>/delete', UserDeleteView.as_view(), name='user_delete'),



]


