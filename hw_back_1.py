#1 task ping-pong
def application(environ, start_response):
    path = environ.get('PATH_INFO', '')
    method = environ.get('REQUEST_METHOD', '')
    
    if method == 'GET' and path == '/ping':
        status = '200 OK'
        headers = [('Content-Type', 'text/plain')]
        start_response(status, headers)
        return [b'pong']
    else:
        status = '404 Not Found'
        headers = [('Content-Type', 'text/plain')]
        start_response(status, headers)
        return [b'Not Found']


#2 task request info
import json

def application(environ, start_response):
    path = environ.get('PATH_INFO', '')
    method = environ.get('REQUEST_METHOD', '')
    
    if method == 'GET' and path == '/info':
        # Собираем информацию о запросе
        info = {
            'method': method,
            'url': path,
            'protocol': environ.get('SERVER_PROTOCOL', ''),
            'query_string': environ.get('QUERY_STRING', ''),
            'headers': {
                'user_agent': environ.get('HTTP_USER_AGENT', ''),
                'host': environ.get('HTTP_HOST', '')
            }
        }
        
        # Превращаем в JSON
        response_body = json.dumps(info, indent=2).encode('utf-8')
        
        status = '200 OK'
        headers = [('Content-Type', 'application/json')]
        start_response(status, headers)
        return [response_body]
    else:
        status = '404 Not Found'
        headers = [('Content-Type', 'text/plain')]
        start_response(status, headers)
        return [b'Not Found']



#3 task hello
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def hello():
    return {"message": "Hello, nfactorial!"}



#4 task meaning life
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def hello():
    return {"message": "Hello, nfactorial!"}

@app.post('/meaning-of-life')
def meaning_of_life():
    return {"meaning": "42"}



#5 task nfactor 
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def hello():
    return {"message": "Hello, nfactorial!"}

@app.post('/meaning-of-life')
def meaning_of_life():
    return {"meaning": "42"}

@app.get('/{num}')
def factorial(num: int):
    # Вычисляем факториал
    result = 1
    for i in range(2, num + 1):
        result *= i
    return {"nfactorial": result}
