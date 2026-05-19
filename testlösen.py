run = True

word="hej"




while run == True:
    correct = "_ _ _"
    
    guess = input("skriv ett ord med 3 bokstäver      ")
    if len(guess) == 3:
        if word[0] == guess[0]:
            correct[0]


    if correct == word:
        print("you got it")
        break

