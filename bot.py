import random
import tweepy
import time

#Auth to Twitter
auth = tweepy.OAuthHandler("pq61bLwHtKz2RWZLzaGgoCYOn", "EXvG1Yso2m3fXN44X6O6yz8Pma9oRoonXODs7OBllLxaKcnKHH")
auth.set_access_token("1286655590454964227-38BNtrJKLoADLEypfHKm4VxrmNP9qc", "bNLgKnLRAvZsDVD41UhEKbFqWquKBhALsQkGYnOqoeslz")

#Create API object
api= tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify= True)

#quote obtaining
path = 'quotes.txt'
while True:
    quote = ""
    with open(path, encoding='utf8') as f:
        lines=f.readlines()
        quote=(random.choice(lines))
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

