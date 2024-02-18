import csv
import nltk
from nltk.tag import hmm
import dill
import os
from tqdm import tqdm

def load_dataset_from_csv(csv_file):
    #Placeholder to contain all the training sentence and tags
    tagged_data = []
    with open(csv_file, 'r') as file:
        #Read the dataset
        reader = csv.reader(file)
        #Itterate over the dataset
        sentence_tags = []
        for row in reader:
            for i in range(len(row)):
                data = row[i].split("|")
                sentence_tags.append((data[0].strip().lower(), data[1].strip()))
            tagged_data.append(sentence_tags)
    return tagged_data


def split_dataset(dataset, split=.9):
    # * 90% training set and 10% test set
    split_index = int(len(dataset) * split)
    return dataset[:split_index], dataset[split_index:]

def train_hmm(dataset):
    trainer = hmm.HiddenMarkovModelTrainer()
    for i in tqdm(range(1), desc="Training"):
        tagger = trainer.train_supervised(dataset)
    return tagger

def main():    
    train_data = load_dataset_from_csv(f"../Tagged_Article/Compiled_Dataset/all.csv")
    #Split the dataset
    train, test = split_dataset(train_data)
    # #Train
    tagger = train_hmm(train)

        # #Accuracy tester
    acurracy = tagger.accuracy(test)
    print(f"Accuracy: {acurracy}")

    #Test
    # sentence = "usa, duha"
    # tokens = ["usa", "duha"]
    # tagged_sentence = tagger.tag(tokens)
    # print("Tagged sentence:", tagged_sentence)

    # #Model saver
    with open("hmm_waray_tagger.pickle", "wb") as model_file:
        dill.dump(tagger, model_file)

if __name__ == "__main__":
    main()