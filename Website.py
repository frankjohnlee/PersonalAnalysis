from AddToDB import app
from flask import render_template, request, url_for
from GetInfoFromFitBit import authenticate_fitbit
from api_utils import API_DICT, OAUTH_SESSIONS


SERVER_HOST = "localhost"
SERVER_PORT = 80


@app.route('/')
def main_page():
    return render_template('index.html')


@app.route('/index.html')
def main_page2():
    return render_template('index.html')


@app.route('/AccManager.html', methods=['GET'])
def acc_manage():
    if "code" in request.url:
        authenticate_fitbit(request.url, OAUTH_SESSIONS['fitbit'])
    return render_template('AccManager.html', sites=API_DICT)


@app.route('/tables.html')
def tables():
    return render_template('tables.html')


if __name__ == '__main__':
    #context = ('C:\\Users\\mattc\\.ssh\\.ssh.crt','C:\\Users\\mattc\\.ssh\\.ssh.key')

    app.run(host=SERVER_HOST,
            port=SERVER_PORT)