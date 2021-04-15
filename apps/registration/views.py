from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import User


def AccountView(request, userid):

    if User.objects.filter(id=userid):
        user = User.objects.get(id=userid)
    else:
        return redirect(reverse_lazy('index'))

    context = {
        'accountuser': user,
    }

    return render(request, 'accounts/account.html', context=context)
