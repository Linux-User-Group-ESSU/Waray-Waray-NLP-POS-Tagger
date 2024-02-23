def load_dataset_from_csv(csv_file, state: bool = False):
    import csv
    #Placeholder to contain all the training sentence and tags
    tagged_data = []
    with open(csv_file, 'r') as file:
        #Read the dataset
        states = []
        reader = csv.reader(file)
        #Itterate over the dataset
        sentence_tags = []
        for row in reader:
            for i in range(len(row)):
                data = row[i].split("|")
                if data[1].strip() not in states : states.append(data[1].strip())
                sentence_tags.append((data[0].strip().lower(), data[1].strip()))
            tagged_data.append(sentence_tags)
    if state:
        return tagged_data, states
    return tagged_data