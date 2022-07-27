import email
from django.shortcuts import render, redirect
from contacts.forms import ContactForm
from django.contrib import messages

# Create your views here.


def contact_us(request):

    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.name = contact.name.title()
            contact.save()
            messages.success(
                request, 'THANK YOU FOR CONTACTING US! WE WILL SOON GET IN TOUCH')
            return redirect('contact-us')

    context = {'form': form}
    return render(request, 'contacts/contact.html', context)
