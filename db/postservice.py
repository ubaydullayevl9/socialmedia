from db import get_db
from db.models import UserPost


# 1. Добавление поста
def add_post_db(user_id, main_text):
    db = next(get_db())

    new_post = UserPost(user_id=user_id, main_text=main_text)
    db.add(new_post)
    db.commit()
    return True


# 2. Получение поста
def get_all_posts_db():
    db = next(get_db())

    return db.query(UserPost).all()


def get_exact_user_post_db(user_id):
    db = next(get_db())

    exact_user_posts = db.query(UserPost).filter_by(user_id=user_id).all()
    return exact_user_posts


def get_exact_post_db(post_id):
    db = next(get_db())

    exact_post = db.query(UserPost).filter_by(id=post_id).first()
    if exact_post:
        return exact_post
    return False


# 3. Изменение поста
def update_exact_post_db(post_id, new_text):
    db = next(get_db())

    exact_post = db.query(UserPost).filter_by(id=post_id).first()
    if exact_post:
        if new_text:
            exact_post.main_text = new_text
            db.commit()
            return True
    return False


# 4. Удаление
def delete_post_db(post_id):
    db = next(get_db())

    exact_post = db.query(UserPost).filter_by(id=post_id).first()
    if exact_post:
        db.delete(exact_post)
        db.commit()
        return True
    return False
