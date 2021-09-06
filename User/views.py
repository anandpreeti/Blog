from django.shortcuts import render, redirect,  get_object_or_404

from django.contrib import messages
from django.http import HttpResponse
from django.core.mail import send_mail


from .models import User, Profile
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, ProfileMoreInfoUpdateForm
from django.views.generic import DetailView



def dashboard(request):
    return HttpResponse('This is dashboard')

@login_required
def profile(request):
    #user = get_object_or_404(User, pk=user_id)
    u_form = UserUpdateForm()
    p_form = ProfileUpdateForm()
    pinfo_form = ProfileMoreInfoUpdateForm()
    context = {

        'u_form': u_form,
        'p_form': p_form,
        'pinfo_form': pinfo_form
    }
    return render(request, 'user/profile.html', context)

@login_required
def profile_edit(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('User:profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'user/profile_edit.html', context)


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'user/profile_detail.html'


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            print(form)
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f' Account created for {username} !')
            return redirect('login')
        else:
            messages.error(request,
                           f' Unable to create account, the email should not be too similar with username or password')

    form = UserRegisterForm()
    return render(request, 'user/signup.html', {'form': form})


def mail(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if email and subject and message:

            send_mail(subject, message, 'anandpreeti1029@gmail.com', [email], fail_silently=False)
            print('Message successfully sent')

    return render(request, 'user/contact.html')
