from django.core.management.base import BaseCommand
from django.utils.text import slugify
from store.models import Category, Product

SAMPLE_PRODUCTS = [
    ("Laptops", "ZenBook Pro 14 OLED", 64999, 7, 4.7, "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?auto=format&fit=crop&w=1200&q=80"),
    ("Laptops", "ThinkPad X1 Carbon", 79999, 5, 4.8, "https://images.unsplash.com/photo-1515879218367-8466d910aaa4?auto=format&fit=crop&w=1200&q=80"),
    ("Phones", "Pixel 9 Pro", 49999, 12, 4.6, "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?auto=format&fit=crop&w=1200&q=80"),
    ("Phones", "iPhone 16", 69999, 9, 4.7, "https://images.unsplash.com/photo-1510557880182-3d4d3cba35a5?auto=format&fit=crop&w=1200&q=80"),
    ("Audio", "Noise Cancelling Headphones", 8999, 15, 4.5, "https://images.unsplash.com/photo-1519677100203-a0e668c92439?auto=format&fit=crop&w=1200&q=80"),
    ("Accessories", "Mechanical Keyboard", 3999, 25, 4.4, "https://images.unsplash.com/photo-1527814050087-3793815479db?auto=format&fit=crop&w=1200&q=80"),
    ("Accessories", "Gaming Mouse", 1799, 40, 4.3, "https://images.unsplash.com/photo-1613141411244-0e4ac259d217?auto=format&fit=crop&w=1200&q=80"),
    ("Monitors", "27-inch 144Hz Monitor", 12999, 10, 4.5, "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?auto=format&fit=crop&w=1200&q=80"),
]

class Command(BaseCommand):
    help = "Seed the database with sample categories and products."

    def handle(self, *args, **options):
        created_products = 0
        for cat_name, name, price, stock, rating, img in SAMPLE_PRODUCTS:
            cat, _ = Category.objects.get_or_create(
                name=cat_name,
                defaults={"slug": slugify(cat_name)},
            )
            slug = slugify(name)
            obj, created = Product.objects.get_or_create(
                slug=slug,
                defaults={
                    "category": cat,
                    "name": name,
                    "description": f"{name} — premium tech product. Demo description for your capstone.",
                    "price": price,
                    "stock": stock,
                    "rating": rating,
                    "image_url": img,
                }
            )
            if created:
                created_products += 1

        self.stdout.write(self.style.SUCCESS(f"Seed complete ✅ Added {created_products} new products."))
