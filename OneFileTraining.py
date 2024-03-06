from  nltk.probability import LaplaceProbDist, WittenBellProbDist, SimpleGoodTuringProbDist
from nltk.tag import hmm
import dill
from tqdm import tqdm
from os import listdir
from parser_nlp.dataset_loader import load_dataset_from_csv
from parser_nlp.spliiter import split_dataset
from sklearn.model_selection import KFold
from Accuracy_Plot.accuracy_plot import plot_train

def train_hmm(dataset, states):
    acc : list[float] = []
    trainer = hmm.HiddenMarkovModelTrainer(
        states=states,
    )
    fold = KFold(n_splits=100, shuffle=True)
    for train, test in tqdm(fold.split(dataset), total=100, desc="Training..."):
        train_data = [dataset[i] for i in train]
        test_data = [dataset[i] for i in test]
        #Uses the LapLace Smoothing because the MLE causes Runtime Overflow
        tagger = trainer.train_supervised(train_data, estimator=lambda fd, bins: WittenBellProbDist(fd, bins))
        acc.append(tagger.accuracy(test_data))
    return tagger, acc

def main(): 
    train_data, states = load_dataset_from_csv(f"Tagged_Article/Compiled_Dataset/all.csv", state=True)
    #Split the dataset
    train, test = split_dataset(train_data)
    # #Train
    tagger, accuracy = train_hmm(train, states)
    print(sum(accuracy) / 100) #Change the 220 if you change the n_splits in KFold

    print(f"Accuracy: {tagger.accuracy(test)}")

    x = [i for i in range(1, 101)]

    plot_train("Single_File_Data", x, accuracy)

    with open("Single_Train_tagger.pickle", "wb") as model_file:
        dill.dump(tagger, model_file)


if __name__ == "__main__":
    main()