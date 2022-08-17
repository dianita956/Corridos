! pip install vaderSentiment
from vaderSentiment import SentimentIntensityAnalyzer

# Initialize VADER so we can use it later
sa = SentimentIntensityAnalyzer()
import pandas as pd
pd.options.display.max_colwidth = 400

! pip install nltk
import nltk
nltk.download('punkt')
!python -m spacy download es_core_news_md
import spacy

nlp = spacy.load('es_core_news_md')

import re

pip install numpy

pip install matplotlib
import matplotlib.pyplot as plot
import numpy as np

"""#import text

"""

with open('gregoriocortez_es_corrido.txt', 'r', encoding='utf-8') as c:
  text = c.read()
  #text = re.sub('\n(.)', r'\1', text)
  print(text)
  
  ""#creating a doc container"""
  
  doc = nlp(text)
  print(doc)
for sent in doc.sents:
   print(sent)
 
 #Let’s move forward with just one of these sentences. Let’s try and grab index 0 in this attribute.
 sentences = list(doc.sents)
 print (sentences)
 
 nltk.sent_tokenize(text)
 for number, sentence in enumerate(nltk.sent_tokenize(text)):
    print(number, sentence)
 # Break text into sentences
sentences = nltk.sent_tokenize(text)

# Make empty list
sentence_scores = []
# Get each sentence and sentence number, which is what enumerate does
for number, sentence in enumerate(sentences):
    # Use VADER to calculate sentiment
    scores = sa.polarity_scores(sentence)
    # Make dictionary and append it to the previously empty list
    sentence_scores.append({'sentence': sentence, 'sentence_number': number+1, 'sentiment_score': scores['compound']})
 pd.DataFrame(sentence_scores)
 # Assign DataFrame to variable red_df
 # 10 most negative sentence
greg_df = pd.DataFrame(sentence_scores)

# Sort by the column "sentiment_score" and slice for first 10 values
greg_df.sort_values(by='sentiment_score')[:10]
 # 10 positive sentence_scores
 # Sort by the column "sentiment_score," this time in descending order, and slice for first 10 values
greg_df.sort_values(by='sentiment_score', ascending=False)[:10]
 ## Make a sentiment plot
 greg_df['sentiment_score'].plot();
 
ax = greg_df['sentiment_score'].plot(x='sentence_number', y='sentiment_score', kind='line',
                        figsize=(10,5), rot=90, title='Sentiment in Gregorio Cortez Corrido')

# Plot a horizontal line at 0
plot.axhline(y=0, color='orange', linestyle='-');
 # Get averages for a rolling window, then plot
greg_df.rolling(5)['sentiment_score'].mean().plot(x='sentence_number', y='sentiment_score', kind='line',
                        figsize=(10,5), rot=90, title='Sentiment in "Gregorio Cortez Corrido"')

# Plot a horizontal line at 0
plot.axhline(y=0, color='orange', linestyle='-');
 
 # topic modeling
 pip install pyproject-toml
 pip install wheel
 pip install hdbscan
 pip install top2vec
 from top2vect import Top2Vec
 
 """#Part of Speech tagging
 In the field of computational linguistics, understanding parts-of-speech is essential. SpaCy offers an easy way to parse a text and identify its parts of speech. Below, we will iterate across each token (word or punctuation) in the text and identify its part of speech.
 """
 
 for token in sentence1:
     print (token.text, token.pos_, token.dep_)
 
 import spacy
 from spacy import displacy
 displacy.render(sentence1, style="dep", jupyter=True, options={})
 
 displacy.render(doc, style="ent", jupyter=True)
 
 """#named entity recogniton"""
 
 for ent in doc.ents:
     print (ent.text, ent.label_)
 
displacy.render(doc, style="ent", jupyter=True)
 
 """#Word Vectors
 REsources
 https://pypi.org/project/PyDictionary/
 """
 
 !pip install PyDictionary
 from PyDictionary import PyDictionary
 
 dictionary=PyDictionary()
 
 words  = ["cantar", "vida"]
 for word in words:
     syns = dictionary.synonym(word)
     print (f"{word}: {syns[0:5]}\n")
 
 sentence1[0].vector
 
 """ Why use Word Vectors?
 
 Once a word vector model is trained, we can do similarity matches very quickly and very reliably. Let’s explore some vectors from our medium sized model. Let’s specifically try and find the words most closely related to the word dog.[cita]
 """
 
 import numpy as np
 #https://stackoverflow.com/questions/54717449/mapping-word-vector-to-the-most-similar-closest-word-using-spacy
 your_word = "atención"
 
 ms = nlp.vocab.vectors.most_similar(
     np.asarray([nlp.vocab.vectors[nlp.vocab.strings[your_word]]]), n=10)
 words = [nlp.vocab.strings[w] for w in ms[0][0]]
 distances = ms[2]
 print(words)
 
 """#doc similarity"""
 
 #doc similarity
 # Similarity of two documents
 print(doc, "<->", doc2, doc.similarity(doc2))
 
 """#word similarity"""
 
 #similarity of tokens and spans
 var1 = doc[2:4]
 var2 = doc[5]
 print(var1,'<->', var2, var1.similarity(var2))
 
 
for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
            token.shape_, token.is_alpha, token.is_stop)
