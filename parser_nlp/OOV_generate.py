import random
import string

def generate_oov_sentence(vocabulary, random_words, oov_ratio=0.7):
  sentence = []
  for _ in range(10):
    if random.random() < oov_ratio:
      sentence.append(random.choice(random_words))
    else:
      word = random.choice(vocabulary)
      sentence.append(word)
  return " ".join(sentence)

# sentence = generate_oov_sentence(vocabulary)
# print(sentence)


def generate_random_word():
    min_length = 3
    max_length = random.randint(3, 12)
    if min_length > max_length:
        raise ValueError("Minimum length must be less than or equal to maximum length.")

    # Get a random length between min and max (inclusive)
    word_length = random.randint(min_length, max_length)

    # Generate random characters
    characters = ''.join(random.choice(string.ascii_letters) for _ in range(word_length))

    return characters

    # Example usage

vocabulary = []
with open("newTag.csv", "r") as vo:
    for voc in vo:
      vocabulary.append(voc.split("|")[0])

for i in range(7):
    with open(f"../New_Article/Random{i}.txt", "w") as rand:
        for _ in range(50):
            random_text = []
            for _ in range(12):
                random_text.append(generate_random_word())
            sentence = generate_oov_sentence(vocabulary, random_text)
            rand.writelines(f"{sentence}\n")