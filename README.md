# TechShop API (Django + DRF)

A small e-commerce backend API for electronics/tech products.

## Features
- Categories + Products
- Product search, sorting, and filters
- Create Orders (with order items, totals, stock reduction)
- CORS ready for React dev server

## Setup

```bash
cd backend
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py seed
python manage.py createsuperuser
python manage.py runserver
```

API base: `http://127.0.0.1:8000/api`

## Endpoints
- GET `/api/health/`
- GET `/api/categories/`
- GET `/api/products/?search=mouse&ordering=price&category=phones&in_stock=true&min_price=1000&max_price=50000`
- GET `/api/products/<id>/`
- POST `/api/orders/`
- GET `/api/orders/<id>/`

### Create Order payload (example)
```json
{
  "full_name": "Ashraf Ahmed",
  "email": "ashraf@example.com",
  "phone": "01000000000",
  "address_line1": "12 Example St",
  "address_line2": "",
  "city": "Alexandria",
  "country": "Egypt",
  "postal_code": "21500",
  "items": [
    {"product_id": 1, "quantity": 2},
    {"product_id": 3, "quantity": 1}
  ]
}
```

Shipping rule (demo): free shipping over 2000 EGP, else 75 EGP.
