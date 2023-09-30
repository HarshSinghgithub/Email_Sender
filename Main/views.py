from django.shortcuts import render, HttpResponse
from .form import EmailForm 
from django.core.mail import send_mail, BadHeaderError

# def SendEmail(request):
#     messageSent = False

#     if request.method == 'POST':
#         form = EmailForm(request.POST)

#         if form.is_valid():
#             subject = form.cleaned_data['subject']
#             sender = form.cleaned_data['sender_mail_id']
#             receiver = form.cleaned_data['receiver_mail_id']
#             message = form.cleaned_data['message']

#             try:
#                 send_mail(subject, message, sender, [receiver])
#                 messageSent = True
#             except BadHeaderError:
#                 return HttpResponse("Invalid header found.")

#     else:
#         form = EmailForm()

#     context = {
#         'form': form,
#         'messageSent': messageSent
#     }

#     return render(request, "index.html", context)


def SendEmail(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)

        if form.is_valid():
            subject = form.cleaned_data['subject']
            sender = form.cleaned_data['sender_mail_id']
            receiver = form.cleaned_data['receiver_mail_id']
            message = form.cleaned_data['message']

            try:
                send_mail(subject, message, sender, [receiver])
                return render(request, 'index.html', {'form': form, 'message_sent': True})
            except BadHeaderError:
                return HttpResponse("Invalid header found. Email not sent.")

        else:
            # Form data is not valid, display form with errors
            return render(request, 'index.html', {'form': form, 'message_sent': False})
    else:
        # Handle GET request logic here if needed
        form = EmailForm()
        return render(request, 'index.html', {'form': form, 'message_sent': None})

