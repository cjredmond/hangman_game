import random

with open("sample.txt") as better_open_file:
    words = better_open_file.read().upper().split()

random_length = random.randint(6,8)
word_bank = []
for word in words:
    if len(word) == random_length:
        word_bank.append(word)
print(word_bank)

chosen_word = word_bank.pop(random.randint(0, len(word_bank)-1))
length = len(chosen_word)

print("The chosen word has {} letters".format(length))

def make_underscores(word):
    underscores = []
    for burn in range(0,len(word)):
        underscores.append("_")
    return underscores



good_guesses =[]
bad_guesses =[]
counter = 0
output = []
blank_word = make_underscores(chosen_word)
winning_word = "".join(blank_word).upper()
all_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I",
"J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
"V", "W", "X", "Y", "Z"]


print(chosen_word)

upper_blank = ""
while counter < 8 and upper_blank != chosen_word:

    upper_blank = "".join(blank_word)
    print(upper_blank)
    print("These letters were already guessed: {}".format(bad_guesses))
    print("These letters have not been guessed:  {}".format(all_letters))
    print("You have {} of 8 strikes".format(counter))


    player_guess = input("What is your guess?   ").upper()

    for l in all_letters:
        if l == player_guess:
            all_letters.remove(l)


    for current_location, current_letter in enumerate(chosen_word):
        if current_letter == player_guess:
            blank_word[current_location] = player_guess

    if player_guess in chosen_word:
        print("Good guess\n")
        if player_guess in good_guesses:
            print("You've already guessed that letter")
        else:
            good_guesses.append(player_guess)
    else:
        if player_guess in bad_guesses:
            print("You've already guessed that letter\n")
        else:
            counter += 1
            print("You have {} of 8 strikes\n".format(counter))
            bad_guesses.append(player_guess)
print("The word was  {} ".format(chosen_word))
