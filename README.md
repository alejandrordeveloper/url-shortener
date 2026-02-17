
# URL Shortener

This is a Django-based URL Shortener web application. Users can enter a long URL and receive a unique, short link using your custom DNS (e.g., `yourname.dpdns.org/abc123`). The app provides a modern interface and a convenient copy button for sharing the generated short URL.

**Important:**
- For production, you must use a custom DNS with your name (e.g., `alejandrodev.dpdns.org`). This ensures your short links are unique, professional, and always accessible. Do not use localhost for sharing links.

## Project Overview

This project allows users to:
- Submit any valid URL via a simple form.
- Receive a unique, short code (e.g., `/abc123`) that redirects to the original URL.
- Instantly copy the full short link (including your DNS) with a single click.
- Share the short link with anyone; the link will always redirect to the original destination as long as your DNS is active.

The backend is built with Django 6, using a single model to store the original URL and its corresponding short code. The frontend is styled for clarity and ease of use, and includes a copy-to-clipboard button for user convenience.

## Features

- Custom DNS-based short links (e.g., `yourname.dpdns.org/abc123`).
- Unique, random short codes for every URL.
- Automatic redirection from the short link to the original URL.
- Modern, user-friendly interface with responsive design.
- One-click copy button for easy sharing.

## How it works

1. Enter a long URL in the input form.
2. Click the "Shorten" button.
3. The app generates a unique short code and displays the full short link using your DNS (e.g., `https://alejandrodev.dpdns.org/abc123`).
4. Click the "Copy" button to copy the link to your clipboard.
5. Share the link with anyone; when visited, it will redirect to the original URL.

## Technologies Used

- Python 3
- Django 6
- HTML & CSS

## Getting Started

1. Clone this repository.
2. Install dependencies:
	```
	pip install -r requirements.txt
	```
3. Set up your `.env` file with your custom DNS (e.g., `alejandrodev.dpdns.org`) in `ALLOWED_HOSTS` and your production settings.
4. Run migrations:
	```
	python manage.py migrate
	```
5. Collect static files:
	```
	python manage.py collectstatic
	```
6. Deploy to your production server (e.g., Railway, PythonAnywhere) and point your DNS to the deployed app.
7. Access your app at `https://yourname.dpdns.org/` and start shortening URLs.

## Deployment

You can deploy this project on platforms like Railway or PythonAnywhere.

**Recommended for production:**
- Use a custom DNS (e.g., `alejandrodev.dpdns.org`) and set it in your `.env` as `ALLOWED_HOSTS`.
- Configure static files as shown in `settings.py` (`STATIC_ROOT`, `STATICFILES_STORAGE`).
- Use Gunicorn and WhiteNoise for serving in production.
- Make sure your DNS points to your deployed app for public access.

## Author

Created by Alejandro Ramirez.

## License

This project is for educational purposes.
