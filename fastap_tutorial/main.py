from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get('/blog')
def index(limit=10, published: bool = False, sort: Optional[str] = None):
    if published:
        data = {'message': f'{limit} published blogs from db', 'name': 'kilo'}
    else:
        data = {'message': f'{limit} blogs from db', 'name': 'kilo'}
    return data


@app.get('/blog/unpublished')
def unpublished():
    data = {'message': 'All unpublished blogs', }
    return data


@app.get('/blog/{blog_id}')
def show(blog_id: int):
    data = {'message': 'About data', 'id': blog_id}
    return data


@app.get('/blog/{blog_id}/comments')
def comments(blog_id: int):
    data = {'message': ['Comment 1', ['Comment2']], 'id': blog_id}
    return data
