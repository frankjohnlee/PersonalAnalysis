import fitbit

CLIENT_ID = '2285WZ'
CLIENT_SECRET = '8e0c01e96edd6f3dafe6ebf63cdf28b2'

'https://www.fitbit.com/oauth2/authorize?response_type=code&client_id=2285WZ&redirect_uri=http://localhost:8080/&scope=activity%20nutrition%20heartrate%20location%20nutrition%20profile%20settings%20sleep%20social%20weight'

unauth_client = fitbit.Fitbit(CLIENT_ID, CLIENT_SECRET)