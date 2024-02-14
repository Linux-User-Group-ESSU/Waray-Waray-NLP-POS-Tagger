import nltk

# nltk.download("punkt")
# nltk.download("averaged_perceptron_tagger")

sentence = "That one person who is big"
tokens = nltk.word_tokenize(sentence)
pos_tags = nltk.pos_tag(tokens)
print(pos_tags)
