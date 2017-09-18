from setup.config import config
from tweepy import OAuthHandler,API


class twitterAuth(object):
    #read credentials
    consumer_key=config["consumer_key"]
    consumer_secret=config["consumer_secret"]
    access_token=config["access_token"]
    access_token_secret=config["access_token_secret"]
    #get auth
    auth = OAuthHandler(consumer_key, consumer_secret)
    #set access token
    auth.set_access_token(access_token, access_token_secret)
    # api object
    api = API(auth)

twitauth= twitterAuth()
