import dill
import nltk

with open("Single_Train_tagger.pickle", "rb") as tag:
    tagger = dill.load(tag)
    word = "yakan ni Ada"
    test_sentence = nltk.word_tokenize(word.lower())
    # test_sentence = ['sumat', 'naman', 'ni', 'castillote', 'nga', 'an', 'papanginauon', 'han', 'ira', 'buhatan', 'amu', 'in', 'kun', 'may-ada', 'tama',]
    tagged_sentece = tagger.tag(test_sentence)
    print(tagged_sentece)
