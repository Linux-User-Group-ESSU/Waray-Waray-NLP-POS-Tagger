#!/usr/bin/python3
from os import listdir

dirs = listdir("SHIN/articles")
for  i in dirs:
    with open(f"SHIN/articles/{i}", "r") as dataset:
        reader = dataset.readlines()
        with open(f"New_Article/{i}", "w") as new_text:
            counter = 0
            tagged = []
            for sent in reader:
                #skip the author and published by
                if counter >= 1 and counter <= 3: pass
                else:
                    if not sent.strip("\n"): pass
                    else:
                        data = sent.split(".")
                        if not data: pass
                        else:
                            for sentences in data:
                                sentence = sentences.replace("\n", "").replace('“', "").replace('”', "").replace('"', "").strip()
                                if not sentence: continue
                                new_text.write(f"{sentence}\n")
                counter += 1