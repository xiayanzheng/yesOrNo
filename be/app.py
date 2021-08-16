from flask import Flask
from flask import jsonify, request
from engine.dp import dataProcess
from flask_cors import CORS
import os

app = Flask(__name__, static_url_path='')
CORS(app)

dbconfig = {
    "dbhost": os.environ.get('dbhost', '127.0.0.2'),
    "dbport": os.environ.get('dbport', '3306'),
    "dbuser": os.environ.get('dbuser', 'root'),
    "dbpass": os.environ.get('dbpass', 'lf'),
    "dbname": os.environ.get('dbname', 'yesorno')
}
print(dbconfig)

dp = dataProcess()
try:
    dp.db(**dbconfig)
except:
    pass


@app.route('/', methods=['GET', 'POST'])
def index():
    return app.send_static_file('index.html')


@app.route('/api/answer', methods=['GET', 'POST'])
def yesOrNo():
    answer = request.args.get('answer', '404')
    qid = request.args.get('qid', '404')
    print(answer, qid)
    dp.pro(qid, answer)
    return jsonify({"val": True})


def run():
    if __name__ == '__main__':
        app.run(host='0.0.0.0', debug=True)


run()
