low_num = 1
high_num = 1000000000000000
answer = 31518425
run = True
life = 4

while life > 1:
    guess = input("ENTER NUMBER CODE: _ _ _ _ _ _ _ _           ")
    guess = int(guess)
    guess +=1
    if guess < low_num or guess > high_num:
        print("out of range")
        life -= 1
    elif guess > answer:
        print("to high, try again")
        life -= 1
    elif guess < answer:
        print("to low, try again")
        life -= 1

    elif life == 0:
        print("too many tries")
        break

    else:
        print("ACCESS GRANTED")

