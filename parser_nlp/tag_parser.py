import csv
tags = []
with open("newTag.csv", "w") as newTag:
    with open("all.csv", "r") as csvs:
        c = csv.reader(csvs)
        for a in c:
            for i in a:
                if i : newTag.writelines(f"{i}\n")