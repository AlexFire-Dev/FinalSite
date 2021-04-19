from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import UpdateView

from .models import User
from .forms import ProfileChangeForm


def AccountView(request, userid):

    if User.objects.filter(id=userid):
        user = User.objects.get(id=userid)
    else:
        return redirect(reverse_lazy('index'))

    context = {
        'accountuser': user,
    }

    return render(request, 'accounts/account.html', context=context)


class ProfileChangeView(UpdateView):
    form_class = ProfileChangeForm
    template_name = 'accounts/profile-change.html'

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        url = reverse('user-account', args=[self.request.user.id])
        return url
