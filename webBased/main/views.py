from django.shortcuts import render
import dill
import os
from django.http import JsonResponse
from .form import FileUploadForm
import csv
# Create your views here.

def tokenize_text(text):
    punctuation = r".!?,'{}[]()@#$%^&*/"

    tokens = []
    current_word = ""
    for char in text:
        if char.isspace():
        # Add the current word to the list if it's not empty
            if current_word:
                tokens.append(current_word)
            current_word = ""
        elif char in punctuation:
        # Add punctuation as a separate token
            tokens.append(char)
        else:
        # Append the character to the current word
            current_word += char
    # Add the final word if it's not empty
    if current_word:
        tokens.append(current_word)

    return tokens


if __name__=="__main__":
    print(tokenize_text("ano't"))

def tag(words):
    model_path = os.path.join(os.path.dirname(__file__), "model.pickle")
    with open(model_path, "rb") as model:
        tagger = dill.load(model)
        word_tokenize = tokenize_text(words)
        return tagger.tag(word_tokenize)

def index(request):
    file_form = FileUploadForm()
    context = {
        "file_form" : file_form
    }
    return render(request, "index.html", context)

def read_file_content(request):
    if request.method == 'POST':
        if 'file' in request.FILES:
            uploaded_file = request.FILES['file']

            file_path = os.path.join("./media/", uploaded_file.name)

            html = ""
            
            with open(file_path, 'wb') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)

            if file_path.endswith(".txt"):
                with open(file_path, "r") as read:
                    data = read.readlines()
                    count = 0
                    for a in data:
                        b = a.strip("\n").strip()
                        if b:
                            tagged = tag(b.strip())
                            for i, j in tagged:
                                wordTag = j.lower()
                                if j == "?":
                                    wordTag = "punc"
                                html += f"""
                                    <div class="word-tag">
                                        <input type="text" value="{i}" class="pos-content">
                                        <br>
                                        <input type="text" value="{j}" class="pos-content {wordTag}" onkeyup="changeClass(event)" id="{count}">
                                    </div>
                                """
                                if i == "." or i == "!" or i == "?":
                                    html += "<div class='new-tag'></div>"  
                                count += 1          
            else:
                with open(file_path, "r") as csvData:
                    count = 0
                    for i in csv.reader(csvData):
                        for j in i:
                            if j.strip("\n").strip():
                                word = j.split("|")[0]
                                tag_ = j.split("|")[1]
                                if tag_ == "?":
                                    tag_ = "punc"
                                
                                html += f"""
                                    <div class="word-tag">
                                        <input type="text" value="{word}" class="pos-content">
                                        <br>
                                        <input type="text" value="{tag_}" class="pos-content {tag_.lower()}" onkeyup="changeClass(event)" id="{count}">
                                    </div>
                                """
                                if word == "." or word == "!" or word == "?":
                                    html += "<div class='new-tag'></div>"  
                                count += 1   

    data_return = {"html" : html}
    data_return["code"] = 200
    return JsonResponse(data_return)