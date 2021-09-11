from django.db.models import Q
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm,  PasswordResetForm
# from .models import Account
from django.contrib.auth import get_user_model
User = get_user_model()
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.views.generic import CreateView, View
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from main.models import CompanyInfo
from .forms import *

# -----

def login_request(request):
    comp_info = CompanyInfo.objects.all()
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'You are now logged in as {username}')
                return redirect('account:dashboard')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password')
    form = AuthenticationForm()
    arg = {
         'form': form,
        'comp_info': comp_info,
     }
    return render(request, 'account/login.html', arg)


def logout_user(request):
    logout(request)
    return redirect('account:login')

@login_required
def dashboard(request):
    comp_info = CompanyInfo.objects.all ()
    arg = {'title': 'dashboard', 'page_name': 'dashboard', 'comp_info':comp_info,}
    return render ( request, 'private/dashboard.html', arg )


def register_administrators(request):
    comp_info = CompanyInfo.objects.all()
    if request.method == 'POST':
        form = AdminSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username}! Your account has been created, you are now able to log in.')
            return redirect('account:login')
    else:
        form = AdminSignUpForm()
    return render(request, 'account/register.html', {'form': form, 'comp_info': comp_info} )


def register_webmasters(request):
    comp_info = CompanyInfo.objects.all()
    if request.method == 'POST':
        form = WebmasterSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username}! Your account has been created, you are now able to log in.')
            return redirect('account:login')
    else:
        form = WebmasterSignUpForm()
    return render(request, 'account/register.html', {'form': form, 'comp_info': comp_info} )


@login_required
def profile(request):
    comp_info = CompanyInfo.objects.all()
    Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('account:profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    arg = \
        {
         'u_form':  u_form,
         'p_form':  p_form,
         'title': 'my profile',
         'page_name': "User's profile!",
            'comp_info': comp_info
        }

    return render(request, 'account/profile.html', arg)

def change_password(request):
    comp_info = CompanyInfo.objects.all()
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('account:password_change')
        else:
            messages.error(request, 'Please correct the error bellow.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'account/change_password.html', {'form': form, 'comp_info': comp_info })
'''
def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "registration/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:9000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("/password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="registration/password_reset_form.html", 
	context={"password_reset_form":password_reset_form})
'''