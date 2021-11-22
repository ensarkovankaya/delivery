import time
from django.core.management.base import BaseCommand

from utils.redis import pub_sub


class Command(BaseCommand):
    help = 'Listen pub sub messages and executes consumers'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Listening messages...'))
        for message in pub_sub.listen():
            if message:
                self.stdout.write(self.style.SUCCESS(f'Message received: {message}'))
