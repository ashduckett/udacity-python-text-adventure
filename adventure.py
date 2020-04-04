import random
import time


def print_n_sleep(msg):
    time.sleep(1)
    print(msg)


def introduction():
    print_n_sleep("It's dark.")
    print_n_sleep("You wake up sweating.")
    print_n_sleep("You see a figure at your bedroom doorway but live alone.")


def death_takes_you():
    print_n_sleep("Death embraces you. A hug that seems to sink into " +
                  "your body.")
    print_n_sleep("You rise up.")
    print_n_sleep("You see your body and Death's boney hand across " +
                  "your chest.")
    print_n_sleep("Blackness as you pass through the structure of the house.")
    print_n_sleep("You disappear into darkness on the horse of Death.")
    print_n_sleep("You start thinking that you're getting closer to the sun.")
    print_n_sleep("It's not the sun.")
    print_n_sleep("It's the burning fires of hell.")
    print_n_sleep("It'll be a long time before you forgive yourself for " +
                  "not asking for other options.")
    print_n_sleep(("Death grins back at you as you finish the journey on the" +
                   " back of his horse..."))


def you_go_on_as_you_did():
    print_n_sleep("You won!")
    print_n_sleep("It's time to make some changes...")


def we_guess_finger_count():
    print_n_sleep("Death puts his skinless left hand behind him, grinning " +
                  "and clutching his scythe with his right.")
    print_n_sleep("How many?")

    finger_count = random.randint(1, 6)

    responses = ['1', '2', '3', '4', '5']

    response = ""
    while response not in responses:
        response = input("")
        if response in responses:
            if int(response == finger_count):
                print_n_sleep("You win!")
                you_go_on_as_you_did()
            else:
                print_n_sleep("You lose!")
                death_takes_you()
        else:
            print_n_sleep("Please select an option between 1 and 5")


def we_sell_our_soul():
    print_n_sleep("You wake up excited. You can't believe " +
                  "it's real.")
    print_n_sleep("MANY years pass. Many accidents happen " +
                  "and nothing can kill you")
    print_n_sleep("You run several business, these days, they run themselves")
    print_n_sleep("All of your loved ones have passed on.")
    print_n_sleep("You realise no amount of money or lifespan " +
                  "can make you happy.")
    print_n_sleep("You beg for death and your howls of pain " +
                  "can be heard for miles...")


def death_outlines_some_options():
    print_n_sleep("*sigh* Every time...")
    print_n_sleep("Okay, here are your options:")

    responses = ['1', '2', '3']
    print_n_sleep("1.\tYou can sell me your soul, in return you'll get to " +
                  "live forever.")
    print_n_sleep("2.\tYou can guess how many fingers I'm holding up and " +
                  "just get on with your life.")
    print_n_sleep("3.\tYou can fight me for it.")

    response = ""
    while response not in responses:
        response = input("")
        if response in responses:
            if response == '1':
                we_sell_our_soul()
            elif response == '2':
                we_guess_finger_count()
            elif response == '3':
                print_n_sleep("A fatal mistake and before you know it Death " +
                              "takes you with a single swipe")
                death_takes_you()
            else:
                print_n_sleep("Please select an option between 1 and 3")


def death_understands():
    print_n_sleep("I know.")
    print_n_sleep("Once you realise that almost everybody is pretending to " +
                  "be something they're not...")
    print_n_sleep("...immitating each other...")
    print_n_sleep("very few with no vanity...")
    print_n_sleep("What do you do?")
    print_n_sleep("How do you live?")
    print_n_sleep("Nevertheless. By default you will go to hell.")

    responses = ['1', '2', '3']
    print_n_sleep("How do you respond?\n")

    print_n_sleep("1.\tHell?! Please! Help me!")
    print_n_sleep("2.\tVery well then...")
    print_n_sleep("3.\tNo!!! You're not taking me! I'm taking control!")

    response = ""
    while response not in responses:
        response = input("")
        if response in responses:
            if response == '1':
                death_outlines_some_options()
            elif response == '2':
                death_takes_you()
            elif response == '3':
                print_n_sleep("You can't. But you could gamble...")
                death_outlines_some_options()
            else:
                print_n_sleep("Please select an option between 1 and 3")


def death_introduces_the_deal():
    print_n_sleep("My name is Gustave Dore.")
    print_n_sleep("Your time has come. I bring a sythe to severe the last " +
                  "ties you have between body and soul.")
    print_n_sleep("Which way you go is now to be decided. I know all.")
    print_n_sleep("Let's see...")
    print_n_sleep("My God.")
    print_n_sleep("Your life.")
    print_n_sleep("Your life has been so boring.")
    print_n_sleep("Have you done nothing bad? Or even good? Have " +
                  "you done nothing!?")
    respond_to_deep_insult()


def respond_to_deep_insult():
    print_n_sleep("You feel insulted. How do you respond?")
    responses = ['1', '2', '3']

    print_n_sleep("1.\tHow dare you! It's hard to know what to do, you know?")
    print_n_sleep("2.\tMy God. You're right.")
    print_n_sleep("3.\tA second chance! Please!!!")

    response = ""
    while response not in responses:
        response = input("")
        if response in responses:
            if response == '1':
                print_n_sleep("You say 1")
                death_understands()
            elif response == '2':
                death_understands()
            elif response == '3':
                death_outlines_some_options()
            else:
                print_n_sleep("Please select an option between 1 and 3")


def death_approaches():
    responses = ['1', '2', '3']
    print_n_sleep("The figure moves towards you appearing to " +
                  "glide instead of walk.")
    print_n_sleep("You realise the figure has no face but carries a sythe.")
    print_n_sleep("It's your time, my child and I've come to collect.")
    print_n_sleep("How do you respond?\n")

    responseStrings = [
        "1.\tWho are you!? What do you want?!?!",
        "2.\tMy time, what do you mean? Get out of my house!",
        "3.\tYou reach for the phone to report an intruder."
    ]

    for response in responseStrings:
        print_n_sleep(response)

    response = ""
    while response not in responses:
        response = input("")
        if response not in responses:
            print_n_sleep("Please select an option between 1 and 3")

    print_n_sleep("The figure: I'm DEEEEAAAAAHEHEHEHEHEHEHTTTTTTTHHHH...")

    if response != '3':
        print_n_sleep("You: Sorry! I'll try to speak up!")
        print_n_sleep(responseStrings[
            int(response) - 1][3:].upper() + '!!!!!!!!')
    else:
        print_n_sleep("Your hand passes through the phone. Damn!")

    death_introduces_the_deal()


def initial_response():
    responses = ['1', '2', '3']

    print_n_sleep("How do you respond?\n")
    print_n_sleep("1.\tWho are you?! Show yourself!")
    print_n_sleep("2.\tYou roll across the bed to grab " +
                  "the baseball bat by the cabinet.")
    print_n_sleep("3.\tYou hide under the covers, cowering.")

    response = ""
    while response not in responses:
        response = input("")
        if response in responses:
            if response == '2':
                print_n_sleep("Your hand passes straight through the bat " +
                              "and you realise there's no escape.")
            elif response == '3':
                print_n_sleep("The little light that's around " +
                              "you gets darker.")
            death_approaches()
        else:
            print_n_sleep("Please select an option between 1 and 3")


playAgain = True
while playAgain:
    introduction()
    initial_response()

    print_n_sleep("GAME OVER. Play again? y/n")
    responses = ['y', 'n']

    response = ""
    while response.lower() not in responses:
        response = input("")
        if response.lower() == 'n':
            playAgain = False
        elif response.lower() == 'y':
            print("Sure thing!")
        else:
            print("Please only enter a y or n character as your response")
