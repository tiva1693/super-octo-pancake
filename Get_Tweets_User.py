
# This function is the base to get tweets based on a specified username
# We take in your specific consumer and access keys and then authenticate
# The for loops through and takes individual tweets and prints them

import tweepy

def getTweets(name):

    # Personal consumer and access
    consumer_key = "xxxxxxxxxxxxxxxxxxxx"
    consumer_secret = "xxxxxxxxxxxxxxxxxxxx"
    access_token = "xxxxxxxxxxxxxxxxxxxx"
    access_token_secret = "xxxxxxxxxxxxxxxxxxxx"

    # Getting twitter authorization of key
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    # Getting twitter authentication of secret
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # Looping through getting 10 tweets
    for tweet in tweepy.Cursor(api.user_timeline, screen_name = name, tweet_mode="extended").items(10):
        if not (tweet.full_text[0] == '@') and not (tweet.full_text[0] == 'R' and tweet.full_text[1] == 'T'):
            print(tweet.full_text)
            print("\n")


def run():
    name = input("Enter name of the user: ")
    getTweets(name)


run()