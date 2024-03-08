import dill
from tokenizer import tokenize_text
import os

#Kuhaa an absolute path han model
model_path = os.path.join(os.path.dirname(__file__), "model.pickle")

#Buksa an model nga ginsave
with open(model_path, "rb") as tag:

    #Ig load an binary nga model into python
    tagger = dill.load(tag)

    #Word ngaim karuyag i-tag
    word = "it mga maestro ha essu sige la it pamolmol hin nakadto ha cebu"

    #Ig tokenize it word
    test_sentence = tokenize_text(word.lower())

    #Ig tag an word kun ano nga POS
    tagged_sentece = tagger.tag(test_sentence)

    #Print and tagged word
    print(tagged_sentece)
