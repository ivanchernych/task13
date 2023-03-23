from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1>Анкета претендента</h1>
                            <h2>на участие в миссии</h2>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="name" class="form-control" id="name" aria-describedby="emailHelp" placeholder="Введите фамилию" name="name">
                                    <input type="name" class="form-control" id="firstname" placeholder="Введите имя" name="firstname">
                                    <p> </p>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у вас образование?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Дошкольное</option>
                                          <option>Начальное общее</option>
                                          <option>Основное общее</option>
                                          <option>Среднее общее</option>
                                          <option>Высшее</option>
                                        </select>
                                    </div>
                                    <p> </p>
                                    <div class="form-group">
                                        <label for="form-check">Какие у Вас есть профессии?</label>
                                        <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="1" name="profession">
                                            <label class="form-check-label" for="acceptRules">Инженер-исследователь</label>
                                        </div>
                                        <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="2" name="profession">
                                            <label class="form-check-label" for="acceptRules">Инженер-строитель</label>
                                        </div>
                                        <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="3" name="profession">
                                            <label class="form-check-label" for="acceptRules">Пилот</label>
                                        </div>
                                         <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="4" name="profession">
                                            <label class="form-check-label" for="acceptRules">Метеоролог</label>
                                        </div>
                                         <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="5" name="profession">
                                            <label class="form-check-label" for="acceptRules">Инженер по жизнеобеспечению</label>
                                        </div>
                                         <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="6" name="profession">
                                            <label class="form-check-label" for="acceptRules">Инженер по радиационной защите</label>
                                        </div>
                                         <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="7" name="profession">
                                            <label class="form-check-label" for="acceptRules">Врач</label>
                                        </div>
                                         <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="8" name="profession">
                                            <label class="form-check-label" for="acceptRules">Экзобиолог</label>
                                        </div>
                                    <p> </p>
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    <p> </p>
                                    </div>
                                    <p> </p>
                                    <div class="form-group">
                                        <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <p> </p>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <p> </p>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    <p> </p>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
