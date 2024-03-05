import dill
from tokenizer import  tokenize_text
import os

def tag(token : str) -> list[tuple[str, str]]:
    cases = []
    for i in tokenize_text(token):
        if i.islower():
            cases.append("L")
        elif i.capitalize():
            cases.append("U")
        else:
            cases.append("NA")

    if token:
        model_path = os.path.join(os.path.dirname(__file__), "model.pickle")
        with open(model_path, "rb") as tag:
            tagger = dill.load(tag)
            test_sentence = tokenize_text(token.lower())
            tagged = tagger.tag(test_sentence)
            tagged_sentences = []
            for j in range(len(tagged)):
                if cases[j] == "L":
                    tagged_sentences.append([tagged[j][0].lower(), tagged[j][1]])
                elif cases[j] == "U":
                    tagged_sentences.append([tagged[j][0].capitalize(), tagged[j][1]])
                else:
                    tagged_sentences.append([tagged[j][0], tagged[j][1]])
            return tagged_sentences
    else:
        return []


if __name__=="__main__":
    print(tag("Hello worldv Model!"))