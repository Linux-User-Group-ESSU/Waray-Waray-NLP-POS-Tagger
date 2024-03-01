words = []
untagged = []
repeated = {}
tags = []
with open("newTag.csv", "r") as file:
    for i in file.readlines():
        if i:
            word = i.split("|")[0]
            tag = i.split("|")[1]
            if i.split("|")[1].strip().replace("\n", "").lower() == "xx":
                pass
            else:
                if word not in words:
                    words.append(word)
                    tags.append(f'{word}|{tag}')
                else :
                    if word in repeated:
                        repeated[word] = repeated[word] + 1
                    else:
                        repeated[word] =  1 

# total = 0
# for i in repeated:
#     total += repeated[i] + 1
# print(total)
with open("newTag.csv", "w") as newTag:
    for  i in tags  :
        newTag.writelines(i)

# with open("../Untagged_Word/untagged.csv", "w") as untag:
#     for i in untagged:
#         untag.writelines(f"{i}\n")

# print(repeated)
