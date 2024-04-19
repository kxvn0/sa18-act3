from django.core.management.base import BaseCommand
from products.models import Product

class Command(BaseCommand):
    help = 'Populate products in the database'

    def handle(self, *args, **kwargs):
        # Create and save products
        Product.objects.create(name='Doritos', price=2.99, description='A medium size bag of Doritos Chips')
        Product.objects.create(name='Sprite', price=1.49, description='A medium size bottle of Sprite with 240 Calories.')
        Product.objects.create(name='Pack of Water', price=8.99, description='A 12 pack of the finest water.')

        self.stdout.write(self.style.SUCCESS('Products added successfully'))
