import tweepy, time, sys, os, config

CONSUMER_KEY = config.CONFIG['consumer_key']
CONSUMER_SECRET = config.CONFIG['consumer_secret']
ACCESS_KEY = config.CONFIG['access_key']
ACCESS_SECRET = config.CONFIG['access_secret']
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename=open('great_hunger_3.txt','r')
text=filename.readlines()
filename.close()

filename=open('counter.save','r')
count=int(filename.read())
filename.close()

api.update_status(status=text[count])

count += 1
print(count)

filename=open('counter.save','w')
filename.write(str(count))
filename.close()