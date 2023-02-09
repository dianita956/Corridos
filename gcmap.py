# %%
pip install geopandas as gpd
import geopandas as gpd
from pyproj import CRS
import pandas as pd
import numpy as np
import streamlit as st

from geograpy import places
import re

import geopy
from geopy.geocoders import ArcGIS
#from geopy.extra.rate_limiter import RateLimiter

import shapely
from shapely.geometry import Point
from shapely.wkt import loads
import plotly.express as px 

import contextily as cx
import xyzservices.providers as xyz
import matplotlib.pyplot as plt #to make sure there are no errors when plotting a graph
import pyproj

#import nltk

import spacy
from spacy import displacy

import googlemaps

import locationtagger
nlp = spacy.load("en_core_web_sm")

# %%
text = "corrido corpus\ElCorridodeGregorioCortez_X.txt"
with open(text, 'r', encoding='utf-8') as c:
    text = c.read()
    
def clean_text(text):
    cleaned= re.sub(r'[":;,.“”]', "", text)
    return(cleaned)
textclean = clean_text(text)
#print(text)


TxGPE=[]
nlp = spacy.load("tx_trained_ner")
doc =nlp(text) 
#print(doc)
for ent in doc.ents:
    #print(ent.text, ent.label_)
    if ent.label_ == "GPE":
        TxGPE.append(ent.text)
print(TxGPE)

# %%
ents = [(e.text, e.start_char, e.end_char, e.label_)for e in doc.ents]
print(ents)

ents = [(e.text)for e in doc.ents]
print(ents)

# %%
displacy.render(doc, style ='ent', jupyter=True, page=True)

# %% [markdown]
# Geoparsing: Finding places from the corrido lyrics

# %%
df = pd.DataFrame(ents, columns=["NER_Places"])
geolocator = ArcGIS(user_agent='CorridosMap')
geocode = lambda query: geolocator.geocode("%s, Texas" % query)
df['Location'] = df['NER_Places'].apply(geocode)
#df['geometry'] = df['NER_Places'].apply(geocode)
df

# %%
gdf = gpd.tools.geocode(df.Location, provider='ArcGIS')
gdf = gpd.GeoDataFrame(gdf, crs="EPSG:4326")
gdf["lat"]=gdf['geometry'].y
gdf ["lon"] = gdf['geometry'].x

gdf

# %%
#txt = st.text_area('El Corrido de Gregorio Cortez', text)
st.write(text)
# %%
st.map(gdf)
# %%
px.set_mapbox_access_token(open("mapboxtoken").read())
fig = px.line_mapbox(gdf,
                        lat=gdf.geometry.y,
                        lon=gdf.geometry.x,
                        hover_name="address",
                       
                        )

fig.update_layout(mapbox_style="stamen-terrain", mapbox_zoom=6, mapbox_center_lat = 29,
    margin={"r":0,"t":0,"l":0,"b":0})



fig.show()

# %%
gdf.to_json()


