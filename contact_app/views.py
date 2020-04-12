from django.shortcuts import render, redirect
from django.contrib import messages
from .models import contactForm
# Create your views here.
def contact(request):
    if request.method == 'POST':
      first_name = request.POST['firstname'] 
      last_name = request.POST['lastname']
      email = request.POST['email']
      subject = request.POST['subject']
      chat = request.POST['message']
      
      if (first_name == '') or (last_name == '') or (email == '') or (subject == '') or (chat == '') :
          messages.error(request, 'One or more field is empty!')
          return redirect('contact')
      else:
            newContact = contactForm()
            newContact.firstName = first_name
            newContact.lastName = last_name
            newContact.email = email
            newContact.subject = subject
            newContact.message = chat
            newContact.save()
            messages.success(request, 'Your Feedback Has been Received')
            return redirect('contact')
    else:
        return render(request, 'contact.html')