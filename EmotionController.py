from extractTweet import *
from calculateSentiment import *

def start():
    location = input("Enter the location to analyse tweets : ") 
    tweetEmotions(location)

if __name__ == "__main__":
   #running controller function
   start()
