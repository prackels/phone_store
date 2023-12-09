from django.urls import path
from .api.view import create, get, delete
urlpatterns = [
    path('post/', create.create_phone, name= 'create_phone'),
    path('get/', get.ViewPhones, name= 'Viewphone'),
    path('phones/<int:pk>/delete/', delete.delete_phone, name='delete_phone'),
]
