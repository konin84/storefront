from django.urls import path
from . import views
app_name = 'gallery'
urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('view-gallery/', views.public_gallery, name='view-gallery'),
    path('add/', views.add, name='add'),
    path('view-photo/<int:pk>/', views.view, name='view'),
    path('update-photo/<int:pk>/', views.update_picture, name='update-photo'),
    path('delete/<int:pk>', views.delete_photo, name='delete-photo'),

]