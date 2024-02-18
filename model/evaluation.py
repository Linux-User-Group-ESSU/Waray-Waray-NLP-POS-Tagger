from sklearn.model_selection import KFold
from collections import defaultdict
from training import train_hmm, load_dataset_from_csv
import dill

def evaluate_hmm_tagger(tagged_sentences, num_folds=5):
    # Initialize a KFold cross-validator. All folds are used for validation except num_folds-1
    # Split the dataset into num_folds time and shffle the dataset before splitting 
    kf = KFold(n_splits=num_folds, shuffle=True)

    # Create a dictionary where the data is a float initialize to 0.0
    overall = defaultdict(float)

    #Open the model
    with open("hmm_waray_tagger.pickle", "rb") as model_tagger:
        tagger = dill.load(model_tagger)
        for _, test_index in kf.split(tagged_sentences):
            # Test and train data
            test = [tagged_sentences[i] for i in test_index]

            accuracy = tagger.accuracy(test)

            # Update overall accuracy
            overall['accuracy'] += accuracy

        # Calculate average evaluation metrics over all folds
        num_test_folds = len(list(kf.split(tagged_sentences)))
        overall['accuracy'] /= num_test_folds

    return overall

tagged_sentences = load_dataset_from_csv("../Tagged_Article/Ada.csv")
evaluation_results = evaluate_hmm_tagger(tagged_sentences)
print("Evaluation results:")
print("Accuracy:", evaluation_results['accuracy'])
