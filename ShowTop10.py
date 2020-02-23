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


    # Making list for tweets
    final = list()
    count = 0

    # Looping through tweets based on timeline
    # Items are 50 to ensure we do not have a retweet or reply
    for tweet in tweepy.Cursor(api.user_timeline, screen_name = name, tweet_mode="extended").items(50):
        if not (tweet.full_text[0] == '@') and not (tweet.full_text[0] == 'R' and tweet.full_text[1] == 'T'):
            #print(tweet.full_text)

            count = count + 1
            temp = str(tweet.full_text)

            final += [temp]
            if count == 10:
                break;
    # Printing
    for x in range(10):
        print(x + 1,':', final[x], '\n')






name = input("Whose tweet would you like to analyze: ")
getTweets(name)