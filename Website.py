from AddToDB import app
from flask import render_template, request, url_for
from GetInfoFromFitBit import authenticate_fitbit


SERVER_HOST = "127.0.0.1"#SERVER_HOST = ""localhost""
SERVER_PORT = 80
CLIENT_ID = '2285WZ'
CLIENT_SECRET = '8e0c01e96edd6f3dafe6ebf63cdf28b2'
REDIRECT='http://localhost/AccManager.html'
API_DICT = {'fitbit':'https://www.fitbit.com/oauth2/authorize?response_type=code&client_id={0}&redirect_uri={1}&scope=activity%20nutrition%20heartrate%20location%20nutrition%20profile%20settings%20sleep%20social%20weight'.format(CLIENT_ID, REDIRECT)
            }


@app.route('/')
def main_page():
    return render_template('index.html')


@app.route('/index.html')
def main_page2():
    return render_template('index.html')


@app.route('/AccManager.html', methods=['GET'])
def acc_manage():
    ##authenticate_fitbit(request.args)
    return render_template('AccManager.html', sites=API_DICT)


@app.route('/tables.html')
def tables():
    return render_template('tables.html')


if __name__ == '__main__':
      app.run(host=SERVER_HOST, port=SERVER_PORT)