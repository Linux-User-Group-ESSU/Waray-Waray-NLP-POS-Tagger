from  nltk.probability import LaplaceProbDist, WittenBellProbDist, SimpleGoodTuringProbDist
from nltk.tag import hmm
import dill
from tqdm import tqdm
from os import listdir
from parser_nlp.dataset_loader import load_dataset_from_csv
from parser_nlp.spliiter import split_dataset
from  sklearn.model_selection import KFold

def train_hmm(dataset, states):
    acc = 0
    trainer = hmm.HiddenMarkovModelTrainer(
        states=states,
    )
    fold = KFold(n_splits=220, shuffle=True, random_state=100)
    for train, test in tqdm(fold.split(dataset), total=220, desc="Training..."):
        train_data = [dataset[i] for i in train]
        test_data = [dataset[i] for i in test]
        #Uses the LapLace Smoothing because the MLE causes Runtime Overflow
        tagger = trainer.train_supervised(train_data, estimator=lambda fd, bins: WittenBellProbDist(fd, bins))
        acc += tagger.accuracy(test_data)
    return tagger, acc / 220

def main(): 
    train_data, states = load_dataset_from_csv(f"Tagged_Article/Compiled_Dataset/all.csv", state=True)
    #Split the dataset
    train, test = split_dataset(train_data)
    # #Train
    tagger, accuracy = train_hmm(train, states)
    print(accuracy)

    print(f"Accuracy: {tagger.accuracy(test)}")


    with open("hmm_waray_tagger.pickle", "wb") as model_file:
        dill.dump(tagger, model_file)


if __name__ == "__main__":
    main()