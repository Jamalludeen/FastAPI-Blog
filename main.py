from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

posts: list[dict] = [
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

@app.get("/", include_in_schema=False)
@app.get("/posts", include_in_schema=False)
def home(request: Request):
    return templates.TemplateResponse(request, "home.html", {"posts": posts})



@app.get("/api/posts")
def get_posts():
    return posts



