# don't forget that it is very important that you have installed the necessary packages for the bot to work properly. (Tweepy and Schedule)

import tweepy
import schedule
import time
import random

# here put your keys that were given by Twitter Developers.
# https://github.com/NiicoBANNED
# If you are going to host your twitter bot on a public page, I recommend creating an .env file to keep your bot keys safe.

consumer_key = 'API_KEY'
consumer_secret = 'API_KEY_SECRET'

key = 'ACCESS_TOKEN'
secret = 'ACCESS_TOKEN_SECRET'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

# Here you put the randoms words that you want your bot to say (You can put all the words you want).

a_array = ['word 1','word 2','word 3']


# What it does is open the file (last_id.txt), read it, then put the last id of the tweet in which the bot was mentioned and finally exit and save it (it's an infinite loop).

def read_last_id():
        file = open('last_id.txt', 'r')
        id = int(file.read().strip())
        file.close()
        return id

def store_last_id(id):
        file = open('last_id.txt', 'w')
        file.write(str(id))
        file.close()

# Respond to the mention with a random word that we have placed in the array and save the id of the tweet (last_id.txt)

def reply_a(tweet):
        api.update_status(
                '@' + tweet.user.screen_name + ' ' + random.choice(a_array),
                tweet.id
        )
        store_last_id(tweet.id)

def tweet_a():
    api.update_status(random.choice(a_array))


def check_mentions():
    mentions = api.mentions_timeline(read_last_id(), tweet_mode='extended')
    for tweet in reversed(mentions):
        print(tweet.full_text)

def main():
    schedule.every(7).seconds.do(check_mentions)

    while True:
        try:
            schedule.run_pending()
            time.sleep(2)
        except tweepy.TweepError as e:
            raise e

if __name__ == "__main__":
 main()

