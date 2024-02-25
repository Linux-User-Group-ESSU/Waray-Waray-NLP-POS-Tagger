from  nltk.probability import (
    LaplaceProbDist, 
    SimpleGoodTuringProbDist,
    WittenBellProbDist)
from nltk.tag import hmm
import dill
from tqdm import tqdm
from parser_nlp.read_files import read_files
from parser_nlp.states import STATES
from parser_nlp.dataset_loader import load_dataset_from_csv
from sklearn.model_selection import KFold
from random import randint
from Accuracy_Plot.accuracy_plot import plot_train


def train_hmm(dataset, trainer):
    acc = 0
    split = len(dataset) // 2
    if split == 1: split += 1
    elif split >= 80 : split = 40
    #KFold to have an unbiased training and test
    fold = KFold(n_splits=split, shuffle=True, random_state=10)
    for train, test in tqdm(fold.split(dataset), total=split, desc="Training..."):
        train_data = [dataset[i] for i in train]
        test_data = [dataset[i] for i in test]

        #Uses the LapLace Smoothing because the MLE causes Runtime Overflow
        tagger = trainer.train_supervised(
            train_data, 
            estimator=lambda fd, bins: WittenBellProbDist(fd, bins)
        )

        acc += tagger.accuracy(test_data)
    return tagger, acc / split


def main(): 
    acc = []
    total = 0
    files = read_files("Tagged_Article")
    trainer = hmm.HiddenMarkovModelTrainer(
        states=STATES,
    )
    for file in files:
        train_data = load_dataset_from_csv(f"Tagged_Article/{file}")
        #Split the dataset
        # #Train
        tagger, accuracy = train_hmm(train_data, trainer)
        acc.append(accuracy)
        total += 1
    print(sum(acc) / total)

    x = [i for i in range(1, total + 1)]

    plot_train("Multiple File", x, acc)
    
    with open("hmm_waray_tagger.pickle", "wb") as model_file:
        dill.dump(tagger, model_file)
    


if __name__ == "__main__":
    main()