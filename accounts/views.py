from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .forms import ProfileEditForm, UserEditForm
from django.contrib.auth.decorators import login_required

def userprofile(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'profile/detail.html',
                {'user': user})

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'account/edit.html',
                  {'user_form':user_form,
                    'profile_form': profile_form})