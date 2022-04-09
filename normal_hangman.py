import random


def normal():
    # BASIC HANG MAN GAME

    print("Welcome in my little hang man project!")

    num_max_guesses, num_guesses = 8, 0
    easy = ["congratulations", "probably", "bankrupt", "banana", "politely", "television", "butterfly", "beautiful"]
    medium = ["possible", "impossible", "believe", "social", "rarely", "university", "politics", "moon", "possibility"]
    difficult = ["phone", "mother", "watch", "book", "partner", "lucky", "deadly", "treat", "fortune", "lame", "break"]
    expert = ["love", "hate", "bomb", "spy", "dead", "life", "duck", "cow", "man", "row", "fox", "job", "spit", "lie"]

    choices = ("easy", "medium", "difficult", "expert")
    diff = input(f"""Which difficulty would you like to have?
                        {choices}: """).lower()

    if diff == "easy":
        search_word = random.choice(easy)
    elif diff == "medium" or diff == "med":
        search_word = random.choice(medium)
    elif diff == "diff" or diff == "difficult":
        search_word = random.choice(difficult)
    elif diff == "expert":
        search_word = random.choice(expert)
    else:
        print("The answer isn't valid.")
        quit()

    output = [" _" for i in range(len(search_word))]
    list_search_word = list(search_word)
    print("".join(output))

    while num_guesses < num_max_guesses:
        user_letter = "just to make the user enter no more than a letter"
        while len(user_letter) != 1:
            user_letter = input("Guess a letter: ").lower()

        if user_letter in search_word:
            for x, y in enumerate(list_search_word):
                if user_letter == y:
                    output[x] = f" {user_letter} "
        else:
            num_guesses += 1

        print()
        join = ("".join(output))

        no_space_output = []
        for i in ("".join(output)):
            if i == " ":
                sp = ""
            else:
                sp = i
            no_space_output.append(sp)

        if ("".join(no_space_output)) == search_word:
            print(join.upper())
            if num_guesses == 0:
                print("Well.. Pretty good little genius! ")
            elif num_guesses == 1:
                print(f"FOUND in only {num_guesses} guess!")
            else:
                print(f"FOUND in only {num_guesses} guesses!")
            break
        else:
            print(join)

    if num_guesses == num_max_guesses:
        print()
        print("Ah... Sorry but unfortunately you didn't find the right word")
        print(f"It was '{search_word}'")

    # END\ BASIC HANG MAN GAME
