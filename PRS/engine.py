from api.models import *
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from datetime import datetime


class RecommenderEngine():

    def __init__(self):
        pass

    def process_next_chunk(self):
        userId, smsids, blob = self.retrieve_para_blob()
        if not blob:
            return
        try:
            blob = self.pre_process(blob)
            sentiment = self.sentiment_analysis(blob)
            topics = self.extract_topics(blob, sentiment)
            self.update_db(userId, topics, smsids)
        except Exception as e:
            pass

    def retrieve_para_blob(self):
        sms = Sms.objects.filter(IsProcessed=False).first()
        if not sms:
            return None, None, None
        startdate = datetime.fromtimestamp(int(str(sms.Date)[:10]))

        receiver = sms.Address
        sender = sms.UserId

        # get first 100 sms of same sender and receiver
        sms_set = Sms.objects.filter(UserId=sender, Address=receiver)[:100]

        sms_ids = [sms.Sms_ID]
        text = ''
        # iterate through sms to collect conversation done in a particular time interval
        for s in sms_set:
            dt = datetime.fromtimestamp(int(str(s.Date)[:10]))
            diff = dt - startdate
            if int(diff.total_seconds()) > 900: # time difference is more than 15 minutes
                break
            text += s.Body + '. '
            sms_ids.append(s.Sms_ID)

        return sender, sms_ids, TextBlob(text)

    def pre_process(self, blob):
        # Correct grammer
        pass

    def sentiment_analysis(self, blob):
        pass

    def extract_topics(self, blob):
        pass

    def update_db(self, userId, topics, smsids):
        # Sms.objects.get('').save()
        pass
