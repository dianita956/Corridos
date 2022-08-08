import spacy
import spacy
from spacy import displacy
from collections import Counter
import pandas as pd
pd.options.display.max_rows = 600
pd.options.display.max_colwidth = 400

nlp = spacy.load('es_core_news_md')

filepath = r'C:\Users\dmlpz\Corridos\la toma de Matamoros.txt'
# Open and read text
text = open(filepath, encoding='utf-8').read()
# Process text with spaCy
document = nlp(text)

outname = filepath.replace('.txt', '-lemmatized.txt')

# Create a lemmatized version of the original text file
with open(outname, 'w', encoding='utf8') as out:
    for token in document:
        # Get the lemma for each token
        out.write(token.lemma_.lower())
        # Insert white space between each token
        out.write(' ')

for token in document:
    print(token.text + ' - ' + token.lemma_)

# get named entities
document.ents
for named_entity in document.ents:
    print(named_entity, named_entity.label_)

# get name person
for named_entity in document.ents:
    if named_entity.label_ == "PER":
        print(named_entity)

#ner with long texts or many texts
import math
number_of_chunks = 80

chunk_size = math.ceil(len(text) / number_of_chunks)

text_chunks = []

for number in range(0, len(text), chunk_size):
    text_chunk = text[number:number+chunk_size]
    text_chunks.append(text_chunk)

chunked_documents = list(nlp.pipe(text_chunks))

# get ppl
people = []

for document in chunked_documents:
    for named_entity in document.ents:
        if named_entity.label_ == "PER":
            people.append(named_entity.text)

people_tally = Counter(people)

df = pd.DataFrame(people_tally.most_common(), columns=['character', 'count'])
df

#get place
places = []
for document in chunked_documents:
    for named_entity in document.ents:
        if named_entity.label_ == "LOC":
            places.append(named_entity.text)

places_tally = Counter(places)

df = pd.DataFrame(places_tally.most_common(), columns=['place', 'count'])
df

# get ner in context
from IPython.display import Markdown, display
import re

def get_ner_in_context(keyword, document, desired_ner_labels= False):

    if desired_ner_labels != False:
        desired_ner_labels = desired_ner_labels
    else:
        desired_ner_labels = ['PER', 'ORG', 'LOC']

    #Iterate through all the sentences in the document and pull out the text of each sentence
    for sentence in document.sents:
        #process each sentence
        sentence_doc = nlp(sentence.text)
        for named_entity in sentence_doc.ents:
            #Check to see if the keyword is in the sentence (and ignore capitalization by making both lowercase)
            if keyword.lower() in named_entity.text.lower()  and named_entity.label_ in desired_ner_labels:
                #Use the regex library to replace linebreaks and to make the keyword bolded, again ignoring capitalization
                #sentence_text = sentence.text

                sentence_text = re.sub('\n', ' ', sentence.text)
                sentence_text = re.sub(f"{named_entity.text}", f"**{named_entity.text}**", sentence_text, flags=re.IGNORECASE)

                display(Markdown('---'))
                display(Markdown(f"**{named_entity.label_}**"))
                display(Markdown(sentence_text))

for document in chunked_documents:
    get_ner_in_context('Mexico', document)
