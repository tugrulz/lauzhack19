from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request
from flask import url_for

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def hello_world():
    return render_template('index.html')

# @app.route('/index')
# def hello_world():
#     return 'Hello World!'

@app.route('/_get_post_json/', methods=['POST'])
def get_post_json():
    data = request.get_json()
    print(data)
    name = data['name']
    score = data['playerMoney']
    print((name, score))

    with open('/Users/elmas/PycharmProjects/lauzhack19/scores.txt', 'a') as f:
        f.write("%s,%s\n" % (name, str(score).split('.')[0]))

    return jsonify(status="success", data=data)

@app.route('/scores/')
@app.route('/scores/<name_and_score>')
def hello(name_and_score=""):
    # with open('scores.txt', 'a') as f:
    #     f.write("%s" % name_and_score)

    import os
    print(os.listdir('./.'))
    with open('/Users/elmas/PycharmProjects/lauzhack19/scores.txt', 'r') as f:
        liste = f.readlines()

    return render_template('scores.html', liste = liste)


if __name__ == '__main__':
    app.run()
