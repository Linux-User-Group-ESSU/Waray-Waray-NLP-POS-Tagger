import dill
import nltk

with open("hmm_waray_tagger.pickle", "rb") as tag:
    tagger = dill.load(tag)
    word = "Hi ako hi Bryan"
    test_sentence = nltk.word_tokenize(word)
    # test_sentence = ['sumat', 'naman', 'ni', 'castillote', 'nga', 'an', 'papanginauon', 'han', 'ira', 'buhatan', 'amu', 'in', 'kun', 'may-ada', 'tama',]
    tagged_sentece = tagger.tag(test_sentence)
    print(tagged_sentece)