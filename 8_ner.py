import spacy 
  
nlp = spacy.load("xx_ent_wiki_sm") 
  
sentence = "Valsts prezidents Egils Levits piedalījās pasākumā, ko organizēja Latvijas Univesitāte."
print(sentence, "\n")
  
doc = nlp(sentence) 
  
for ent in doc.ents: 
    print(ent.text, "-", ent.label_) 

# Source:
# https://www.geeksforgeeks.org/python-named-entity-recognition-ner-using-spacy/
