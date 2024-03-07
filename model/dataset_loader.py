from typing import Union
import csv

def load_dataset_from_csv(csv_file : str, state: bool = False) -> Union[list[list[tuple]] | list[str]]:
    """
    Loads a dataset from a CSV file.

    This function reads data from a CSV file where each row contains tagged words in the format 'word|tag'.
    It returns a list of tagged sentences, where each sentence is represented as a list of tuples (word, tag).

    Parameters:
        csv_file (str): The path to the CSV file containing tagged data.
        state (bool): A flag indicating whether to return the unique set of states/tags present in the dataset. Default is False.

    Returns:
        tagged_data (list): A list of tagged sentences, where each sentence is represented as a list of tuples (word, tag).
        states (list): A list of unique states/tags present in the dataset. Only returned if 'state' flag is set to True.
    """

    #Placeholder for all the tagged data
    tagged_data = []

    #Open the csv file containing the dataset
    with open(csv_file, 'r') as file:

        #Placeholder for all the states
        states = []

        #Parse the content of the CSV file using csv library
        reader = csv.reader(file)

        #Read each row of the dataset
        for row in reader:

            #Placeholder for each sentence that have beeb tagged
            sentence_tags = []

            #Word by word read
            for i in range(len(row)):

                #Get the word and tag
                data = row[i].split("|")

                #Append the tag if the current word tag is not in the state variable
                if data[1].strip() not in states : states.append(data[1].strip())

                #Add the word-tag pair in the sentence_tags list
                sentence_tags.append((data[0].strip().lower(), data[1].strip()))
            
            #Append the tagged sentence in the tagged_data list
            tagged_data.append(sentence_tags)
    
    if state:
        #Return the tagged data and states if the states parameter is set to True
        return tagged_data, states
    
    #Just return the tagged data if the state is false
    return tagged_data