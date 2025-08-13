from fastapi import FastAPI, Request

from db import Base, engine
from api.photo_api.main import photo_router
from api.user_api.main import user_router
from api.post_api.main import post_router
from api.comment_api.main import comment_router
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from db.postservice import get_all_posts_db, get_exact_post_db
from db.userservice import get_all_or_exact_user_db

templates = Jinja2Templates(directory="templates")


app = FastAPI(docs_url="/docs")

Base.metadata.create_all(engine)

app.include_router(photo_router)
app.include_router(user_router)
app.include_router(post_router)
app.include_router(comment_router)


@app.get('/', response_class=HTMLResponse)
async def main(request: Request):
    all_posts = get_all_posts_db()
    #all_posts_users = []
    #for post in all_posts:
    #    user = get_all_or_exact_user_db(post.user_id)
    #    if user:
    #        all_posts_users.append({"post": post, "user": user})
    #        print( all_posts_users)
#
    #return templates.TemplateResponse(request=request, name="index.html", context={"posts": all_posts_users})

@app.get("/{post_id}", response_class=HTMLResponse)
async def exact_product_html(request: Request, post_id: int):
    exact_post = get_exact_post_db(post_id)
    return templates.TemplateResponse(request, name="exact_post.html", context={"post": all})
