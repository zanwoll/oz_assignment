from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, This is Main Page!"

# Alt + Shift + 화살표 위/아래 ( 위치에 복사 )
@app.route("/about")
def about():
    return "Hello, This is About Page!"

@app.route("/company")
def company():
    return "Hello, This is Company Page!"

# 동적으로 URL 파라미터 값을 받아서 처리해준다.
@app.route("/user/<username>")
def user_profile(username):
    return f'UserName : {username}'

@app.route("/number/<int:number>")
def number(number):
    return f'Number : {number}'

import requests
@app.route("/test")
def test():
    url = 'http://127.0.0.1:5000/submit'
    data = 'test data'
    requests.post(url=url, data=data)

    return Response

@app.route('/submit', methods=['GET', 'POST', 'PUT', 'DELETE'])
def submit():
    print(request.method)

    if request.method == 'GET':
        print("GET Method")

    if request.method == 'POST':
        print("***POST Method***", request.data)
    return Response("Successfully submitted", status=200)

if __name__ == "__main__":
    app.run()