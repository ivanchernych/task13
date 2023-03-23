from flask import Flask, url_for, request
from werkzeug.utils import secure_filename
import os
from io import BytesIO
from PIL import Image

app = Flask(__name__)

photo_file = "static/img/photo.jpg"


@app.route('/')
@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <h1>Результат отбора</h1>
                        <h2>Претендент на участие в миссии {nickname}:</h2>
                        <div class="alert alert-success" role="alert">
                          Поздравляем! ваш рейтинг после {level} этапа отбора
                        </div>
                        <p> составляет {rating}!</p>
                        <div class="alert alert-warning" role="alert">
                         Желаем удачи!
                      </body>
                    </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
