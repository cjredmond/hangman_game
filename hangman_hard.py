import random
with open("/usr/share/dict/words") as better_open_file:
    words = better_open_file.read().upper().split()

easy_words = []
med_words = []
hard_words = []
for word in words:
    if len(word) < 6:
        easy_words.append(word)
for word in words:
    if len(word) >= 6 and len(word) <= 10:
        med_words.append(word)
for word in words:
    if len(word) > 10:
        hard_words.append(word)

level = input("Please choose game level:  EASY--MEDIUM--HARD   ").upper()
game = "y"
while game == "y":

    if level == "EASY":
        chosen_word = easy_words[random.randint(0, len(easy_words)-1)]
        length = len(chosen_word)
    elif level == "MEDIUM":
        chosen_word = med_words[random.randint(0, len(med_words)-1)]
        length = len(chosen_word)
    else:
        chosen_word = hard_words[random.randint(0, len(hard_words)-1)]
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
    upper_blank = ""
    player_guess = "hello"

    while counter < 8 and upper_blank != chosen_word:

        upper_blank = "".join(blank_word)
        print(upper_blank)
        print("These letters were already guessed: {}".format(bad_guesses))
        print("You have {} of 8 strikes".format(counter))

        player_guess = input("What is your guess?   ").upper()
        while len(player_guess) > 1:
            player_guess = input("You can only guess ONE letter   ").upper()



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

    game = input("Do you want to play again Y/n?   ")
