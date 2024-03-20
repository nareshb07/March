# send_email_script.py
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "whatsapp_clone.settings")

import django
django.setup()



from django.core.mail import send_mail

send_mail(
    'Subject here',
    'Here is the message.',
    'mindsetmatters30@gmail.com',
    ['k.nareshb077@gmail.com'],
    fail_silently=False,
)



