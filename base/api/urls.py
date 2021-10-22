from django.urls import path
from .views import getRoutes, getRooms, getRoom

urlpatterns = [
    path('', getRoutes),
    path('rooms/', getRooms),
    path('rooms/<str:pk>/', getRoom),
]
