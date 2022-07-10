from django.shortcuts import render
from pages.models import WhatWeDo, Moderator

# Create your views here.


def pages(request):
    what_we_do = WhatWeDo.objects.order_by('created').all()
    moderators = Moderator.objects.order_by('-is_staff', 'created').all()

    context = {'what_we_do': what_we_do, 'moderators': moderators}
    return render(request, 'pages/index.html', context)


def moderator(request, pk):
    moderator = Moderator.objects.order_by('-is_staff', 'created').get(id=pk)
    context = {'moderator': moderator}
    return render(request, 'pages/moderator-profile.html', context)
