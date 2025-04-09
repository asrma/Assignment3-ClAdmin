from flask import Flask

app = Flask('app')


@app.route('/')
def hello_world():
    return 'Hello from Sharma ECS Container.'


app.run(host='0.0.0.0')
