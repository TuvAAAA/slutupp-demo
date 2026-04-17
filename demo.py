


bag = []
max_items = 20


part_1 = True

while part_1:
    print("dialog")

    choice = int(input("What do you wanna do first?     Go outside[1]      Check out your room[2]       Turn on the tv[3]       "))


    if choice == 1:
        input("AACK! You open the door and there seems to have been a massive flood during the night, luckly you live on a hill so it didn't take your house with you.")
        choice2 = int(input("what do you wanna do now?      Go back inside[1]       Figure out what happend[2]      "))
        while choice2 == 1:
            input("You go back inside but something in you wants to find out why there is so much water(also you might die of starvation). Then you see that you have an unred text from your friend: There has been a massive water rise, we're all gonna gather at the town upp on the mountain.")
            choice2 = choice2-1

        while choice2 == 2:
            input("You decide to call some friends, nothing. You try the tv, nothing. And last you try the radio, only static noise. Then you see that you have an unred text from your friend: There has been a massive water rise, we're all gonna gather at the town upp on the mountain.")
            choice2 = choice2 -2

        input("You think back to the old kayak you had gotten on impuls and decide och check if you still have it")
    


    elif choice == 2:
        input("Nothing is out of the ordianry, your room is a bit messy tho.")


    elif choice == 3:
        input("You turn on the tv but its just static noise and a gray screen, seems like the signal isn't working.")
