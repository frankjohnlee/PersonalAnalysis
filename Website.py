from AddToDB import app
from flask import render_template
from jinja2 import Template

FLASK_DEBUG=1
CLIENT_ID = '2285WZ'
CLIENT_SECRET = '8e0c01e96edd6f3dafe6ebf63cdf28b2'
FITBIT_API = 'https://www.fitbit.com/oauth2/authorize?' \
             'response_type=code&client_id={}&redirect_uri=http://localhost:8080/' \
             '&scope=activity%20nutrition%20heartrate%20location%20nutrition' \
             '%20profile%20settings%20sleep%20social%20weight'.format(CLIENT_ID)

@app.route('/')
def main_page():
    return render_template('index.html', site=FITBIT_API)




if __name__ == '__main__':
      app.run(host="localhost", port=80)