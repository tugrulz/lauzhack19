from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request
from flask import url_for
import random

scores_file = '/Users/elmas/PycharmProjects/lauzhack19/scores.txt'
app = Flask(__name__, static_url_path='/static')

longnames = ['John Jacob Jingle Heimer Schmidt', 'Man with The Longest Name', 'No Buffer Overflow for Old Men', 'Get A Shorter Name Bitch']
randomnames = ['Mec Chelou', "John Doe", "Mario Rossi", 'Gimli Gloinsson', 'Frodo Baggins', 'Cristiano Ronaldo']

@app.route('/')
@app.route('/<username>')
def hello_world(username=""):
    if(len(username) > 50):
        username = random.choice(longnames)

    if(username == ""):
        username = random.choice(randomnames)

    print(username)
    with open(scores_file, 'a') as f:
        f.write("%s," % (username))

    return render_template('index.html')

def update_scoreboard():
    with open(scores_file) as f:
        liste = f.read().splitlines()

    scores = []
    for line in liste:
        splitted = line.split(',')
        name = splitted[0]
        score = splitted[1]
        scores.append((name, score))

    scores = sorted(scores, key=lambda x: x[1])
    print(scores)
    if (len(scores) > 10):
        scores = scores[0:9] + [scores[-1]]

    print(scores)
    with open(scores_file, 'w') as f:
        for score in scores:
            print(score)
            f.write(score[0] + "," + score[1] + "\n")

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

    with open(scores_file, 'a') as f:
        print((str(score).split('.')[0]))
        f.write("%s\n" % (str(score).split('.')[0]))

    return jsonify(status="success", data=data)

@app.route('/scores/')
def hello():
    # with open('scores.txt', 'a') as f:
    #     f.write("%s" % name_and_score)

    liste = {}
    update_scoreboard()
    with open(scores_file, 'r') as f:
        for line in f:
            line = line.strip()
            splitted = line.split(',')
            liste[splitted[0]] = splitted[1]

    return render_template('scores.html', liste = liste)


if __name__ == '__main__':
    app.run("0.0.0.0")
