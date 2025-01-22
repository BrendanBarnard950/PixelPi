from django.urls import path
from . import views

urlpatterns = [
    path('images/', views.view_images, name='view_images'),
    path('upload/', views.upload_image, name='upload_image'),
    path('delete/<int:id>/', views.delete_image, name='delete_image'),
    path('image/<int:id>/', views.view_full_image, name='view_full_image'),
]
