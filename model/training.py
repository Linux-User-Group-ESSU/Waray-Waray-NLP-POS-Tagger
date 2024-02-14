import csv
import nltk
from nltk.tag import hmm
import dill
import os

def load_dataset_from_csv(csv_file):
    #Placeholder to contain all the training sentence and tags
    sentences = []
    with open(csv_file, 'r') as file:
        #Read the dataset
        reader = csv.reader(file)
        #Skip the header file
        next(reader)
        #Itterate over the dataset
        for row in reader:
            sentence = " ".join(row[::2]).lower().strip()
            tokens = nltk.word_tokenize(sentence)
            tagged_data = [(token, row[i+1]) for i, token in enumerate(tokens) if token]
            sentences.append(tagged_data)
    return sentences


def split_dataset(dataset, split=.9):
    # * 90% training set and 10% test set
    split_index = int(len(dataset) * split)
    return dataset[:split_index], dataset[split_index:]

def train_hmm(dataset):
    trainer = hmm.HiddenMarkovModelTrainer()
    for _ in range(500):
        tagger = trainer.train_supervised(dataset)
    return tagger

def main():
    files = os.listdir("../Tagged_Article")
    testing = []
    for i in  range(len(files)-25):
    #open the dataset
        print(f"Traning: {files[i]}")
        train_data = load_dataset_from_csv(f"../Tagged_Article/{files[i]}")
        #Split the dataset
        train, test = split_dataset(train_data)
        testing.append(test[0])
        # #Train
        tagger = train_hmm(train)

        # #Accuracy tester
    acurracy = tagger.accuracy(testing)
    print(f"Accuracy: {acurracy}")

    # #Test
    # sentence = "usa, duha"
    # tokens = nltk.word_tokenize(sentence.lower())
    # tagged_sentence = tagger.tag(tokens)
    # print("Tagged sentence:", tagged_sentence)

    # #Model saver
    with open("hmm_waray_tagger.pickle", "wb") as model_file:
        dill.dump(tagger, model_file)

if __name__ == "__main__":
    main()