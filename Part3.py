from nltk.corpus import twitter_samples
import re
from nltk.tokenize import sent_tokenize, word_tokenize, TweetTokenizer

tweet_tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True, reduce_len=True)
all_tweets = twitter_samples.strings('tweets.20150430-223406.json')

# Total Number of Hashtags
hashTagCounter = 0
for tweets in all_tweets:
    hashtag_list = re.findall(r'\B#\w*[a-zA-Z]+\w*', tweets)
    hashTagCounter = hashTagCounter+len(hashtag_list)

print(hashTagCounter)

# Total number of mentions
mentionsCounter = 0
for tweets in all_tweets:

    mentionsList = re.findall(r'\B@\w*[a-zA-Z]+\w*', tweets)
    #print(mentionsList)
    mentionsCounter = mentionsCounter+len(mentionsList)

print(mentionsCounter)

# Total number of URLs
URLCounter = 0
for tweets in all_tweets:
    urlList = re.findall(r'^https?:\/\/.*[\r\n]*', tweets)
    URLCounter = URLCounter+len(urlList)

print(URLCounter)

# Removing hashtag and mentions from tweets
for tweets in all_tweets:
    print("Old String is : "+tweets)
    newTweetString = re.sub("@[A-Za-z0-9_]+", "", tweets)
    newTweetString = re.sub("#[A-Za-z0-9_]+", "", newTweetString)
    print("New String is : "+newTweetString)