from typing import Optional

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from . import models, schemas
from .database import engine, SessionLocal
from .models import Blog

app = FastAPI()

models.Base.metadata.create_all(engine)


# @app.get('/blog')
# def index(limit=10, published: bool = False, sort: Optional[str] = None):
#    if published:
#        data = {'message': f'{limit} published blogs from db', 'name': 'kilo'}
#    else:
#        data = {'message': f'{limit} blogs from db', 'name': 'kilo'}
#    return data
#
#
# @app.get('/blog/unpublished')
# def unpublished():
#    data = {'message': 'All unpublished blogs', }
#    return data
#
#
# @app.get('/blog/{blog_id}')
# def show(blog_id: int):
#    data = {'message': 'About data', 'id': blog_id}
#    return data
#
#
# @app.get('/blog/{blog_id}/comments')
# def comments(blog_id: int):
#    data = {'message': ['Comment 1', ['Comment2']], 'id': blog_id}
#    return data
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/blog/create')
def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
