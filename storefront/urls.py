from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views #import this
# the two lines bellow help us create the urlpatterns for static files and media
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('wb-admin/', include('account.urls')),
    path ('gallery/', include('gallery.urls')),
    path('froala_editor/', include('froala_editor.urls')),


    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='registration/password_reset.html',
             subject_template_name='registration/password_reset_subject.txt',
             email_template_name='registration/password_reset_email.html',
         ),name='password_reset'),

    path ( 'password-reset/done/', auth_views.PasswordResetDoneView.as_view (
        template_name='registration/password_reset_mail_sent.html' ), name='password_reset_done' ),

    path ( 'password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view (
        template_name='registration/password_reset_confirmation.html' ), name='password_reset_confirm' ),

    path ( 'password-reset-complete/',
           auth_views.PasswordResetCompleteView.as_view ( template_name='registration/password_reset_completed.html' ),
           name='password_reset_complete' )
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
