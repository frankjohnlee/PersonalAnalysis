import fitbit
from base64 import b64encode
import datetime as dt

CLIENT_ID = '2285WZ'
CLIENT_SECRET = '8e0c01e96edd6f3dafe6ebf63cdf28b2'
REDIRECT='https://localhost/AccManager.html'
GRANT_TYPE = 'authorization_code'

#  This is the Fitbit URL
TOKEN_URL = "https://api.fitbit.com/oauth2/token"

AUTH_B64_ENCODED = b64encode((CLIENT_ID + ":" + CLIENT_SECRET).encode("utf-8"))
AUTH_B64_ENCODED = AUTH_B64_ENCODED.decode()


def authenticate_fitbit(authorization_response, fitbit_site):
    token = fitbit_site.fetch_token(
        authorization_response=authorization_response,
        token_url=TOKEN_URL,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        Authorization='Basic {}'.format(AUTH_B64_ENCODED))
    consumer_key = CLIENT_ID
    consumer_secret = CLIENT_SECRET
    access_token = token['access_token']
    refresh_token = token['refresh_token']
    user_id = token['user_id']
    print(token)

    authd_client = fitbit.Fitbit(consumer_key, consumer_secret,
                                 access_token=access_token, refresh_token=refresh_token)

    sleep_info = authd_client.time_series(resource='sleep/minutesAsleep', period='1m')
    sleep_info = sleep_info['sleep-minutesAsleep']
    print(sleep_info)
