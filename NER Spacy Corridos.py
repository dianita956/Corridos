#!/usr/bin/env python
# coding: utf-8

# In[14]:


get_ipython().system('pip install requests')

get_ipython().system('pip install requests -U')


# In[15]:


from shapely.wkt import loads
import pandas as pd
import spacy
from spacy import displacy
import nltk
nlp = spacy.load("en_core_web_lg", disable=["tok2vec", "tagger", 
                                            "parser", "attribute_ruler", "lemmatizer"])

nlp.pipe_names


# In[16]:


import csv
import requests
import geopandas as gpd


# In[17]:


import json #javascript object notation to store data outside python. watch videos from Matt Digital Humanities. 
from bs4 import BeautifulSoup


# ## Web Scrap and Extract List of municipalities in Texas from Wiki 
# 
# https://en.wikipedia.org/wiki/List_of_municipalities_in_Texas
# 

# In[44]:


url ="https://en.wikipedia.org/wiki/List_of_municipalities_in_Texas"


# In[45]:


file = "../corridos/listofmunicipalitiesinTexas.txt"
s = requests.get(url)


# In[46]:


soup = BeautifulSoup(s.text, "lxml")#to tell the program to read the site as HTML (lxml)


# In[47]:


print(soup)


# In[48]:


def heading_extract():
    #find a specific item from the website to make scrapping easier. 
    heading = soup.find("h1",{"id": 'firstHeading'})
   
    with open(file,"a+", encoding='utf-8') as f:
             f.write(heading.get_text())
              
heading_extract()#check file explore
#ensure the text file is there and inputting data from the web.


# In[49]:


#content extraction
def content_extract():
    contents = soups.findAll("p")
    with open (file, "a+") as f:
        for i in contents:
            f.write(i.get_text())


# In[50]:


#sources for citation 
def get_sources():
    sources = soup.findAll("cite")
    with open(file, "a+")as f:
        f.write("\nSOURCES\n")
        for i in sources:
            f.write(i.get_text())


# In[51]:


def table_extraction():
    table = soup.find("table", class_= "wikitable sortable")
    with open (file, "a+", encoding="utf-8")as f: 
        for row in table.findAll("tr"):
            for th in row.findAll("th"):
                #ending a line break to organize the txt file
                f.write("\n" + th.get_text() + ": ")
                for td in row.findAll("td"):
                    f.write(td.get_text())
                      
table_extraction()
#print(soup.find("table", class_= "wikitable sortable"))


# run code all above

# In[ ]:





# In[ ]:


texasrequest = requests.get("https://data.texas.gov/resource/m3yf-ffwm.json")

#load data as text
texasner = texasrequest.text

#load data as GeoDataFrame
texasnerdf = pd.read_csv('https://data.texas.gov/api/views/m3yf-ffwm/rows.csv?accessType=DOWNLOAD&api_foundry=true')


# In[ ]:


texasnerdf.head()


# In[ ]:


texasnerdf.dtypes


# In[ ]:


texasnerdf['geometry'] = texasnerdf['the_geom']
texasnerdf.geometry =  texasnerdf['the_geom'].apply(loads)
#texasgdf = gpd.GeoDataFrame(texasnerdf)

texasnerdf.dtypes


# In[ ]:


texasnerdf.loc[:,["NAME","geometry"]]


# ## Text Analysis: Named Enities Reconginzation

# In[ ]:


text = open('../Corridos/corrido corpus/ElCorridodeGregorioCortez_X.txt', encoding="utf-8").read()
for number, sentence in enumerate(nltk.sent_tokenize(text)):
    print(sentence)
 # Break text into sentences
sentences = nltk.sent_tokenize(text)


# In[ ]:


doc =nlp(text)

ents =list(doc.ents)

place= []

for ent in ents:
    if ent.label_ == "GPE":
        place.append(ent)
        
print(place)
    


# In[ ]:


displacy.render(doc, style='ent')


# In[ ]:


ents = [(e.text, e.start_char, e.end_char, e.label_) for e in doc.ents]
print(ents)


# In[ ]:


# Getting the pipeline component
ner=nlp.get_pipe("ner")


# Processing Text using SpaCy and pipelines for NERs

# In[ ]:


lang = "en"
pipeline = ["ner"]

