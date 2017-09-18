from tweepy import Stream, streaming
from utils.twitterAuth import twitauth
from utils.database import Database
api = twitauth.api


class gadgetStreamListener(streaming.StreamListener):
    #override on_status
    def on_status(self, status):
        print("TWEET ->  ", status.text, "Location : ", status.user.location)
        location=status.user.location
        if status.user.location == None or status.user.location =="":
            location= "Unknown"
        print("Location : ",location)
        Database.updateOne("gadgetscore",
                           filter={"name": "Iphone", "location": location},
                           update={"$inc": {"score": 1}},
                           upsert=True)

    #def on_data(self, raw_data):
    #    print(raw_data)

    def on_error(self, status):
        print(status)

    def on_limit(self, track):
        print("limit ", track.text)

    def on_exception(self, exception):
        print(exception,exception.text)


def runStream():
    myStreamListener = gadgetStreamListener()
    myStream = Stream(auth = api.auth, listener=myStreamListener)
    myStream.filter(track=["Iphone"])
