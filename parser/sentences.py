def tosentence(filepath, resource_folder, destination_folder = None):
    from os.path import join

    if destination_folder: destination_folder = join(destination_folder, filepath)
    if resource_folder: resource_folder = join(resource_folder, filepath)
    
    with open(resource_folder, "r") as dataset:
        reader = dataset.readlines()
        with open(destination_folder, "w") as new_text:
            counter = 0
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

if __name__=="__main__":
    from os import listdir
    dirs = listdir("../SHIN/articles")
    for  i in dirs:
        tosentence(i, "../SHIN/articles/", "../New_Article/")