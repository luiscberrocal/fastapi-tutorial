from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    data = {'message': 'Hello', 'name': 'kilo'}
    return data
