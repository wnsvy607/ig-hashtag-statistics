import requests as req


def get_token(app_id, secret_code) :
    base_url = "https://graph.facebook.com/oauth/access_token"
    res = req.get(base_url, {'client_id' : app_id, 'client_secret' : secret_code, 'grant_type' : 'client_credentials'})
    data = res.json()
    return data['access_token']

def get_account(token, ig_user_id) :
    base_url = f"https://graph.facebook.com/v19.0/{ig_user_id}"
    return req.get(base_url, {'access_token' : token}).json()