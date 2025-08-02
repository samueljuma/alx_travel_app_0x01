from django.core.management.base import BaseCommand
from alx_travel_app.listings.models import Listing
from django.contrib.auth import get_user_model
from faker import Faker
import random

User = get_user_model()
fake = Faker()

class Command(BaseCommand):
    help = 'Seed the database with sample listing data'

    def handle(self, *args, **kwargs):
        if not User.objects.exists():
            self.stdout.write(self.style.ERROR('No users found. Create at least one user first.'))
            return

        host = User.objects.first()  # Use first available user as host
        for _ in range(10):
            Listing.objects.create(
                title=fake.sentence(nb_words=4),
                description=fake.paragraph(),
                location=fake.city(),
                price_per_night=round(random.uniform(50, 500), 2),
                host=host,
            )
        self.stdout.write(self.style.SUCCESS('Sample listings created!'))
