import random
import tweepy
import time
import os
from os import environ

#Auth to Twitter
CON_KEY = environ['CON_KEY']
CON_SECRET = environ['CON_SECRET']
ACC_KEY = environ['ACC_KEY']
ACC_SECRET = environ['ACC_SECRET']

auth = tweepy.OAuthHandler(CON_KEY,CON_SECRET)
auth.set_access_token(ACC_KEY,ACC_SECRET)

#Create API object
api= tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify= True)


#quote obtaining
path = 'quotes.txt'
while True:
    quote = ""
    with open(path, encoding='utf8') as f:
        lines= f.readlines()
        quote = (random.choice(lines))
    print (quote)
    #print out tweet
    api.update_status(quote)
    time.sleep(3600)




#line = (random.choice(open('quotes.txt'))))
#print (len(line))
#print(line) 


#try:
#    api.verify_credentials()
#    print("Authentication OK")
#except:
#    print("Error during auth.")
# test quotes length 
#f= open('quotes.txt')
#line = f.readline()
#while line:
#    if len(line)>280:
#        print(line)
#    line=f.readline()
#f.close()
#print('done')
#� vs ...
# � vs '

