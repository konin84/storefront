from django.urls import path
from . import views
app_name = 'main'

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('about-us/', views.about_us, name='about_us'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('add-new-product/', views.add_new_product, name='add_new_product'),
    path('main/<slug:slug>/', views.product_detail, name='product_detail'),

    path('products/', views.products, name='our_products'),
    path('product-list/', views.product_list, name='product_list'),
    path('delete-product/<int:pk>/', views.delete_product, name='delete_product'),
    path('update-product/<int:pk>/', views.update_product, name='update_product'),

    path('add-company/', views.add_company, name='add_company'),

    path('add-about-company/', views.add_about_company, name='add_about_company'),

    path('add-sliders/', views.add_sliders, name='add_sliders'),

    path('messages/', views.msg_list, name='msg_list'),
    path('delete-msg/<int:pk>', views.delete_msg, name='delete_msg'),
    path('message/<int:id>/', views.msg_detail, name='msg_detail'),
    path('staff-registration', views.staff_management, name='register_staff'),
]