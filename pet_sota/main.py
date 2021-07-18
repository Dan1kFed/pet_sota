from flask import Flask, request, render_template, abort, send_file
import os


app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route('/', methods=['GET', 'POST'])
def processor():
    if request.method == 'GET':
        return render_template('index.html')

    if request.method == 'POST':
        pass


if __name__ == '__main__':
    app.run(threaded=False, debug = True)