from  nltk.probability import WittenBellProbDist        #Probability Distribution Used
from nltk.tag import hmm                                #HMM Model Trainer
import dill                                             #HMM model saver
from tqdm import tqdm                                   #Pretty training status
from dataset_loader import load_dataset_from_csv        #UDF for loading the dataset from csv
from sklearn.model_selection import KFold               #Datasset slicer
from accuracy_plot import plot_train                    #UDF for plotting the accuracy graph
from typing import Union                                #Library combining two return type

def train_hmm(dataset : list[list[str]], states : list[str]) -> Union[hmm.HiddenMarkovModelTagger, list[float]]:
    """
    Trains a Hidden Markov Model (HMM) on a dataset using K-Fold cross-validation.

    Parameters:
    dataset (list): A list of sequences where each sequence represents a training instance.
    states (str): The list of all the states in the Training set.

    Returns:
    tagger: The trained Hidden Markov Model tagger.
    acc (list): A list of accuracies achieved during cross-validation.

    Note:
    The WittenBellProbDist Smoothing technique is used in training due to potential runtime overflow issues with Maximum Likelihood Estimation (MLE) 
    and WittenBellProbDist give the highest accuracy compared to MLE and other Smoothing technique in the NLTK library.
    """

    #List containing all the accuracy in each training
    acc : list[float] = []

    #HMM trainer 
    trainer = hmm.HiddenMarkovModelTrainer(
        states=states, #States are the Tags that a model need to used or remember
    )

    #Dataset spliiter: Split the dataset n_split times and shuffle all the training data before splitting to avoid bias
    fold = KFold(n_splits=100, shuffle=True)

    #Itterate over the splitted dataset.
    #* * train and test variable in the loop contains the indices of the train and test to be used in the dataset
    for train, test in tqdm(fold.split(dataset), total=100, desc="Training..."):

        #Get the training set in the dataset by itterating over it's index.
        train_data = [dataset[i] for i in train]

        #Get the test set in the dataset by itterating over it's index.
        test_data = [dataset[i] for i in test]

        #Uses the WittenBellProbDist Smoothing because the MLE causes Runtime Overflow and WittenBellProbDist gives the highest Accuracy
        tagger = trainer.train_supervised(train_data, estimator=lambda fd, bins: WittenBellProbDist(fd, bins))

        #Test the accuracy of the model and append the score to acc variable above
        acc.append(tagger.accuracy(test_data))
    
    #Return the HMM Tagger and the list of each trainning accuracy
    return tagger, acc


def main() -> None:
    """
    Main function to execute the training of a Hidden Markov Model (HMM) on a dataset and perform related tasks.

    This function loads a dataset from a CSV file, trains an HMM using the loaded dataset,
    calculates the average accuracy of the trained model, plots the training accuracy,
    and saves the trained model to a pickle file.

    Returns:
    None
    """

    #Load the dataset and all the states/tag the dataset have
    train_data, states = load_dataset_from_csv(f"../Tagged_Article_Corrected/Compiled_Dataset/all.csv", state=True)

    #Function call to train_hmm passing the training dataet and states.
    tagger, accuracies = train_hmm(train_data, states)

    #Calculate the aaverage accuracy of the HMM Tagger
    accuracy = sum(accuracies) / 100

    #Plot the accuracy of the model in each training
    plot_train("Model_Accuracy", accuracies)

    #Binary file creation to be used to save the HMM Tagger Model
    with open("model.pickle", "wb") as model_file:

        #Save the model to the bbinary file created using dill library
        dill.dump(tagger, model_file)


if __name__ == "__main__":
    main()