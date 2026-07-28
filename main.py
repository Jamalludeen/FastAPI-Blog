from fastapi import FastAPI

app = FastAPI()

posts = [
    {
        "id": 1,
        "author": "James Bond",
        "title": "FastAPI is Awesome",
        "content": "This is a framework for building APIs",
        "date_posted": "2025 01 17",
    },
    {
        "id": 2,
        "author": "John Doe",
        "title": "Python is Great for backend",
        "content": "Python is a programming language.",
        "date_posted": "2023 09 22",
    }
]

@app.get("/")
def home():
    return {"message": "Hello World!"}


@app.get("/api/posts")
def get_posts():
    return posts

