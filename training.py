import csv
from  nltk.probability import LaplaceProbDist
from nltk.tag import hmm
import dill
from tqdm import tqdm
from os import listdir

def load_dataset_from_csv(csv_file):
    #Placeholder to contain all the training sentence and tags
    tagged_data = []
    states = []
    with open(csv_file, 'r') as file:
        #Read the dataset
        reader = csv.reader(file)
        #Itterate over the dataset
        sentence_tags = []
        for row in reader:
            for i in range(len(row)):
                data = row[i].split("|")
                if data[1].strip() not in states : states.append(data[1].strip())
                sentence_tags.append((data[0].strip().lower(), data[1].strip()))
            tagged_data.append(sentence_tags)
    return tagged_data, states


def split_dataset(dataset, split=.9):
    # * 90% training set and 10% test set
    split_index = int(len(dataset) * split)
    return dataset[:split_index], dataset[split_index:]

def train_hmm(dataset, states):
    trainer = hmm.HiddenMarkovModelTrainer(
        states=states,
    )
    for i in tqdm(range(1), desc="Training"):
        #Uses the LapLace Smoothing because the MLE causes Runtime Overflow
        tagger = trainer.train_supervised(dataset, estimator=lambda fd, bins: LaplaceProbDist(fd, bins))
    return tagger

def main(): 
    train_data, states = load_dataset_from_csv(f"../Tagged_Article/Compiled_Dataset/all.csv")
    print(states)
    #Split the dataset
    train, test = split_dataset(train_data)
    # #Train
    tagger = train_hmm(train, states)

    print(f"Accuracy: {tagger.accuracy(test)}")

    with open("hmm_waray_tagger.pickle", "wb") as model_file:
        dill.dump(tagger, model_file)


if __name__ == "__main__":
    main()