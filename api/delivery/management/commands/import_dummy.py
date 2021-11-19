import json

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from delivery.models import Cuisine, Dinner, Restaurant


class Command(BaseCommand):
    help = 'Imports dummy data to database'

    def add_arguments(self, parser):
        parser.add_argument('--file', default=settings.DUMMY_FILE, help="dummy file path")

    def handle(self, *args, **options):
        data = self.load_data(path=options["file"])

    @staticmethod
    def load_data(path: str) -> dict:
        """Loads dummy data from given file path
        :rtype: dict
        """
        try:
            with open(path, "r") as f:
                return json.load(f)
        except FileNotFoundError as err:
            raise CommandError(err)
