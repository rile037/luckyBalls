## Lucky Six v.0.1.
## By rile037

import random
import threading
import time
import tkinter

root = tkinter.Tk()
root.title("Lucky Balls v1.0 ")
root.geometry("500x500")

root.mainloop()
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


ulog = 0


def biranjeBrojeva():
    global ulog
    ulog = input("Unesite vas ulog (iznos upisujete u dinarima, npr. 200): ")
    print("Vas ulog: " + ulog + " rsd")
    print("Brojeve unosite sa razmakom (npr. 1 23 40 37 12 5)")
    izabraniBrojevi = input("Unesite 6 brojeva [1 - 48]: ")
    print("\nVasi brojevi: \n")
    brojevi = izabraniBrojevi.split(" ")
    for i in range(6):
        print("- " + brojevi[i])
    return brojevi



listaIzabranihBrojeva = biranjeBrojeva()

print(">>> Izvlacenje pocinje!")
##35
brojevi = []
t = 1


def izaberiBroj():
    broj = random.randint(1, 48)
    return broj


def countdown(t):
    """
    Countdown Timer
    """
    while t:
        # Divmod takes only two arguments so
        # you'll need to do this for each time
        # unit you need to add
        mins, secs = divmod(t, 60)
        hours, mins = divmod(mins, 60)
        days, hours = divmod(hours, 24)
        timer = '{:02d}:{:02d}:{:02d}:{:02d}'.format(days, hours, mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    izaberiBroj()


win = 0
brojac = 0


def ubacivanjeBrojevaUBubanj():
    global brojac
    global win
    global ulog
    broj = izaberiBroj()
    if len(brojevi) == 35:
        print(">>> Cestitamo pobednicima! ")
        print("\nIzvuceni brojevi: \n" + str(brojevi) + "\n")
        if win > 0:
            print(">>> WIN !!!! Cestitamo !!!! WIN <<<")
            print("Dobitak: x" + str(win))
            print("Ulog: " + str(ulog))
            dobitak = win * int(ulog)
            print("- Vas dobitak: " + str(dobitak) + " rsd")
            print("\n")
            win = 0
        else:
            print("- Pogodili ste " + str(brojac) + " od ukupno 35 izvucenih brojeva. Vise srece drugi put!\n")
        x = 3

        for x in range(0, 3):
            countdown(1)
            print("- Novo kolo pocinje za ", 3 - x)
        print("\n")
        print("- Novo kolo pocinje!")
        countdown(3)
        brojac = 0
        brojevi.clear()
        ubacivanjeBrojevaUBubanj()

    else:
        if broj not in brojevi:
            countdown(int(t))
            print("\n")
            brojevi.append(broj)
            duzina = len(brojevi)
            if str(broj) in listaIzabranihBrojeva:
                brojac += 1
                print("- Broj pogodjenih brojeva: " + str(brojac))

            match duzina:
                case 1:
                    print("Bubanj: " + str(broj))
                    if brojac == 6:
                        win = 250000
                        brojac = 0
                case 2:
                    print("Bubanj: " + str(broj))
                    if brojac == 6:
                        win = 200000
                        brojac = 0
                case 3:
                    print("Bubanj: " + str(broj))
                    if brojac == 6:
                        win = 150000
                        brojac = 0
                case 4:
                    print("Bubanj: " + str(broj))
                    if brojac == 6:
                        win = 100000
                        brojac = 0
                case 5:
                    print("Bubanj: " + str(broj))
                    if brojac == 6:
                        win = 50000
                        brojac = 0
                case 6:
                    print(broj, " x25000")
                    if brojac == 6:
                        win = 25000
                        brojac = 0
                case 7:
                    print(broj, " x15000")
                    if brojac == 6:
                        win = 15000
                        brojac = 0
                case 8:
                    print(broj, " x7500")
                    if brojac == 6:
                        win = 7500
                        brojac = 0
                case 9:
                    print(broj, " x3000")
                    if brojac == 6:
                        win = 3000
                        brojac = 0
                case 10:
                    print(broj, " x1250")
                    if brojac == 6:
                        win = 1250
                        brojac = 0
                case 11:

                    print(broj, " x700")
                    if brojac == 6:
                        win = 700
                        brojac = 0
                case 12:
                    print(broj, " x350")
                    if brojac == 6:
                        win = 350
                        brojac = 0
                case 13:
                    print(broj, " x250")
                    if brojac == 6:
                        win = 250
                        brojac = 0
                case 14:
                    print(broj, " x175")
                    if brojac == 6:
                        win = 175
                        brojac = 0
                case 15:
                    print(broj, " x125")
                    if brojac == 6:
                        win = 125
                        brojac = 0
                case 16:
                    print(broj, " x100")
                    if brojac == 6:
                        win = 100
                        brojac = 0
                case 17:
                    print(broj, " x90")
                    if brojac == 6:
                        win = 90
                        brojac = 0
                case 18:
                    print(broj, " x80")
                    if brojac == 6:
                        win = 80
                        brojac = 0
                case 19:
                    print(broj, " x70")
                    if brojac == 6:
                        win = 70
                        brojac = 0
                case 20:
                    print(broj, " x60")
                    if brojac == 6:
                        win = 60
                        brojac = 0
                case 21:
                    print(broj, " x50")
                    if brojac == 6:
                        win = 50
                        brojac = 0
                case 22:
                    print(broj, " x35")
                    if brojac == 6:
                        win = 35
                        brojac = 0
                case 23:
                    print(broj, " x25")
                    if brojac == 6:
                        win = 25
                        brojac = 0
                case 24:
                    print(broj, " x20")
                    if brojac == 6:
                        win = 20
                        brojac = 0
                case 25:
                    print(broj, " x15")
                    if brojac == 6:
                        win = 15
                        brojac = 0
                case 26:
                    print(broj, " x12")
                    if brojac == 6:
                        win = 12
                        brojac = 0
                case 27:
                    print(broj, " x10")
                    if brojac == 6:
                        win = 10
                        brojac = 0
                case 28:
                    print(broj, " x8")
                    if brojac == 6:
                        win = 8
                        brojac = 0
                case 29:
                    print(broj, " x7")
                    if brojac == 6:
                        win = 7
                        brojac = 0
                case 30:
                    print(broj, " x6")
                    if brojac == 6:
                        win = 6
                        brojac = 0
                case 31:
                    print(broj, " x5")
                    if brojac == 6:
                        win = 5
                        brojac = 0
                case 32:
                    print(broj, " x4")
                    if brojac == 6:
                        win = 4
                        brojac = 0
                case 33:
                    print(broj, " x3")
                    if brojac == 6:
                        win = 3
                        brojac = 0
                case 34:
                    print(broj, " x2")
                    if brojac == 6:
                        win = 2
                        brojac = 0
                case 35:
                    print(broj, " x1")
                    if brojac == 6:
                        win = 1
                        brojac = 0


        else:
            izaberiBroj()
        threading.Timer(0.1, ubacivanjeBrojevaUBubanj).start()
    return broj


ubacivanjeBrojevaUBubanj()