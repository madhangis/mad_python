import tweepy,sys,random,requests
from time import sleep
consumer_key=" "#provide consumer key ,which will be obtained after app creation
consumer_secret=" "#provide consumer key secret ,which will be obtained while getting consumer key
access_token=" "#Access key and access secret key are obtained along with consumer keys and the values nedds to be correctly copy pasted
access_token_secret=" "
author=tweepy.OAuthHandler(consumer_key,consumer_secret)
author.set_access_token(access_token,access_token_secret)
author.secure=True
api=tweepy.API(author)
myjoke=requests.get("http://api.icndb.com/jokes/random/?escape=javascript")#link for posting random jokes
myStatusText=str(myjoke.json()['value']['joke'])

       
mybot=api.get_user(screen_name='@madhangicreates')#give your screen name madhangicreates is mine leaving it as it is for example purpose
mylist=api.get_list('@'+mybot.screen_name,slug='my-list')
print('running bot:@' + mybot.screen_name+"\n using list:"+mylist.name+"\n member count for mylist"+str(mylist.member_count))

for tweet in tweepy.Cursor(api.search,q='#Halloween').items(3):#i have given q as #halloween ,which is my subject of discussion you can give any other # of preference
    try:
        if tweet.user.id==mybot.id:
            continue
        print('found tweet by:'+tweet.user.screen_name)
        if (tweet.retweeted==False) or (tweet.Favorited==False):
            tweet.retweet()
            tweet.favorite()
            
            api.add_list_member(screen_name=tweet.user.screen_name,owner_screen_name=mybot.screen_name,list_id=mylist.id)
            api.update_status(status=myStatusText)
            print(":) retweeted and favorite list + added users to mylist !!")
        if tweet.user.following==False:
            tweet.user.follow()
            print("following the user /\:)")
    except tweepy.TweepError as e:
        print(e.reason)
        sleep(5)
        continue
    except StopIteration:
        break
    
    
    except tweepy.TweepError as e:
        print(e.reason)
        sleep(5)
        continue
    except StopIteration:
        break
    
    
