from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    data = {'message': 'Hello', 'name': 'kilo'}
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
