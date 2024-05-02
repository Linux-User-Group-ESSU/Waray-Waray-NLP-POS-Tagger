from django.shortcuts import render
import dill
import os
from django.http import JsonResponse
from .form import FileUploadForm
import csv
import json
from  .models import FileUploaded
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
    f = FileUploaded.objects.all().order_by("file")
    files = []
    for i in f:
        title = str(i.file).removeprefix("media/")
        files.append({"id" : i.pk, "file" : title})
    
    context = {
        "file_form" : file_form,
        "files" : files
    }
    return render(request, "index.html", context)

def create_html(file_path):
    html = ""
    if file_path.endswith(".txt"):
        with open(file_path, "r") as read:
            data = read.readlines()
            count = 0
            for a in data:
                b = a.strip("\n").strip()
                if b:
                    tagged = tag(b.strip())
                    for i, j in tagged:
                        if i.split() != "&":
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
                        if word != "&":
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
    
    return html

def read_file_content(request):
    if request.method == 'POST':

        data_return = {}

        file_data = FileUploadForm(request.POST, request.FILES)
        if file_data.is_valid():
            save = file_data.save()

            file_path = FileUploaded.objects.get(id=save.pk)

            html = create_html(str(file_path.file))
            data_return["code"] = 200
            data_return["name"] = str(file_path.file).removeprefix("media/")
            data_return["html"] = html
        
        else:
            error = file_data.errors.as_text()
            data_return["code"] = 404
            data_return["error_data"] = error
                
    return JsonResponse(data_return)


def save_in_server(request):
    data_return = {}
    if request.method == "POST":
        data_return["code"] = 200
        data_json = json.loads(request.body)
        data_array = data_json.get('data', [])
        filename = data_json.get("filename")
        with open(f"media/{filename}", "w") as new_data:
            writer = csv.writer(new_data)
            sentence = []
            for i in data_array:
                word = i["word"].strip()
                tag = i["tag"].strip()

                if word == "." or word == "?" or word == "!":
                    sentence.append(f"{word}|{tag}")
                    writer.writerow(sentence)
                    sentence.clear()
                else:
                    sentence.append(f"{word}|{tag}")

    else:
        data_return['code'] = 403
    return JsonResponse(data_return)

def readDb(request):
    id = request.GET.get("id")
    filename = FileUploaded.objects.get(id=id)

    html = create_html(str(filename.file))

    return JsonResponse({"html" : html, "filename" : str(filename.file).removeprefix("media/")})