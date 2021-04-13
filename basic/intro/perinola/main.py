from controller import GameController
from flask import Flask, jsonify

app= Flask(__name__)
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'
app.config['CORS_HEADERS'] = 'Content-Type'



game = GameController.GamerController()

@app.route('/play')
def play():
    response = jsonify(game.play())
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/players')
def players():
    list=[]
    for i in game.get_players():
       list.append({'name':i.get_name(), 'money':i.get_money()})
    response = jsonify(list)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__=='__main__':
    app.run('0.0.0.0', 5000, debug=True)