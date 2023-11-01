# Name: NyJavion
# Prog Purpose: This M?agic 8-ball code use a Pyhton tuple since the
#               user doesn't have the ability to change the 8-bll answers.

# However, the purpose could have used a Pyhton list instead of a tuple.
# Note; Tuples use parenthese; lists use the square braces

import random

answer_8_ball = ( " As I see it, yes", "Ask again later",
                  "Better not tell you now", "Cannot predict now",
                  "Concentrate and ask again", "Don't count on it",
                  "It is certain", "It is decidedly so", "Most likely",
                  "My reply is no", "My source says no", "Outlook good",
                  "Outlook not so good", "Reply hazy try again",
                  "Signs point to yes", "Very doubtful", "Without a doubt",
                  "Yes", "Yes definitely", "You may rely on it",)

def main():

    print("I am the MAGIC-8 Ball and can answer any YES or NO questions!")

    another_question = True
    while another_question:
        answer = random.choice(answer_8_ball)

        print("\nShake the MAGIC-8 Ball")
        print("...and now...")
        question = input("\nWhat is your YES or NO question?")
        print("The MAGIC-8 Ball says: " + answer)

        askAgain = input("\nWould you like to ask another question (Y or N)?: ")
        if askAgain.upper() == "N" or askAgain == "n":
            another_question = False

    print("\nCome back again when you have other important questions.")
    print("...MAGIC-8 Ball OUT.")


main()




