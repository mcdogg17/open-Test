from flask import Flask, render_template, request
from flask_socketio import SocketIO
import toxicity_test

app = Flask(__name__)
app.config['SECRET_KEY'] = 'openBank'
socketio = SocketIO(app)


def transformation(tor):
    return [round(elem.item() * 100, 2) for elem in tor]


@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('test_toxic.html')


@app.route('/toxicity', methods=['POST'])
def toxic_unit():
    tmp = transformation(toxicity_test.predict(request.json['text'])[0])
    return {
        "neutral": tmp[0],
        "positive": tmp[1],
        "negative": tmp[2]
    }


@socketio.on("run_test")
def run_test(text):
    if text:
        tmp = transformation(toxicity_test.predict(text)[0])

        socketio.emit("send_result", tmp)
    else:
        socketio.emit("send_result", [0, 0, 0])


if __name__ == '__main__':
    socketio.run(app, host='127.0.0.1', port=80, allow_unsafe_werkzeug=True)
