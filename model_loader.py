import dill
import nltk
from tokenizer import tokenize_text

with open("Single_Train_tagger.pickle", "rb") as tag:
    tagger = dill.load(tag)
    word = "it mga maestro ha essu sige la it pamolmol hin nakadto ha cebu"
    test_sentence = tokenize_text(word.lower())
    # test_sentence = ['sumat', 'naman', 'ni', 'castillote', 'nga', 'an', 'papanginauon', 'han', 'ira', 'buhatan', 'amu', 'in', 'kun', 'may-ada', 'tama',]
    tagged_sentece = tagger.tag(test_sentence)
    print(tagged_sentece)
