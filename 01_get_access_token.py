import requests

# https://www.strava.com/oauth/authorize?client_id=137077&response_type=code&redirect_uri=http://localhost&scope=activity:read_all
# --->
# http://localhost/?state=&code=b8d188ffc86171967f9c4dbe060c704f2f34d0c9&scope=read,activity:read_all  AUTH CODE = b8....
# Replace with your actual values
client_id = '137077'
client_secret = 'bffaefe7156cb1b5fe13678fb2a02c621ca20355'
auth_code = 'b8d188ffc86171967f9c4dbe060c704f2f34d0c9'

# Exchange authorization code for access token
response = requests.post(
    'https://www.strava.com/oauth/token',
    data={
        'client_id': client_id,
        'client_secret': client_secret,
        'code': auth_code,
        'grant_type': 'authorization_code'
    }
)
# Get the access token from the response
access_token = response.json()['access_token']
print(f"Access Token: {access_token}")
