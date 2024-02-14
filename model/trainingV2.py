import nltk
from nltk.tag import hmm

# Your dataset
train_data = [[('an', 'DT'), ('ayam', 'PRP'), ('inusig', 'NN'), ('makusog', 'inusig')], 
              [('hi', 'PRP'), ('karuyag', 'karuyag'), ('tsokolate', 'VB')]
              # Add the rest of your data here...
             ]

# Train the model
trainer = hmm.HiddenMarkovModelTrainer()
tagger = trainer.train_supervised(train_data)

# Test the model
test_sentence = "an ayam inusig makusog".split()
print(tagger.tag(test_sentence))