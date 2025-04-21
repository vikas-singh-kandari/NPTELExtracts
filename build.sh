#!/usr/bin/env bash
set -o errexit  # Exit on any error

# Install all Python dependencies
pip install -r requirements.txt

# Collect static files (for production)
python manage.py collectstatic --no-input

# Apply database migrations
python manage.py migrate

# Optional: Create superuser if env variable is set
if [ "$CREATE_SUPERUSER" = "True" ]; then
  python manage.py createsuperuser --no-input \
    --username "$DJANGO_SUPERUSER_USERNAME" \
    --email "$DJANGO_SUPERUSER_EMAIL"
fi
