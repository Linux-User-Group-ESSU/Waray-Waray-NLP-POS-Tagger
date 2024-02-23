import csv
from  nltk.probability import LaplaceProbDist
from nltk.tag import hmm
import dill
from tqdm import tqdm
from os import listdir
from parser_nlp.dataset_loader import load_dataset_from_csv
from parser_nlp.spliiter import split_dataset

def train_hmm(dataset, states):
    trainer = hmm.HiddenMarkovModelTrainer(
        states=states,
    )
    for i in tqdm(range(1), desc="Training"):
        #Uses the LapLace Smoothing because the MLE causes Runtime Overflow
        tagger = trainer.train_supervised(dataset, estimator=lambda fd, bins: LaplaceProbDist(fd, bins))
    return tagger

def main(): 
    train_data, states = load_dataset_from_csv(f"Tagged_Article/Compiled_Dataset/all.csv", state=True)
    #Split the dataset
    train, test = split_dataset(train_data)
    # #Train
    tagger = train_hmm(train, states)

    print(f"Accuracy: {tagger.accuracy(test)}")

    with open("hmm_waray_tagger.pickle", "wb") as model_file:
        dill.dump(tagger, model_file)


if __name__ == "__main__":
    main()