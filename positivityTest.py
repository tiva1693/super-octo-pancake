import tweepy
import turtle


# Populating our lists
listOfNegatives = list()
with open ("negative.txt", "r") as myfile:
    for line in myfile:
        listOfNegatives.append(line.strip())


listOfPositives = list()
with open ("positive.txt", "r") as myfile1:
    for line in myfile1:
        listOfPositives.append(line.strip())




# Two helper functions to check if the word is positive or negative
def comparePositive(word):
    for x in range(len(listOfPositives)):
        if word == listOfPositives[x]:
            return True

def compareNegative(word):
    for x in range(len(listOfNegatives)):
        if word == listOfNegatives[x]:
            return True

def compareToList(tweet):

    # Printing our selected tweet
    print("Selected: ", tweet)

    # Creating our turtle and setting the position
    kevin = turtle.Turtle()
    kevin.pensize(5)
    turtle.title("Pos/Neg")
    turtle.screensize(2000, 1500)
    kevin.color('white')
    kevin.setpos(-325, 300)
    y = 300

    # Splitting into words
    tweetList = list(tweet.split())
    count = 0

    # Looping
    for x in range(len(tweetList)):

        # Count to ensure our lines remain on screen
        count += len(tweetList[x])

        # Checking if its positive or negative
        isPositive = comparePositive(tweetList[x])
        isNegative = compareNegative(tweetList[x])


        # Going out of bounds reposition
        if count >= 120:
            kevin.penup()
            kevin.setx(-325)
            kevin.sety(y - 100)
            y = y - 100
            kevin.pendown()
            count = 0

        # Movement if positive
        if isPositive == True:
            kevin.color('green')
            kevin.left(45)
            kevin.forward(30)
            kevin.dot(7)
            kevin.right(90)
            kevin.forward(30)
            kevin.left(45)

        # Movement if negative
        elif isNegative == True:
            kevin.color('red')
            kevin.right(45)
            kevin.forward(30)
            kevin.dot(7)
            kevin.left(90)
            kevin.forward(30)
            kevin.right(45)

        # Neutral
        else:
            kevin.color('grey')
            kevin.dot(7)
            kevin.forward(20)




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

            count = count + 1
            temp = str(tweet.full_text)

            # Setting our list
            final += [temp]

            if count == 10:
                break;
    # Printing
    for x in range(10):
        print(x + 1,':', final[x], '\n')

    # Selecting a specific tweet
    index = input("Which tweet would you like to visualise? \n =>")
    index = int(index)
    compareToList(final[index - 1])




name = input("Whose tweet would you like to analyze: ")
getTweets(name)

turtle.done()

