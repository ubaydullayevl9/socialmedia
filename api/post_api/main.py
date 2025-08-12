from fastapi import APIRouter
from typing import List
from api.post_api.schemas import UserPostCreate, UserPostUpdate, UserPostRead
from db.postservice import add_post_db, get_all_posts_db, get_exact_post_db, update_exact_post_db, delete_post_db, \
    get_exact_user_post_db

post_router = APIRouter(prefix="/post", tags=["Post API"])


@post_router.post("/create_post", response_model=bool)
async def create_post_api(post:UserPostCreate):
    return add_post_db(post.user_id, post.main_text)

@post_router.get("/get_all_post", response_model=List[UserPostRead])
async def get_all_post_api():
    return get_all_posts_db()

@post_router.get("/get_exact_post{post_id}", response_model=UserPostRead)
async def get_exact_post_api(post_id: int):
    return get_exact_post_db(post_id)

@post_router.get("/get_all_user_post{user_id}", response_model=List[UserPostRead])
async def get_all_user_post_api(user_id: int):
    return get_exact_user_post_db(user_id)

@post_router.put("/update_post/{post_id}", response_model=bool)
async def update_post_api(post_id: int, post: UserPostUpdate):
    return update_exact_post_db(post_id, post.main_text)

@post_router.delete("/delete_post/{post_id}", response_model=bool)
async def delete_post_api(post_id: int):
    return delete_post_db(post_id)

