

from random import randint

word_list= ["cordyceps"]
lock = 5
word = list(word_list[(0,len(word_list)- 1)])
guessed_password = [""]*len(word)
guessed_letters = []


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
            while choice ==2:
                input("You notice your phone lighting up and see that you have a text message from you friend that reads: There has been a massive water rise, we're all gonna gather at the town upp on the mountain.")
                input("you wonder how youd get there now that there have been a massive water rise.")
                choice =-2
                md1=md1-1
            #story

        elif choice == 3:
            input("You turn on the tv but its just static noise and a gray screen, seems like the signal isn't working.")
            while choice ==3:
                input("You notice a text message from your friend that reads: There has been a massive water rise, we're all gonna gather at the town upp on the mountain.")
                input("you wonder how youd get there now that there have been a massive water rise.")
                choice =-3
                md1=md1-1
            #story

    
    input("You think back to the old kayak you had gotten on impuls and decide to check if you still have it")
    input("You do! thankfully it's also in a good condition. Now the only thing left to do is pack some recorces to bring with you")
    bagrun = True
   #bag, lägg till saker mm

    #göra så att man alltid har access till sin bag
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

    input("Great now you have some stuff on your journey")
    input("You get into your kayak with your stuff and start to paddle towards the moutain")
    way = int(input("The quote on quote road turns into three sections all leading to the moutain, which do you take:     Forest[1]       Open[2]     City[3]      "))
    if way ==1:
        input("You decide to take the forest path and admire how it looked even though this feel kinda scary")
        input("it's really quiet, too quiet, before you see something move in the distance")

    if way ==2:
        w

    if way ==3:
        
        input("You decide to go the city way to see the wreckage that the flood had caused")
        input("You continue calm rowing and suddely you see something floating in the need distance, you go towards it, pick it up and see it was some sort of laptop.")
        
        

        while lock>1:
            input("you open it upp and somehow it starts upp and not being water damaged, it loads a little bit before it shows: ENTER PASSWORD     ")
            input("it was a 9 letter combination, it couldn't be that hard right?")
            letters = input("ENTER PASSWORD")
            list(letters)
            for l in letters:
                



        
            
            


        





