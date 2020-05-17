from django.shortcuts import render , redirect
from .forms import ContactForm
from django.conf import settings
from .models import ContactDetails
from django.core.mail import  BadHeaderError
from django.core.mail import send_mail as sm
from django.http import HttpResponse , HttpResponseRedirect




def send_mail(request):
    contactdetails = ContactDetails.objects.last()
    template = 'contact.html'

    if request.method == 'POST' : 
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            subject = contact_form.cleaned_data['subject']
            from_email = contact_form.cleaned_data['from_email']
            message = contact_form.cleaned_data['message']
            #trying to send the mail which will contain the following fields
            try : 
                sm(subject , message ,from_email , ['test@gmail.com'] )
            
            except BadHeaderError : 
                return HttpResponse('ivalid header')

            return redirect('contact:success')

    else:
        contact_form = ContactForm()


    context = {
        'contactdetails' : contactdetails  , 
        'contact_form' : contact_form
    }

    return render(request, template , context)


def success(request):
    return HttpResponse('Message Sent Successfully')