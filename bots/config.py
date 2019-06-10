import tweepy
import logging
import os

logger = logging.getLogger()

#print(os.getenv('CONSUMER_KEY', "hello"))
#print(os.environ['CONSUMER_KEY'])
print(os.environ['CONSUMER_KEY'])
#print os.environ

def create_api():
   # consumer_key = unicode(str(os.getenv("CONSUMER_KEY")), "utf-8")
   # consumer_secret = unicode(str(os.getenv("CONSUMER_SECRET")), "utf-8")
   # access_token = unicode(str(os.getenv("ACCESS_TOKEN")), "utf-8")
   # access_token_secret = unicode(str(os.getenv("ACCESS_TOKEN_SECRET")), "utf-8")
    
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api
