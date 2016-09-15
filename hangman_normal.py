import random
with open("sample.txt") as better_open_file:
    words = better_open_file.read().upper().split()

chosen_word = words[random.randint(0, len(words)-1)]
length = len(chosen_word)
# print(length)
# print(words)
# print(chosen_word)

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




while counter < 7 and winning_word != chosen_word:

    print(winning_word)
    upper_blank = "".join(blank_word)
    print(upper_blank)
    print("These letters were already guessed: {}".format(bad_guesses))


    player_guess = input("What is your guess?   ").upper()

    for current_location, current_letter in enumerate(chosen_word):
        if current_letter == player_guess:
            blank_word[current_location] = player_guess



    if player_guess in chosen_word:
        print("Good guess")
        if player_guess in good_guesses:
            print("You've already guessed that letter")
        else:
            good_guesses.append(player_guess)

    else:
        counter += 1
        print("You have {} of 7 strikes".format(counter))
        if player_guess in bad_guesses:
            print("You've already guessed that letter")
        else:
            bad_guesses.append(player_guess)
