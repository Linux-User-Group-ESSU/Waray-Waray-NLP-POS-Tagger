import csv
from tag_file_loader import load_tagset
from read_files import read_files
from string import punctuation

punctuations = list(set(punctuation))
datas = load_tagset("newTag.csv")
files = read_files("../Tagged_Article")

for file in files:
    updated = []
    with open(f"../Tagged_Article/{file}", "r") as newArt:
        reader = csv.reader(newArt)
        for i in reader:
            sentence = []
            for j in i:
                word = j.split("|")[0]
                tag = j.split("|")[1]

                if word in datas:
                    wordTag = datas[word]
                    if wordTag == tag or tag == "NN" or tag == "PNN":
                        sentence.append(f"{word}|{tag}")
                    else:
                        sentence.append(f"{word}|{wordTag}")
                elif word in punctuation:
                    sentence.append(f"{word}|?")
                else:
                    sentence.append(f"{word}|{tag}")
            updated.append(sentence)
    
    with open(f"../Tagged_Article_Corrected/{file}", "w") as corrected:
        writer = csv.writer(corrected)

        for i in updated:
            writer.writerow(i)