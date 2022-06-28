from flask import Flask
from mongoengine import connect

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

connect('my_db', username='db_username', password='db_password', authentication_source='admin')


@app.route('/hello', methods=['GET'])
def test():
    return 'Hello', 200
