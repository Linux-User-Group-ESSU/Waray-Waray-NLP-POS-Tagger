from model.training import load_dataset_from_csv, train_hmm, split_dataset
import nltk
from nltk.tag import hmm

datas = load_dataset_from_csv("Tagged_Article/Sumat.csv")
trainer = hmm.HiddenMarkovModelTrainer()
train, test = split_dataset(datas)
data = [[('sumat', 'VB'), ('lokal/', 'XX'), ('november', 'XX'), ('12', 'NMBR'), (',', '?'), ('2012/', 'XX'), ('guinsumat', 'XX'), ('naman', 'CLTC'), ('ni', 'DT'), ('castillote', 'XX'), ('nga', 'LNKR'), ('an', 'DT'), ('papanginauon', 'XX'), ('han', 'DT'), ('ira', 'PNN'), ('buhatan', 'NN'), ('amu', 'XX'), ('in', 'XX'), ('kun', 'XX'), ('may-ada', 'XX'), ('tama', 'MDFR'), ('nga', 'LNKR'), ('labeling', 'XX'), ('an', 'DT'), ('mga', 'MDFR'), ('mulayan', 'XX'), ('ngan', 'CJTN'), ('an', 'DT'), ('mga', 'MDFR'), ('ine', 'XX'), ('in', 'XX'), ('dapat', 'XX'), ('waray', 'MDFR'), ('gamiti', 'XX'), ('hin', 'XX'), ('pintar', 'XX'), ('nga', 'LNKR'), ('pwede', 'MDFR'), ('makahilo', 'XX'), ('ngadto', 'XX'), ('han', 'DT'), ('mga', 'MDFR'), ('kabataan', 'NN'), ('ginsasagdonan', 'XX'), ('naman', 'CLTC'), ('adton', 'XX'), ('mga', 'MDFR'), ('manmaralit', 'XX'), ('nga', 'LNKR'), ('dire', 'XX'), ('basta', 'IJTN'), ('basta', 'IJTN'), ('pumalit', 'VB'), ('hin', 'XX'), ('mulayan', 'XX'), ('bisan', 'MDFR'), ('diin', 'PNN'), ('ngan', 'CJTN'), ('dapat', 'XX'), ('basahon', 'XX'), ('adton', 'XX'), ('tatak', 'XX'), ('han', 'DT'), ('mulayan', 'XX'), ('agud', 'XX'), ('masiguro', 'XX'), ('nga', 'LNKR'), ('talwas', 'XX'), ('ine', 'XX'), ('para', 'CJTN'), ('ngadto', 'XX'), ('han', 'DT'), ('imo', 'XX'), ('tatagan', 'VB')], [('sumat', 'VB'), ('lokal/', 'XX'), ('november', 'XX'), ('12', 'NMBR'), (',', '?'), ('2012/', 'XX'), ('guinsumat', 'XX'), ('naman', 'CLTC'), ('ni', 'DT'), ('castillote', 'XX'), ('nga', 'LNKR'), ('an', 'DT'), ('papanginauon', 'XX'), ('han', 'DT'), ('ira', 'PNN'), ('buhatan', 'NN'), ('amu', 'XX'), ('in', 'XX'), ('kun', 'XX'), ('may-ada', 'XX'), ('tama', 'MDFR'), ('nga', 'LNKR'), ('labeling', 'XX'), ('an', 'DT'), ('mga', 'MDFR'), ('mulayan', 'XX'), ('ngan', 'CJTN'), ('an', 'DT'), ('mga', 'MDFR'), ('ine', 'XX'), ('in', 'XX'), ('dapat', 'XX'), ('waray', 'MDFR'), ('gamiti', 'XX'), ('hin', 'XX'), ('pintar', 'XX'), ('nga', 'LNKR'), ('pwede', 'MDFR'), ('makahilo', 'XX'), ('ngadto', 'XX'), ('han', 'DT'), ('mga', 'MDFR'), ('kabataan', 'NN'), ('ginsasagdonan', 'XX'), ('naman', 'CLTC'), ('adton', 'XX'), ('mga', 'MDFR'), ('manmaralit', 'XX'), ('nga', 'LNKR'), ('dire', 'XX'), ('basta', 'IJTN'), ('basta', 'IJTN'), ('pumalit', 'VB'), ('hin', 'XX'), ('mulayan', 'XX'), ('bisan', 'MDFR'), ('diin', 'PNN'), ('ngan', 'CJTN'), ('dapat', 'XX'), ('basahon', 'XX'), ('adton', 'XX'), ('tatak', 'XX'), ('han', 'DT'), ('mulayan', 'XX'), ('agud', 'XX'), ('masiguro', 'XX'), ('nga', 'LNKR'), ('talwas', 'XX'), ('ine', 'XX'), ('para', 'CJTN'), ('ngadto', 'XX'), ('han', 'DT'), ('imo', 'XX'), ('tatagan', 'VB')]]
tagger = trainer.train(labeled_sequences=data)

print(tagger.accuracy(test))

#Test
sentence = "Sumat Lokal November 12, 2012"
token = nltk.word_tokenize(sentence.lower())
tagged = tagger.tag(token)
print(tagged)