def tokenize_text(text):
    punctuation = ".!?,{}[]()@#$%^&*_"

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
            tokens.append(current_word)
            tokens.append(char)
            current_word =""
        else:
        # Append the character to the current word
            current_word += char
    # Add the final word if it's not empty
    if current_word:
        tokens.append(current_word)

    return tokens


if __name__=="__main__":
    print(tokenize_text("Hello world."))
    