import random

with open("sample.txt") as better_open_file:
    words = better_open_file.read().upper().split()

random_length = random.randint(4,9)
word_bank = words
# for word in words:
#     if len(word) == random_length:
#         word_bank.append(word)
# print(word_bank)
counter = 0
while counter < 4:
    counter += 1
    guess = input("Guess a letter     ").upper()

    for word in word_bank:
        if guess not in word:
            word_bank.remove(word)
print(word_bank)
