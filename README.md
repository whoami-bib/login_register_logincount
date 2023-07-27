
# Django Rest Framework Application - User Registration and Login API

This is a Django Rest Framework application that provides API endpoints for user registration, user login, and access to user login counts. The application uses JWT authentication for secure access to the endpoints.
## Getting started

To use this repository, you need to follow the steps below:

### Clone the repository

clone this repository to your local machine using the URL:

`git clone https://github.com/your-username/login_register_logincount.git
`
### Install Dependencies
Navigate to the project directory and install the required dependencies using pip:

`cd login_register_logincount`

`cd pixelboho`

`pip install -r requirements.txt`

### Database Setup
Make sure you have set up your database. By default, this application uses the SQLite database. Run the following commands to create the database and apply migrations:

`python manage.py migrate`

### Run the application

Start the development server to run the application

`python manage.py runserver`

## API Endpoints
### 1.User Registration:
Endpoint: http://localhost:8000/api/register/

-Method: POST

Body:

`{
    "email": "jomy@12.com",
    "password": "amal@12",
    "is_admin": "True"  // Optional for registering an admin user
}`

### 2. User Login:

Endpoint: http://localhost:8000/api/login/

method : POST

Body:

`{
    "email": "jomy@12.com",
    "password": "amal@12"
}
`

### 3. Home Page:

Endpoint: http://localhost:8000/api/home/

Method : GET

Authorization: Bearer YOUR_ACCESS_TOKEN

### 4. user Login Count:

Endpoint: http://localhost:8000/api/login-count/

Method : GET

Authorization: Bearer YOUR_ACCESS_TOKEN





