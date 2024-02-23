from  nltk.probability import LaplaceProbDist
from nltk.tag import hmm
import dill
from tqdm import tqdm
from parser_nlp.read_files import read_files
from parser_nlp.states import STATES
from parser_nlp.spliiter import split_dataset
from parser_nlp.dataset_loader import load_dataset_from_csv


def train_hmm(dataset, trainer):
    for i in tqdm(range(10), desc="Training"):
        #Uses the LapLace Smoothing because the MLE causes Runtime Overflow
        tagger = trainer.train_supervised(dataset, estimator=lambda fd, bins: LaplaceProbDist(fd, bins))
    return tagger

def main(): 
    files = read_files("Tagged_Article")
    trainer = hmm.HiddenMarkovModelTrainer(
        states=STATES,
    )
    for file in files:
        train_data = load_dataset_from_csv(f"Tagged_Article/{file}")
    #Split the dataset
        train, test = split_dataset(train_data)
        # #Train
        tagger = train_hmm(train, trainer)

        print(f"Accuracy: {tagger.accuracy(test)}")

    with open("hmm_waray_tagger.pickle", "wb") as model_file:
        dill.dump(tagger, model_file)


if __name__ == "__main__":
    main()