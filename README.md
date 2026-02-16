# URL Shortener

This is a simple URL Shortener web application built with Django.
It allows users to enter a long URL and receive a shortened version, which redirects to the original link.

## Features

- Shorten any valid URL to a custom short code.
- Each short URL is unique and easy to share.
- Automatic redirection from the short URL to the original URL.
- User-friendly interface with modern styles.
- Customizable short code prefix (e.g., includes your name).

## How it works

1. Enter a long URL in the form.
2. Click "Shorten" to generate a short URL.
3. Use the short URL to be redirected to the original address.

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

You can deploy this project on platforms like PythonAnywhere.
Remember to set up your `.env` file and configure static files for production.

## Author

Created by Alejandro Ramirez.

## License

This project is for educational purposes.
