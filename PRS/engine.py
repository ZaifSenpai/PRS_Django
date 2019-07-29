import gensim
from api.models import Sms, Recommendation, Topics
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from datetime import datetime
from sklearn.datasets import fetch_20newsgroups
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
import re
import time


def lemmatize_stemming(text):
    stemmer = PorterStemmer()
    return stemmer.stem(WordNetLemmatizer().lemmatize(text, pos='v'))


def tokenize_lemmatize(text):
    result = []
    for token in gensim.utils.simple_preprocess(text):
        if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
            result.append(lemmatize_stemming(token))
    return result


class RecommenderEngine():

    def __init__(self):
        pass

    def process_next_chunk(self):
        userId, smsids, text = self.retrieve_para()
        if not text:  # text is None of empty
            return
        try:
            sentiment = self.sentiment_analysis(text)
            topics = self.extract_topics(text, sentiment)
            self.update_db(userId, topics, smsids)
        except Exception as e:
            print(e)

    def retrieve_para(self):
        sms = Sms.objects.filter(IsProcessed=False).first()
        if not sms:
            return None, None, None
        startdate = datetime.fromtimestamp(int(str(sms.Date)[:10]))

        receiver = sms.Address
        sender = sms.UserId

        # get first 100 sms of same sender and receiver
        sms_set = Sms.objects.filter(UserId=sender, Address=receiver)[:100]

        sms_ids = []
        text = ''
        # iterate through sms to collect conversation done in a particular time interval
        for s in sms_set:
            dt = datetime.fromtimestamp(int(str(s.Date)[:10]))
            diff = dt - startdate
            if int(diff.total_seconds()) > 900:  # time difference is more than 15 minutes
                break
            text += s.Body + '. '
            sms_ids.append(s.Sms_ID)

        return sender, sms_ids, text

    def sentiment_analysis(self, text):
        blob = TextBlob(text, analyzer=NaiveBayesAnalyzer())
        return blob.sentiment

    def extract_topics(self, text, sentiment):
        if (sentiment.classification == 'pos'):
            tokens = tokenize_lemmatize(text)
            if not tokens:
                return
            processed = [tokens]
            dictionary = gensim.corpora.Dictionary(processed)
            if not dictionary:
                return
            bow_corpus = [dictionary.doc2bow(doc) for doc in processed]
            if not (bow_corpus):
                return
            lda_model = gensim.models.LdaMulticore(bow_corpus,
                                                   num_topics=1,
                                                   id2word=dictionary,
                                                   passes=10,
                                                   workers=2)
            if (lda_model.show_topics()):
                return re.findall('"(.*?)"', lda_model.show_topics()[0][1])

    def update_db(self, userId, topics, smsids):
        sms = Sms.objects.filter(pk__in=smsids)
        for s in sms:
            s.IsProcessed = True
            s.save()

        dtn = int(time.time())
        for topic in topics:
            Topics.objects.create(Title=topic, ProcessedDatetime=dtn)

        return


sample_text_advice = """
I am interested in anything that is interesting. Eclecticity seeps into my brain much more easily than the thunderingly similar data of a single concentrated topic area. Though I tend to gravitate towards computer, science, and math information, I will just as likely find an article on a political, religious, or historical topic just as interesting as an article on how astronauts keep their Coke fizzy in space or a book on how public key encryption works. 

My interests are gauged by how much time I spend in each of them. I spend time on my personal relationship with Christ (greatest interest), computing, writing, performing trumpet, and cycling, in order. 

Though I do not spend most of my daily time actively engaging in monastic exercises of personal study and reflection, or even in what would popularly be considered religious activity, I have determined to mold my entire life, moment by moment, in a way that is pleasing to God. This is my greatest interest. 

The second-most done activity in my life is computing, as it is currently my job. I do try to spend some time off the clock exercising this interest, but if allowed free in the wild, it would probably take third place to the next interest: writing. 

I enjoy writing very much. My writing topics and style tend to match my eclecticity, though I enjoy the role of an essayist-poet most of all. I have written many instructional articles, though I have lately stayed away from them due to my over-exercise of that area of writing. I enjoy poetry, and while few poets ever put bread on the table and write substantial amounts of poetry, I am not motivated by anything primarily for money and find poetry an expressive way to communicate things that prose is unable to. 

I have played the trumpet since the end of third grade and have become fairly accomplished at it. Music is important to me, and I find the practicing every day to be a satisfying relaxation. 

When I have time to ride my bicycle, I do. At one point, I used to actively train and race, when I came out of obesity and worked more diligently on my physique than I am now.
"""

# https://axesso-axesso-amazon-data-service-v1.p.rapidapi.com/amz/amazon-search-by-keyword?sortBy=relevanceblender&domainCode=com&page=1&keyword=game+team
## URL Parameters:
# sortBy			relevanceblender
# domainCode		com
# page				1
# keyword 			game+team
## Headers:
# X-RapidAPI-Host	axesso-axesso-amazon-data-service-v1.p.rapidapi.com
# X-RapidAPI-Key	c10e853eb8msh471d1730b3b5c9ep19ed71jsnb9ba58f02d4b
# 
