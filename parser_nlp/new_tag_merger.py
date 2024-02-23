import csv

with open("dataset.csv", "r") as new_tags:
    with open("newTag.csv", "a") as old_tags:
        reader = csv.reader(new_tags)

        for i in reader:
            if i[0] and i[1]:
                word = i[0].strip()
                tag = i[1].replace('\n', '').strip()
                old_tags.writelines(f"{word}|{tag}\n")