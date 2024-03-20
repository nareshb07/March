from django.core.mail import send_mail
from django.conf import settings 
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_forget_password_mail(email , token ):
    subject = 'Your forget password link'
    message = f'Hi , click on the link to reset your password http://127.0.0.1:8000/chats/change-password/{token}/'
    email_from = settings.EMAIL_SENDER_MAIL
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)
    return True

from django.core.mail import EmailMultiAlternatives

def send_PaymentSuccess_mail_to_Follower(email, order):
    try:
        subject = 'Payment Successful'
        html_message = render_to_string('follower_payment_success.html',{"Order_obj":order})
        plain_message = strip_tags(html_message)
        email_from = settings.EMAIL_SENDER_MAIL
        recipient_list = [email]
        msg = EmailMultiAlternatives(subject, plain_message, email_from, recipient_list)
        msg.attach_alternative(html_message, "text/html")
        msg.send()
        return True
    except Exception as e:
        print(e)
        return False




def send_PaymentSuccess_mail_to_Creator(email, order):
    try:
        subject = 'Payment Successful'
        html_message = render_to_string('creator_payment_success.html',{"Order_obj":order})
        plain_message = strip_tags(html_message)
        email_from = settings.EMAIL_SENDER_MAIL
        recipient_list = [email]

        msg = EmailMultiAlternatives(subject, plain_message, email_from, recipient_list)
        msg.attach_alternative(html_message, "text/html")
        msg.send()

        # send_mail(subject,plain_message,  email_from, recipient_list, html_message=message)
        return True
    except Exception as e:
        print(e)
        return False

    