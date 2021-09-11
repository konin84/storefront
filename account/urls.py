from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'account'

urlpatterns = [

    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register-admin', views.register_administrators, name='admin_registration'),
    path('register-webmaster', views.register_webmasters, name='webmaster_registration'),
    path('', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    # Change your password
    path('password_change/', views.change_password,name='password_change'),

    # reset password urls
    # path('password_reset/', views.password_reset_request, name='password_reset_request'),
    # path('password_reset/done/', auth_views.password_reset_done, name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', auth_views.password_reset_confirm, name='password_reset_confirm'),
    # path('reset/done/', auth_views.password_reset_complete, name='password_reset_complete'),
    # end of reset password urls

]
