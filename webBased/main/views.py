from django.shortcuts import render
import dill
import os
from django.http import JsonResponse
from .form import FileUploadForm
# Create your views here.

def tokenize_text(text):
    punctuation = r".!?,'{}[]()@#$%^&*"

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
            
            with open(file_path, 'wb') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)
            
            datas = []
            html = ""
            
            with open(file_path, "r") as read:
                data = read.readlines()
                for i in data:
                    tagged = tag(i.strip())
                    for i, j in tagged:
                        html += f"""
                            <div class="word-tag">
                                <input type="text" value="{i}" class="pos-content">
                                <br>
                                <input type="text" value="{j}" class="pos-content">
                            </div>
                        """
                        if i == "." or i == "!" or i == "?":
                            html += "<div class='new-tag'></div>"            

    data_return = {"html" : html}
    data_return["code"] = 200
    return JsonResponse(data_return)