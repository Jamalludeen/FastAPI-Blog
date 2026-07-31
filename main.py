from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
# /static is the url, and second parameter is the instance of StatifFiles that points to
app.mount("/static", StaticFiles(directory="static"), name="static")

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

@app.get("/", include_in_schema=False, name="home")
@app.get("/posts", include_in_schema=False, name="posts")
def home(request: Request):
    return templates.TemplateResponse(request, "home.html", {"posts": posts, "title": "Project"})



@app.get("/api/posts")
def get_posts():
    return posts

@app.get("/api/posts/{post_id}")
def get_post(post_id: int):
    for post in posts:
        if post.get("id") == post_id:
            return post
    return {"error": "Post not found"}


