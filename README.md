# URL Shortener

Simple URL Shortener web app built with Django.
Users enter a long URL and receive a shortened version (with a custom prefix), which redirects to the original link.
Short URLs are relative (e.g., /alejandro-abc123) and work in your local or production environment without a custom domain.
You can share the relative short URL with anyone using your app's base address.

## Features

- Shorten any valid URL to a custom short code (with prefix).
- Each short URL is unique and easy to share.
- Automatic redirection from the short URL to the original URL.
- User-friendly interface with modern styles.
- Customizable short code prefix (e.g., includes your name).
- Short URLs are relative (e.g., /alejandro-abc123) and can be shared by copying the link shown after shortening.

## How it works

1. Enter a long URL in the form.
2. Click "Shorten" to generate a short URL.
3. Copy the short URL (relative, e.g., /alejandro-abc123) and share it with others.
4. Anyone visiting the short URL will be redirected to the original address.

## Technologies Used

- Python 3
- Django 6
- HTML & CSS

## Getting Started

1. Clone the repository.
2. Install dependencies:
	```
	pip install -r requirements.txt
	```
3. Run migrations:
	```
	python manage.py migrate
	```
4. Start the development server:
	```
	python manage.py runserver
	```
5. Open your browser at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Deployment

You can deploy this project on platforms like Railway or PythonAnywhere.
For Railway:
1. Set up your `.env` file with production settings.
2. Configure static files (see settings.py for STATIC_ROOT and STATICFILES_STORAGE).
3. Use Gunicorn and WhiteNoise for production serving.
4. Short URLs remain relative; share them using your Railway app's base address.

## Author

Created by Alejandro Ramirez.

## License

This project is for educational purposes.
