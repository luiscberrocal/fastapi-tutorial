from typing import Optional

from fastapi import FastAPI, Depends, status, Response, HTTPException
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


@app.post('/blog/create', status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog(id, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} onot found')

    blog.update(request)  # noqa
    db.commit()
    return 'Updated'


@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(get_db)):  # noqa
    db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)  # noqa
    db.commit()
    return 'None'


@app.get('/blog')
def all_blogs(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@app.get('/blog/{id}', status_code=status.HTTP_200_OK)
def blog(id, response: Response, db: Session = Depends(get_db)):  # noqa
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()  # noqa
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} does not exist')
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail': f'Blog with id {id} does not exist'}
    return blog
