from requests_oauthlib import OAuth2Session

CLIENT_ID = '2285WZ'
CLIENT_SECRET = '8e0c01e96edd6f3dafe6ebf63cdf28b2'
REDIRECT='https://localhost/AccManager.html'

fitbit_site = OAuth2Session(CLIENT_ID,
                            redirect_uri=REDIRECT,
                            scope=['activity', 'heartrate', 'sleep', 'weight'])

authorization_url, state = fitbit_site.authorization_url(
    'https://www.fitbit.com/oauth2/authorize',
    expires_in=604800
)

OAUTH_SESSIONS = {'fitbit': fitbit_site}
API_DICT = {'fitbit': authorization_url}