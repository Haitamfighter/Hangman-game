from normal_hangman import normal
from advanced_hangman import advanced

# choice = input("Choose between 'normal' or 'advanced' hangman game: ").lower()
choice = "adv"

if choice == "advanced" or choice == "adv":
    advanced()
elif choice == "normal" or choice == "nor":
    normal()
