from pyexpat.errors import messages
from django.shortcuts import redirect, render
from pages.models import WhatWeDo, About, Moderator
from pages.forms import ContactForm
from django.contrib import messages

# Create your views here.


def pages(request):
    what_we_do = WhatWeDo.objects.order_by('created').all()
    moderators = Moderator.objects.order_by('-is_staff', 'created').all()
    # todays_forecast = Map.objects.order_by('-created').all()[0]

    # contact page
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.name = contact.name.title()
            contact.save()
            messages.success(request,
                             'THANK YOU FOR HAVING INTEREST IN US. WE WILL GET BACK TO YOU SOON !!!')
            return redirect('/#contact')

    context = {'what_we_do': what_we_do,
               'moderators': moderators, 'form': form}
    return render(request, 'pages/index.html', context)


def about(request):
    video = About.objects.all()[:1]

    context = {'video': video}
    return render(request, 'pages/about.html', context)


def moderator(request, pk):
    moderator = Moderator.objects.order_by('-is_staff', 'created').get(id=pk)
    context = {'moderator': moderator}
    return render(request, 'pages/moderator-profile.html', context)
