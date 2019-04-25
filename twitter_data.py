#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import pandas as pd

##You need to create a twitter app at developer.twitter.com and then from there fetch required token keys:
#Variables that contains the user credentials to access Twitter API 
access_token = "youraccess_token"
access_token_secret = "token_secret"
consumer_key = "API_key"
consumer_secret = "API_secret"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['your_object1', 'object2' ])  ##fill in with data, you want to use to filter your tweets 
    
    #Once you replace the relevant data , you can then run the file from cmd and save the output to a text file.
    
