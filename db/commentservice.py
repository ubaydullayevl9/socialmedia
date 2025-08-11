from db import get_db
from db.models import Comment


def add_comment_db(user_id, post_id, text):
    db = next(get_db())

    new_content = Comment(user_id=user_id, post_id=post_id, text=text)
    db.add(new_content)
    db.commit()
    return new_content


def get_exact_user_comment_db(user_id):
    db = next(get_db())
    exact_user_comment = db.query(Comment).filter_by(user_id=user_id).first()
    return exact_user_comment


def get_exact_post_comments_db(post_id):
    db = next(get_db())
    exact_user_comment = db.query(Comment).filter_by(user_id=post_id).first()
    return exact_user_comment


def update_comment_text_db(comment_id, new_text):
    db = next(get_db())
    exact_comment = db.query(Comment).filter_by(id=comment_id).first()
    if exact_comment:
        if new_text:
            exact_comment.text = new_text
            db.commit()
            return True
    return False


def delete_comment_db(comment_id):
    db = next(get_db())
    exact_comment = db.query(Comment).filter_by(id=comment_id).first()
    if exact_comment:
        db.delete(exact_comment)
        db.commit()
        return True
    return False


"""_id
1. Добавление коммента
2. Получение коммента по айди пользовтеля(вернет все)
3. Получение коммента по айди поста(вернет все)
4. Изменение коммента
5. Удаление коммента
"""