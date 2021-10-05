from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    data = {'message': 'Hello', 'name': 'kilo'}
    return data


@app.get('/about')
def about():
    data = {'message': 'About data', 'name': 'about'}
    return data
