"""
ASGI config for whatsapp_clone project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""



from django.core.asgi import get_asgi_application

from django.urls import path

from channels.routing import ProtocolTypeRouter, URLRouter

from channels.auth import AuthMiddlewareStack



import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'whatsapp_clone.settings')

django.setup()

from chats.consumers import PersonalChatConsumer 


application = get_asgi_application()


application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter([
            path('ws/<int:id>/', PersonalChatConsumer.as_asgi()),
        ])
    )
})
