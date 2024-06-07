# FastAPI Project

This is a FastAPI project that includes user authentication and basic CRUD operations for posts.

## Installation Guide

This guide will help you set up and run the FastAPI project on your local machine.

### Prerequisites
Make sure you have the following installed on your system:

    Python 3.8+
    MySQL

### Step-by-Step Installation
Clone the Repository
````
git clone https://github.com/repo.git
cd your-repo
````

### Set Up a Virtual Environment
Create and activate a virtual environment to isolate the project's dependencies:

````
python3 -m venv venv
source venv/bin/activate
````

### Install Dependencies
Install the required dependencies using the requirements.txt file:
````
pip install -r requirements.txt
````


### Configure Environment Variables
Create a .env file in the project root directory to store environment variables. Add the following content:
````
DATABASE_URL=mysql+pymysql://root:root@127.0.0.1/lucidtask
SECRET_KEY=your_secret_key
ACCESS_TOKEN_EXPIRE_MINUTES=30
````
Replace root:root with your MySQL username and password, and your_secret_key with a strong secret key.


### Run Database Migrations
Create a .env file in the project root directory to store environment variables. Add the following content:
````
alembic upgrade head
````

### Run the application:
````
uvicorn app.main:app --reload
````


## API Endpoints Or you can check the postman collections.

## Signup
### Request
`GET /auth/signup`
````
curl -X POST "http://127.0.0.1:8000/auth/signup" \
-H "Content-Type: application/json" \
-d '{"email": "user@example.com", "password": "password123"}'
````
### Response
`Success`
```
{
  "id": 1,
  "email": "user@example.com"
}
```
`Error:`
```
{
  "detail": "Email already registered"
}
```

## Login
### Request
`GET /auth/signup`
````
curl -X POST "http://127.0.0.1:8000/auth/login" \
-H "Content-Type: application/json" \
-d '{"email": "user@example.com", "password": "password123"}'

````
### Response
`Success`
```
{
  "access_token": "your_access_token",
  "token_type": "bearer"
}
```
`Error:`
```
{
  "detail": "Invalid email or password"}
```

## AddPost
### Request
`GET /auth/addpost`
````
curl -X POST "http://127.0.0.1:8000/auth/addpost" \
-H "Content-Type: application/json" \
-H "Authorization: Bearer your_access_token" \
-d '{"text": "This is a new post"}'
````
### Response
`Success`
```
{
  "id": 1,
  "text": "This is a new post",
  "user_id": 1
}
```
`Error:`
```
{
  "detail": "Invalid token"
}
```
## GetPosts
### Request
`GET /auth/getposts`
````
curl -X GET "http://127.0.0.1:8000/auth/getposts" \
-H "Authorization: Bearer your_access_token"
````
### Response
`Success`
```
[
  {
    "id": 1,
    "text": "This is a new post",
    "user_id": 1
  }
]
```
`Error:`
```
{
  "detail": "Invalid token"
}
```

## DeletePost
### Request
`GET /auth/deletepost/{post_id}`
````
curl -X DELETE "http://127.0.0.1:8000/auth/deletepost/1" \
-H "Authorization: Bearer your_access_token"
````
### Response
`Success`
```
{
  "detail": "Post deleted"
}
```
`Error:`
```
{
  "detail": "Invalid token"
}
```

