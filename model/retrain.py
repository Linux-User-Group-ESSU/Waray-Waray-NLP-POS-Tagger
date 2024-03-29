import dill
import sys
import csv
from dataset_loader import load_dataset_from_csv
from spliiter import split_dataset
from read_files import read_files
import os

args = sys.argv

def retrain(dataset, path):
	with open("model.pickle", "rb") as model_binary:
		model = dill.load(model_binary)
		test, train = split_dataset(dataset)
		model = model.train(train, test)

		with open(path, "wb") as new_model:
			dill.dump(model, new_model)

def model_checker():
	model_path = args[args.index("-m") + 1]
	if os.path.exists(model_path):
		return model_path
	else:
		return None

if "-fl" in args and "-fldr" in args or "-m" not in args:
	print("Usage: python3 retrain.py -m [model_path.pickle] -f [file name.csv] | -fldr [dataset folder]")
elif "-fl" in args:
	filepath = args[args.index("-fl") + 1]
	if filepath.endswith(".csv") and os.path.exists(filepath):
		path = model_checker()
		if path:
			model = None
			dataset = load_dataset_from_csv(filepath)
			retrain(dataset, path)
	else:
		print("Warning: Not a csv file or the file don't exist!")
elif "-fldr" in args:
	folderpath = args[args.index("-fldr") + 1]
	path = model_checker()
	if path:
		files = read_files(folderpath)
		for file in files:
			dataset = load_dataset_from_csv(f"{folderpath}/{file}")
			retrain(dataset, path)
	else:
		print("Warning: Model doesn't exist!")


else:
	print("Usage: python3 retrain.py -m [model_path.pickle] -f [file name] | -fldr [dataset folder]")

