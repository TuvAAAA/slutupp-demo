

while True:
    

    x = "cordyceps"
    def check_place(char_g, char_w,place):
        if char_g == char_w:
            print(place + "letter: right letter, right place!")
    guess = input("enter a word:  ")
    while (len(guess) !=9):
               print("that's not a nine letter word")
               guess=input("enter a word:  ")
    for i in range(9):
        if guess == x:
             print("welcome")
             break
        
        check_place(guess[0],x[0], "first")
        if guess[0] == x[1] or guess[0] == x[2] or guess[0] == x[3] or guess[0] ==x[4] or guess[0] ==x[5] or guess[0] ==x[6] or guess[0] ==x[7] or guess[0] ==x[8]:
            print("firstletter: right letter, worng place.")
        
        
        check_place(guess[1],x[1], "second")
        if guess[1] == x[0] or guess[1] == x[2] or guess[1] == x[3] or guess[1] ==x[4] or guess[1] ==x[5] or guess[1] ==x[6] or guess[1] ==x[7] or guess[1] ==x[8]:
            print("firstletter: right letter, worng place.")

        
        
        check_place(guess[2],x[2], "third")
        if guess[2] == x[0] or guess[2] == x[1] or guess[2] == x[3] or guess[2] ==x[4] or guess[2] ==x[5] or guess[2] ==x[6] or guess[2] ==x[7] or guess[2] ==x[8]:
            print("firstletter: right letter, worng place.")

        
        
        check_place(guess[3],x[3], "fourth")
        if guess[3] == x[0] or guess[3] == x[1] or guess[3] == x[2] or guess[3] ==x[4] or guess[3] ==x[5] or guess[3] ==x[6] or guess[3] ==x[7] or guess[3] ==x[8]:
            print("firstletter: right letter, worng place.")

        
        
        check_place(guess[4],x[4], "fifth")
        if guess[4] == x[0] or guess[4] == x[1] or guess[4] == x[2] or guess[4] ==x[3] or guess[4] ==x[5] or guess[4] ==x[6] or guess[4] ==x[7] or guess[4] ==x[8]:
            print("firstletter: right letter, worng place.")

        
        
        check_place(guess[5],x[5], "sixth")
        if guess[5] == x[0] or guess[5] == x[1] or guess[5] == x[2] or guess[5] ==x[3] or guess[5] ==x[4] or guess[5] ==x[6] or guess[5] ==x[7] or guess[5] ==x[8]:
            print("firstletter: right letter, worng place.")

        
        
        check_place(guess[6],x[6], "seventh")
        if guess[6] == x[0] or guess[6] == x[1] or guess[6] == x[2] or guess[6] ==x[3] or guess[6] ==x[4] or guess[6] ==x[5] or guess[6] ==x[7] or guess[7] ==x[8]:
            print("firstletter: right letter, worng place.")


        
        
        check_place(guess[7],x[7], "eight")
        if guess[7] == x[0] or guess[7] == x[1] or guess[7] == x[2] or guess[7] ==x[4] or guess[7] ==x[4] or guess[7] ==x[5] or guess[7] ==x[6] or guess[7] ==x[8]:
            print("firstletter: right letter, worng place.")

        
        check_place(guess[8],x[8], "ninth")
        if guess[8] == x[0] or guess[8] == x[1] or guess[8] == x[2] or guess[8] ==x[4] or guess[8] ==x[4] or guess[8] ==x[5] or guess[8] ==x[6] or guess[8] ==x[7]:
            print("firstletter: right letter, worng place.")


    if guess !=x:
         print("passowrd inccorect to many times")
         break
    else:
         print("incorrect, try again")
        














