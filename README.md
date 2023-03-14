# Trade-Hub puddle

## Overview

Trade Hub is an online marketplace built using the Django web framework. It allows users to buy and sell items using a secure and user-friendly interface. [Watch the video](https://youtu.be/qPswfarsK6w)

## Features

1. User registration and authentication
2. Product listings with images and descriptions
3. Product search and filtering
4. Secure payment processing (Comming Soon).

## Installation

This is not for production. To run Trade Hub on your local machine, follow these steps:

1. Clone the repository:
```shell
git clone <--clone this project-->
```

2. Create a virtual environment and install dependencies:
```shell
cd trade-hub
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

3. Set up the database:
```shell
python manage.py migrate
python manage.py createsuperuser
python manage.py loaddata fixtures/products.json
```

4. Start the development server:
```shell
python manage.py runserver
```

5. Visit http://localhost:8080 or url shown on Terminal in your web browser to access Trade Hub.

# Contributing
If you would like to contribute to Trade Hub, please read our contributing guidelines(coming soon) and submit a pull request.

# License

Trade Hub is licensed under the MIT License.
