import csv
from checker import is_special

with open("../Untagged_Word/untagged.csv", "r") as new_tags:
    with open("newTag.csv", "a") as old_tags:
        for i in new_tags.readlines():
            word = i.split("|")[0]
            tag = i.split("|")[1].replace("\n", "").strip()
            old_tags.writelines(f"{word}|{tag}\n")

        # for i in reader:
        #     for j in i:
        #         if j:
        #             word = i.split("|")[0]
        #             if word not in datas and not is_special(word) and not word.isdigit():
        #                 datas.append(word)
        #                 tag = j.split("|")[1]
        #                 old_tags.writelines(f"{word}|{tag}\n")