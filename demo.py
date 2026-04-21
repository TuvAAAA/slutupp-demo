


bag = []
max_items = 20

md1 = 1
part_1 = True

while part_1:
        
    while md1 ==1:
        print("dialog")
       
        choice = int(input("What do you wanna do first?     Go outside[1]      Check out your room[2]       Turn on the tv[3]       "))
        if choice == 1:
            input("AACK! You open the door and there seems to have been a massive flood during the night, luckly you live on a hill so it didn't take your house with you.")
            choice2 = int(input("what do you wanna do now?      Go back inside[1]       Figure out what happend[2]      "))
            while choice2 == 1:
                input("You go back inside but something in you wants to find out why there is so much water(also you might die of starvation). Then you see that you have an unred text from your friend: There has been a massive water rise, we're all gonna gather at the town upp on the mountain.")
                choice2 =- 1
                md1=md1-1

            while choice2 == 2:
                input("You decide to call some friends, nothing. You try the tv, nothing. And last you try the radio, only static noise. Then you see that you have an unred text from your friend: There has been a massive water rise, we're all gonna gather at the town upp on the mountain.")
                choice2 =-2
                md1=md1-1

        elif choice == 2:
            input("Nothing is out of the ordianry, your room is a bit messy tho.")
            #story

        elif choice == 3:
            input("You turn on the tv but its just static noise and a gray screen, seems like the signal isn't working.")
            #story

    
    input("You think back to the old kayak you had gotten on impuls and decide to check if you still have it")
    input("You do! thankfully it's also in a good condition. Now the only thing left to do is pack some recorces to bring with you")
    bagrun = True
   #bag, lägg till saker mm
    while bagrun:
        recorces = print("What do you wanna bring:         water, snacks, food, aidkit, patchkit, flashlight, batteries, emergency flare, ....")
        print("Add [A]")
        print("Remove [R]")
        print("Done [D]")
        print("Items [I]")
        choice = input("välj och skriv in:      ")
        if choice.lower()=="a":
            if len(bag)>=max_items:
                print("You're carring to much, try leaving some things behind")
            else:
                bag.append(input("write what you wanna bring:       "))
        elif choice.lower()=="r":
            item = input("what whould you like to remove")
            if item in bag:
                bag.remove(item)
                print(f"{item} har tagits bort")
            else:
                print(f"{item} doesn't exist in your inventory")

        elif choice.lower()=="d":
            bagrun = False
        elif choice.lower()=="i":
            print(bag)

    print("tjoho")
        
            
            


        





