import random
with open("sample.txt") as better_open_file:
    words = better_open_file.read().lower().split()

chosen_word = words[random.randint(0, len(words)-1)]
length = len(chosen_word)
print(length)
print(words)
print(chosen_word)

print("The chosen word has {} letters".format(length))

good_guesses =[]
bad_guesses =[]
counter = 0
game = True

while counter < 8:
    counter += 1
    def make_underscores(word):
        underscores = []
        for burn in range(0,len(word)):
            underscores.append("_")
        return "".join(underscores)
    print(make_underscores(chosen_word))

    player_guess = input("What is your guess?   ").lower()

    if player_guess in chosen_word:
        print("Good guess")
        if player_guess in good_guesses:
            print("You've already guessed that letter")
        else:
            good_guesses.append(player_guess)

    else:
        print("Bad guess")
        if player_guess in bad_guesses:
            print("You've already guessed that letter")
        else:
            bad_guesses.append(player_guess)

    print(good_guesses)
    print(bad_guesses)
