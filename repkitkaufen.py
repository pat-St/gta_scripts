import time

import keyboard
import mouse

global stop
stop = True
counterLoop = 0


def warten():
    time.sleep(wartezeit)


def tankeöffnen():
    warten()
    keyboard.press('e')
    warten()
    keyboard.release('e')


def repkitkaufen():
    tankeöffnen()
    mouse.move(1016, 602, absolute=True)
    warten()
    counterLoop = 0
    while counterLoop < 10:
        print("klick")
        mouse.click('left')
        if stop == True:
            break
        time.sleep(0.53)
        counterLoop += 1
    print("fertig 10 stpck")
    warten()
    mouse.move(1270, 450, absolute=True)
    warten()
    mouse.click('left')
    warten()


def kanisterkaufen():
    tankeöffnen()
    mouse.move(1016, 602, absolute=True)
    warten()
    counterLoop = 0
    for i in range(choice_kanister):
        print("klick")
        mouse.click('left')
        if stop == True:
            break
        time.sleep(0.53)
        counterLoop += 1
    print("fertig 10 stpck")
    warten()
    mouse.move(1270, 450, absolute=True)
    warten()
    mouse.click('left')
    warten()


def kanisterdurchgänge():
    kanisterkaufen()
    warten()
    inventar()


def repkitdurchgänge():
    if choice == '1':
        print("loop 1")
        repkitkaufen()
        warten()
        inventar()
    elif choice == '2':
        print("loop 2")
        for i in range(2):
            print("test2")
            repkitkaufen()
        warten()
        inventar()
    elif choice == '3':
        print("loop 3")
        for i in range(3):
            print("test3")
            repkitkaufen()
        warten()
        inventar()
    elif choice == '4':
        print("test4")
        print("loop 4")
        for i in range(4):
            print("test4")
            repkitkaufen()
        warten()
        inventar()
    else:
        print("Ungültige Auswahl. Bitte wähle eine Option von 1 bis 4.")
        quit()


def inventar():
    print("inv")
    warten()
    keyboard.press('tab')
    warten()
    keyboard.release('tab')
    warten()
    # inventar 1 slot
    mouse.move(326, 250, absolute=True)
    warten()
    mouse.press('left')
    warten()
    # auto 1 slot
    mouse.move(1039, 430, absolute=1)
    warten()
    mouse.release('left')
    warten()
    keyboard.press('esc')
    warten()
    keyboard.release('esc')


def start_event():
    global stop
    stop = False
    print("Start")


def stop_event():
    global stop
    stop = True
    print("Wird Pausiert")


keyboard.add_hotkey('x', lambda: start_event())
keyboard.add_hotkey('e', lambda: stop_event())

print("")
selection = input("Kanister (y) oder Repkit (n):")
print("")

IS_REPKIT = False

if (len(selection) > 0) and (str(selection).lower() == 'y'):
    IS_REPKIT = True
    print("---------------------")
    print("Kanister Aktiviert")


else:
    IS_REPKIT = False
    print("---------------------")
    print("Repkit Aktiviert")


print("---------------------")
wartezeit = int(
    input("Gib die Wartezeit zwischen den Eingaben in Sekunden ein: "))
print("---------------------")
if IS_REPKIT == False:
    print("------------Repkits Ausgewählt------------")
    print(' 1 ausführung = 10 repkits:')
    print(' wähle zwischen 1 - 4 durchgänge ')
    print(" 1st Slot Inventar und Auto")
    print("")
    choice = input("Deine Auswahl: ")
    print("---------------------")
else:
    print("------------Kanister Ausgewählt------------")
    print(' 1 ausführung = 3 Kanister:')
    print(' wähle zwischen 1 - 4 durchgänge ')
    print(" 1st Slot Inventar und Auto")
    print("")
    choice_kanister = input("Deine Auswahl: ")
    print("---------------------")


while True:

    # warten bis eingabe dann start
    print("Zum Starten x drücken dund e zum Pausieren")
    while stop == True:
        time.sleep(2)

    while stop == False:
        warten()
        if stop == True:
            break

        if IS_REPKIT == False:
            repkitdurchgänge()
        else:
            kanisterdurchgänge()
        if stop == True:
            break
