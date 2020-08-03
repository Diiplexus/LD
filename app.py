from appKeys import keys
import requests
twitchOAuthUrl = "https://id.twitch.tv/oauth2/authorize"
twitchOAuthParams = {"client_id": appKeys.get("ClientID"), "redirect_uri":"http://localhost/", "response_type":"token", "scope":"checkTwitchDevDocsForThis"}

def get_connection_token():
    requests.get(twitchOAuthUrl, twitchOAuthParams)
    
"""
def app(self):
    pass


def get_twitch_userData(self, waitHours):
    raise NotImplementedError
"""