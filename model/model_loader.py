import dill
import nltk

with open("hmm_waray_tagger.pickle", "rb") as tag:
    print(tag)
    tagger = dill.load(tag)

    sentence = "Inusig ka dadama"
    token = nltk.word_tokenize(sentence)
    tagged_sentece = tagger.tag(token)
    print(tagged_sentece)