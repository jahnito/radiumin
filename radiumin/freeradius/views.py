from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import RadcheckModel, RadusergroupModel
from .forms import RadiusLogin


def index(request):
    def login(request):
        form = RadiusLogin()
        return render(request, 'freeradius/index.html', context={'form': form})

    if request.method == 'POST':
        form = RadiusLogin(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = RadcheckModel.objects.filter(
                rad_username=username,
                value=password).first()
            if user is not None:
                groups = RadusergroupModel.objects.filter(
                    rad_username=user.rad_username
                )
                context = {
                    'user': user,
                    'groups': groups,
                }
                return render(
                    request, 'freeradius/user.html', context=context
                )
            else:
                return login(request)
        else:
            return login(request)
    else:
        return login(request)
