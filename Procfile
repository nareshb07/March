web: gunicorn --bind :8000 --workers 3 --threads 2 whatsapp_clone.wsgi:application
websocket: daphne -b :: -p 5000 whatsapp_clone.asgi:application