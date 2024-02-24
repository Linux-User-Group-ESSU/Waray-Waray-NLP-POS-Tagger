def split_dataset(dataset, split=.9):
    # * 90% training set and 10% test set
    split_index = int(len(dataset) * split)
    return dataset[split_index:], dataset[:split_index]