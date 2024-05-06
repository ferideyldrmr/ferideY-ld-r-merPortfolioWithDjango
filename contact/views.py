from django.http import JsonResponse
from django.core.mail import send_mail
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def contact_form(request):
    if request.method == 'POST':
        nameText = request.POST('name')
        emailText = request.POST('email')
        subjectText = request.POST('subject')
        messageText = request.POST('message')

        send_mail(
            subjectText,
            f"Name: {nameText}\nEmail: {emailText}\n\n{messageText}",  # E-posta gövdesi
            'your-email@example.com',  # Gönderen e-posta adresi
            ['feride_3441@outlook.com'],  # Alıcı e-posta adresi
            fail_silently=False,
        )

        context = {
            'success': True,
            'message': 'Contact form sent successfully.',
        }
        return render(request, 'index.html', {"message_name": nameText})
    else:
        context = {
            'success': False,
            'message': 'Invalid request method.',
        }

        return render(request, 'index.html', {})
