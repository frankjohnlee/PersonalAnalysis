import fitbit
import urllib
import base64

CLIENT_ID = '2285WZ'
CLIENT_SECRET = '8e0c01e96edd6f3dafe6ebf63cdf28b2'
REDIRECT='http://localhost/AccManager.html'
GRANT_TYPE = 'authorization_code'

#  This is the Fitbit URL
TOKEN_URL = "https://api.fitbit.com/oauth2/token"

def authenticate_fitbit(code):
    print('got here')

    # Form the data payload
    BodyText = {'code': code,
                'redirect_uri': REDIRECT,
                'client_id': CLIENT_ID,
                'grant_type': GRANT_TYPE}

    BodyURLEncoded = urllib.parse.urlencode(BodyText)

    #  Start the request
    req = urllib.request.Request(TOKEN_URL, BodyURLEncoded)

    #  Add the headers, first we base64 encode the client id and client secret with a : in between
    # and create the authorisation header
    req.add_header('Authorization', 'Basic ' + base64.b64encode(CLIENT_ID + ":" + CLIENT_SECRET))
    req.add_header('Content-Type', 'application/x-www-form-urlencoded')

    # Fire off the request
    try:
        response = urllib.urlopen(req)
        FullResponse = response.read()
        print(FullResponse)

    except urllib.URLError as e:
        print(e.code)
        print(e.read())


#unauth_client = fitbit.Fitbit(CLIENT_ID, CLIENT_SECRET)