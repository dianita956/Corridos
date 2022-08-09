import spacy
import sys
import numpy as np
from spacy import displacy
from collections import Counter
import pandas as pd

#sentiment analysis

from vaderSentiment import SentimentIntensityAnalyzer
dir()


nlp = spacy.load("es_core_news_md")

# Initialize VADER so we can use it later
sid = SentimentIntensityAnalyzer()

pd.options.display.max_colwidth = 400

corridos_filename = r'C:\Users\dmlpz\Corridos\Corridos.csv'

corridos_df = pd.read_csv(r'C:\Users\dmlpz\Corridos\Corridos.csv', encoding='utf-8', engine='python')
corridos_df.head()

def calculate_sentiment(lyrics):
    # Run VADER on the text
    scores = sid.polarity_scores(lyrics)
    # Extract the compound score
    compound_score = scores['compound']
    # Return compound score
    return compound_score

# Apply the function to every row in the "text" column and output the results into a new column "sentiment_score"
corridos_df['sentiment_score'] = corridos_df['lyrics'].apply(calculate_sentiment)
corridos_df.sort_values(by='sentiment_score', ascending=False)[:10]

pd.DataFrame(corridos_df)
