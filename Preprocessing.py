#preprocessing of the tweets.
from replacers import SpellingReplacer
import re
from nltk.stem import PorterStemmer
import enchant
from nltk.corpus import stopwords

def preprocess(tweet):

    tweet=tweet.lower()

    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','URL',tweet)
    
    tweet = re.sub('@[^\s]+','AT_USER',tweet)
    
    tweet = re.sub('[\s]+', ' ', tweet)
    
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)

    tweet = tweet.strip('\'"')

    tweet = re.sub(r'\d+', '', tweet)
    
    stop = set(stopwords.words('english'))
    tweet_list=tweet.split(" ")
    stop_tweet=[]
    
    for word in tweet_list:
        if word not in stop and len(word)>3:
            stop_tweet.append(word)
    
    return (stop_tweet)

def spell_correction(tweet):
    
    replacer=SpellingReplacer()
    length=len(tweet)
    i=0
    dGB=enchant.Dict('en_GB')   
    
    while i<length:
        if not dGB.check(tweet[i]):
            tweet[i]=replacer.replace(tweet[i])
        i=i+1
    
    return str(tweet)

input_tweet=raw_input('Enter the tweet:')
pre_tweet=preprocess(input_tweet)
final_tweet=spell_correction(pre_tweet)
print str(final_tweet)





