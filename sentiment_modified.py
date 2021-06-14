import re
from textblob import TextBlob
import pandas as pd

class video_pred:
    
    
    def __init__(self,text):
        self.text = text
    def clean_text(self, text: str):
        if text:
            if type(text) == bytes: #Decoding byte strings
                text = text.decode('utf-8')
            text = re.sub(r"http\S+", "", text) #Removing URLS
            text = re.sub(r"\\b\w+(?:\.\w+)+\s*", '',  text.replace('-', '')) #Remvoing .coms
            if not text:  #Skipping empty strings
                return "" 
            return text
        else: return None
    # get sentiment score
    def get_sentiment_score(self, text: str):
        #Cleaning the text
        text = self.clean_text(text)
        if not text: return 0 #Returning empty strings
        #Getting Score
        blob = TextBlob(text)
        sentiment_score = blob.sentiment.polarity
        sentiment_score_rounded = round(sentiment_score, 6)
        return sentiment_score_rounded
    
df = pd.read_excel('/home/prudvi/Downloads/Data_Analysis/Data_Analysis/sample_data.xlsx',sheet_name='Sheet1')
for i in df['video_title']:
    score=get_sentiment_score(i)
    df['score']=score
df.head(20)    
    
