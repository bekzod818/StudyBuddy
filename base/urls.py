from django.urls import path
from .views import home, room, create_room, update_room, delete_room, loginPage, logoutUser, registerPage, delete_message, userProfile

urlpatterns = [
    path('login/', loginPage, name="login"),
    path('logout/', logoutUser, name="logout"),
    path('register/', registerPage, name="register"),
    path('', home, name='home'),
    path('room/<int:pk>/', room, name='room'),
    path('profile/<str:pk>/', userProfile, name='user_profile'),
    path('create_room/', create_room, name='create_room'),
    path('update_room/<str:pk>/', update_room, name='update_room'),
    path('delete_room/<str:pk>/', delete_room, name='delete_room'),
    path('delete_message/<str:pk>/', delete_message, name='delete_message'),
]