#!/usr/bin/env python

# Tweepy followback bot
import tweepy
import logging
from config import create_api
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def followback(api):
    logger.info("Retrieving and following followers")
    for follower in tweepy.Cursor(api.followers).items():
        if not follower.following:
           logger.info(f"Following {follower.name}")
           follower.follow()
           return

def main():
    api = create_api()
    while True:
        followback(api)
        logger.info("Waiting...")
        time.sleep(60)

if __name__ == "__main__":
   main()
