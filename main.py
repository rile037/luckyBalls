## Lucky Balls v.1.0.
## By rile037

import random
import threading
import time

def numberPick():
    bet = input("- Enter your bet, please [currency $]: ")
    print("Your bet is: " + bet + " $")
    print("\n")
    print("INFO: Enter the numbers with white space (e.g. 1 23 40 37 12 5)")
    pickedNumbers = input("Enter six numbers, please [RANGE: 1 - 48]: ")
    print("\nINFO: 'xNumber' represents multiplication with your bet. \n- e.g. x50[win] * 50$[bet] = 2500$[reward]")
    print("\nYour numbers: \n")
    numbers = pickedNumbers.split(" ")
    for i in range(6):
        print("- " + numbers[i])
    return numbers

listOfChosenNumbers = numberPick()
numbers = []
t = 2.4


print(">>> Game begins!")

def pickNumber():
    number = random.randint(1, 48)
    return number


def countdown(t):
    """
    Countdown Timer
    """
    while t:
        mins, secs = divmod(t, 60)
        hours, mins = divmod(mins, 60)
        days, hours = divmod(hours, 24)
        timer = '{:02d}:{:02d}:{:02d}:{:02d}'.format(days, hours, mins, secs)
        time.sleep(1)
        t -= 1

    pickNumber()


win = 0
counter = 0


def choosingRandomNumbers():
    global counter
    global win
    global bet
    number = pickNumber()
    if len(numbers) == 35:
        print(">>> Winners, congratulations! ")
        print("\nDrawn numbers: \n" + str(numbers) + "\n")
        if win > 0:
            print(">>> WIN !!!! CONGRATULATION !!!! WIN <<<")
            print("Reward: x" + str(win))
            print("Bet: " + str(bet))
            reward = win * int(bet)
            print("- Your reward is: " + str(reward) + " $")
            print("\n")
            win = 0
        else:
            print("- You hit " + str(counter) + " out of 35 drawn numbers. Better luck next time!\n")
        x = 3

        for x in range(0, 15):
            countdown(1)
            print("- New game starts in ... ", 15 - x)
        print("\n")
        print("- New game is about to begin! Get ready!")
        countdown(3)
        counter = 0
        numbers.clear()
        choosingRandomNumbers()

    else:
        if number not in numbers:
            countdown(int(t))
            print("\n")
            numbers.append(number)
            lenght = len(numbers)
            if str(number) in listOfChosenNumbers:
                counter += 1
                print("- Number of drawn numbers you got: " + str(counter))

            match lenght:
                case 1:
                    print(str(number))
                    if counter == 6:
                        win = 250000
                        counter = 0
                case 2:
                    print(str(number))
                    if counter == 6:
                        win = 200000
                        counter = 0
                case 3:
                    print(str(number))
                    if counter == 6:
                        win = 150000
                        counter = 0
                case 4:
                    print(str(number))
                    if counter == 6:
                        win = 100000
                        counter = 0
                case 5:
                    print(str(number))
                    if counter == 6:
                        win = 50000
                        counter = 0
                case 6:
                    print(number, " x25000")
                    if counter == 6:
                        win = 25000
                        counter = 0
                case 7:
                    print(number, " x15000")
                    if counter == 6:
                        win = 15000
                        counter = 0
                case 8:
                    print(number, " x7500")
                    if counter == 6:
                        win = 7500
                        counter = 0
                case 9:
                    print(number, " x3000")
                    if counter == 6:
                        win = 3000
                        counter = 0
                case 10:
                    print(number, " x1250")
                    if counter == 6:
                        win = 1250
                        counter = 0
                case 11:

                    print(number, " x700")
                    if counter == 6:
                        win = 700
                        counter = 0
                case 12:
                    print(number, " x350")
                    if counter == 6:
                        win = 350
                        counter = 0
                case 13:
                    print(number, " x250")
                    if counter == 6:
                        win = 250
                        counter = 0
                case 14:
                    print(number, " x175")
                    if counter == 6:
                        win = 175
                        counter = 0
                case 15:
                    print(number, " x125")
                    if counter == 6:
                        win = 125
                        counter = 0
                case 16:
                    print(number, " x100")
                    if counter == 6:
                        win = 100
                        counter = 0
                case 17:
                    print(number, " x90")
                    if counter == 6:
                        win = 90
                        counter = 0
                case 18:
                    print(number, " x80")
                    if counter == 6:
                        win = 80
                        counter = 0
                case 19:
                    print(number, " x70")
                    if counter == 6:
                        win = 70
                        counter = 0
                case 20:
                    print(number, " x60")
                    if counter == 6:
                        win = 60
                        counter = 0
                case 21:
                    print(number, " x50")
                    if counter == 6:
                        win = 50
                        counter = 0
                case 22:
                    print(number, " x35")
                    if counter == 6:
                        win = 35
                        counter = 0
                case 23:
                    print(number, " x25")
                    if counter == 6:
                        win = 25
                        counter = 0
                case 24:
                    print(number, " x20")
                    if counter == 6:
                        win = 20
                        counter = 0
                case 25:
                    print(number, " x15")
                    if counter == 6:
                        win = 15
                        counter = 0
                case 26:
                    print(number, " x12")
                    if counter == 6:
                        win = 12
                        counter = 0
                case 27:
                    print(number, " x10")
                    if counter == 6:
                        win = 10
                        counter = 0
                case 28:
                    print(number, " x8")
                    if counter == 6:
                        win = 8
                        counter = 0
                case 29:
                    print(number, " x7")
                    if counter == 6:
                        win = 7
                        counter = 0
                case 30:
                    print(number, " x6")
                    if counter == 6:
                        win = 6
                        counter = 0
                case 31:
                    print(number, " x5")
                    if counter == 6:
                        win = 5
                        counter = 0
                case 32:
                    print(number, " x4")
                    if counter == 6:
                        win = 4
                        counter = 0
                case 33:
                    print(number, " x3")
                    if counter == 6:
                        win = 3
                        counter = 0
                case 34:
                    print(number, " x2")
                    if counter == 6:
                        win = 2
                        counter = 0
                case 35:
                    print(number, " x1")
                    if counter == 6:
                        win = 1
                        counter = 0


        else:
            pickNumber()
        threading.Timer(0.1, choosingRandomNumbers).start()
    return number


t1 = threading.Thread(target=numberPick, args="").start()
choosingRandomNumbers()

