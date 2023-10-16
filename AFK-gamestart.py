import json
import os
import subprocess
import time
from pathlib import Path

import clipboard
import keyboard
import mouse
import numpy as np
import pyautogui
from PIL import ImageGrab


def log_to_file(message):
    with open('logfile.txt', 'a') as file:
        timestamp = time.strftime("%d.%m.%Y / %H:%M", time.localtime())
        log_message = f"{timestamp} - {message}\n"
        file.write(log_message)


def print_hour_and_minute():
    current_time = time.localtime()
    formatted_time = time.strftime("%d.%m.%Y / %H:%M", current_time)
    print(f"Aktuelles Datum, Stunde und Minute: {formatted_time} Uhr.")

### Überprüft ob ein Pixel im angegeben Farbraum ist
## inputPixel = [R,G,B] ; Der pixel der überprüft wird
## minPixelRange = [R,G,B] ; Der pixel darf nicht unterschreiten
## maxPixelRange = [R,G,B] ; Der pixel darf nicht überschreiten
## Return: True wenn in Range, ansonsten False
def inColorRange(inputPixel,minPixelRange,maxPixelRange):
    for pos in range(3):
        # Erster Fall, zu niedrig
        if inputPixel[pos] < minPixelRange[pos]:
            return False
        # Zweiter Fall, zu hoch
        if inputPixel[pos] > maxPixelRange[pos]:
            return False
    return True


class GamesSaveState:
    def __init__(self,password = '',path = ''):
        self.password = password
        self.path = path
        self.create()

    def read_password(self):
        return self.password
    
    def read_path(self):
        return self.path
    
    def write_password(self, password):
        self.password = password
    
    def write_path(self, path):
        self.path = path

    def paste_password(self):
        keyboard.wait("ctrl+v")
        new_password = clipboard.paste()
        self.write_password(new_password)

    def paste_path(self):
        keyboard.wait("ctrl+v")
        new_path = clipboard.paste().strip('"')  # Entfernt Anführungszeichen, wenn sie vorhanden sind
        self.write_path(new_path)

    def password_empty(self):
        return len(self.password) == 0
    
    def path_empty(self):
        return len(self.path) == 0
    
    def create(self):
        if not os.path.exists(self.config_path()):
            os.makedirs(self.config_path())
        if not os.path.exists(self.config_file()):
            self.save()
        self.read()

    def write_data(self):
        return {
            "password": self.password,
            "path": self.path
        }

    def save(self):
        with open(self.config_file(), "+w") as file:
                json.dump(self.write_data(), file)

    def read(self):
        with open(self.config_file(), "r") as file:
            tmp = json.load(file)
            self.password = str(tmp['password'])
            self.path = str(tmp['path'])
    
    def config_path(self):
        return os.path.join(os.getenv('APPDATA'),'grand_afk_game_start')

    def config_file(self):
        return os.path.join(self.config_path(),'config.json')

def prepare() -> GamesSaveState:
    speicherZustand = GamesSaveState()
    if speicherZustand.password_empty():
        # new_password = input("Bitte geben Sie ein neues Passwort ein: ")
        print("Bitte schreiben Sie ein Password ein oder (mit STRG+V): ")
        # speicherZustand.write_password(new_password)
        speicherZustand.paste_password()

    if speicherZustand.path_empty():
        # new_path = input("Bitte geben Sie den Pfad ein: ")
        # speicherZustand.write_path(new_path)
        print("Bitte schreiben Sie den Pfad zur .exe-Datei ein oder (mit STRG+V): ")
        speicherZustand.paste_path()

    speicherZustand.save()
    return speicherZustand

def password():

    print("Password eingabe wurde erkannt.")
    pyautogui.moveTo(562,566,duration=0.5)
    time.sleep(4)
    mouse.click('left')
    print("Password wird eingegeben.")
    time.sleep(4)
    # keyboard.write('HIER PASSWORD EINGEBEN') # hier password eingeben
    
    keyboard.write(speicherZustand.read_password())
    time.sleep(4)
    print("Accoount wird eingeloggt.")
    pyautogui.moveTo(651,678,duration=0.5)
    time.sleep(4)
    mouse.click('left')
    print("Login Fertig.")

def pixelabfrage(game_coords):
    screenshot = ImageGrab.grab(
        bbox=game_coords, include_layered_windows=True, all_screens=True)
    erkennung = np.array(screenshot)
    # print(str(screenshot))
    xlen = len(erkennung)
    ylen = len(erkennung[0])

    # print("x:" + str(xlen) + " y:" + str(ylen))
    midX = xlen // 2
    midY = ylen // 2
    return  erkennung[midX, midY]

def ispasswordabfrage():
    pixel = pixelabfrage([1410, 600, 1416, 610])
    minColor = [237, 60, 86] # Minimun farbe range
    maxColor = [245, 64, 91] # Maximum farbe range
    if inColorRange(pixel,minColor,maxColor):
        log_to_file(f"Password eingabe erkannt. R:G:B {pixel}")
        return True
    log_to_file(f"keine Password eingabe erkannt. R:G:B {pixel}")
    return False

def isSpielAn():
    pixel = pixelabfrage([1870, 50, 1880, 55])
    minColor = [249, 227, 52]
    maxColor = [255, 234, 58] # Maximum farbe range
    if inColorRange(pixel,minColor,maxColor):
        log_to_file(f"Gelbe 1 erkannt. R:G:B {pixel}")
        return True
    log_to_file(f"Gelbe 1 nicht erkannt. R:G:B {pixel}")
    return False

def istgrandcoinssliderda():
    pixel = pixelabfrage([950, 920, 960, 930])
    minColor = [239, 184, 36]
    maxColor = [245, 188, 40] # Maximum farbe range
    if inColorRange(pixel,minColor,maxColor):
        log_to_file(f"grand coins slider erkannt. R:G:B {pixel}")
        return True
    log_to_file(f"Grandcoin slider nicht erkannt. R:G:B {pixel}")
    return False

def IsServerFull():
    pixel = pixelabfrage([1410, 600, 1416, 610])
    minColor = [237, 60, 86] # Minimun farbe range
    maxColor = [245, 64, 91] # Maximum farbe range
    if inColorRange(pixel,minColor,maxColor):
        log_to_file(f"Server Full. R:G:B {pixel}")
        return True
    log_to_file(f"Server nicht Full. R:G:B {pixel}")
    return False

def SpielBeenden():
    print("Alle programme werden beendet.")
    log_to_file("Alle programme werden Beendet")
    print_hour_and_minute()
    os.system("taskkill /f /im GTA5.exe")
    time.sleep(5)
    os.system("taskkill /f /im Launcher.exe")
    time.sleep(5)
    os.system("taskkill /f /im LauncherPatcher.exe")
    time.sleep(5)
    os.system("taskkill /f /im ragemp_v.exe")
    time.sleep(5)
    os.system("taskkill /f /im PlayGTAV.exe")
    time.sleep(5)
    os.system("taskkill /f /im updater.exe")

def startding():
    log_to_file("RageMP wird gestart")
    print("Rage wird gestarted.")
    print_hour_and_minute()
    start_path = speicherZustand.read_path()
    start_cmd = "start \"RageMp\" /d C:\\RAGEMP {execution_path}".format(execution_path=start_path)
    os.system(start_cmd) 
    # os.system("switch.bat \"RageMp\"") 

def RageMPconnenct():
    log_to_file("Ragemp Connect")
    print("Auf Grand connecten.")
    print_hour_and_minute()
    pyautogui.moveTo(1357,217,duration=0.5)
    time.sleep(5)
    mouse.click('left')
    time.sleep(5)
    pyautogui.moveTo(864,557,duration=0.5)
    time.sleep(5)
    mouse.click('left')
    mouse.click('left')
    mouse.click('left')
    time.sleep(5)
    keyboard.write("de.gta5grand.com")
    pyautogui.moveTo(1146,563,duration=0.5)
    time.sleep(5)
    mouse.click('left')

def SpawnPunkt():
    log_to_file("Wird bei familie gespawnt")
    print("Spawnpunkt am Familienhaus wird ausgewählt.")
    print_hour_and_minute()
    pyautogui.moveTo(197,595,duration=0.5)
    time.sleep(10)
    mouse.click('left')

def PressA():
    keyboard.press('a')
    time.sleep(0.1)
    keyboard.release('a')
    print("A wird gedrückt")

def PressD():
    keyboard.press('d')
    time.sleep(0.1)
    keyboard.release('d')
    print("D wird gedrückt")

def PressW():
    keyboard.press('w')
    time.sleep(0.1)
    keyboard.release('w')   
    print("W wird gedrückt") 

def warten():
    print("10 Sekunden Pause")
    time.sleep(10)

def GrandCoinSlider20hours():
    # investion moven und klicken
    if istgrandcoinssliderda():
        log_to_file("Grand coin slider erkannt")
        print("Grand Coins erkannt")
        pyautogui.moveTo(950, 804,duration=0.5)# auf dem slider ziehen
        time.sleep(3)
        pyautogui.dragTo(956, 329, 1, button='left') # 
        time.sleep(3)
        pyautogui.moveTo(938, 941) # auf fertig drücken
        time.sleep(3)
        mouse.click('left')

def escbis20sdtSlider():
    for x in range(10): 
        if not istgrandcoinssliderda():
            log_to_file("Kein grandcoin slider erkannt")
            print("Esc bis Grandcoinslider")
            print_hour_and_minute()
            keyboard.press_and_release('esc')
            time.sleep(2)
        else:
            print_hour_and_minute()
            break

def Investion8Stunden():
    print("Investion 8 Stunden wird angenommen")
    log_to_file("8 Stunden invest wird angenommen")
    # handy rausholen
    time.sleep(1)
    keyboard.press_and_release('k')
    time.sleep(3)
    # investion moven und klicken
    pyautogui.moveTo(1713, 1009,duration=0.5)
    time.sleep(3)
    mouse.click('left')
    time.sleep(3)
    # auf tagsüber moven und klicken
    pyautogui.moveTo(94, 537,duration=0.5)
    time.sleep(3)
    mouse.click('left')
    time.sleep(3)
    # scrollbar moven und klicken
    pyautogui.moveTo(1608, 965,duration=0.5)
    time.sleep(3)
    mouse.click('left')
    time.sleep(1)
    mouse.click('left')
    time.sleep(3)
    # 8 stunden invest 
    pyautogui.moveTo(1451, 866,duration=0.5)
    time.sleep(3)
    mouse.click('left')
    time.sleep(3)
    # annhemen
    pyautogui.moveTo(877, 725,duration=0.5)
    time.sleep(3)
    mouse.click('left')
    time.sleep(3)
    # rausgeben
    keyboard.press_and_release('esc')

def FamAufgabe4Stunden():
    print("Familienaufgabe 4 Stunden wird angenommen")
    log_to_file("Familienaufgabe 4 Stunden wird angenommen")

    # Familienaufgabe annhemen
    time.sleep(1)
    keyboard.press_and_release('m')
    time.sleep(3)
    # auf familie moven
    pyautogui.moveTo(1087, 866,duration=0.5)
    time.sleep(3)
    mouse.click('left')
    time.sleep(3)
    # familien aufgabe
    pyautogui.moveTo(156, 685,duration=0.5)
    time.sleep(3)
    mouse.click('left')
    time.sleep(3)
    # Scrollbar
    pyautogui.moveTo(1510, 1051,duration=0.5)
    time.sleep(3)
    mouse.click('left')
    time.sleep(3)
    # 4 stunden aufgabe annhemen
    pyautogui.moveTo(617, 994,duration=0.5)
    time.sleep(3)
    mouse.click('left')

global stop
stop = True

def start_event():
    global stop
    stop = False
    print("Start")
    log_to_file("AFK Bot Programm start mit q taste")

def stop_event():
    global stop
    stop = True
    print("Wird Pausiert")
    log_to_file("AFK Bot Programm stop mit e taste")

keyboard.add_hotkey('q', lambda: start_event())
keyboard.add_hotkey('e', lambda: stop_event())

def istImZeitraum(start_time=(0,0),end_time=(0,0)):
    systemzeit = time.localtime()
    st = time.localtime()
    from_start = time.struct_time(
        (st.tm_year,)
        + (st.tm_mon,)
        + (st.tm_mday,)
        + (start_time[0],)
        + (start_time[1],)
        + (0,)
        + (st.tm_wday,)
        + (st.tm_yday,)
        + (st.tm_isdst,)
    )
    to_end = time.struct_time(
        (st.tm_year,)
        + (st.tm_mon,)
        + (st.tm_mday,)
        + (end_time[0],)
        + (end_time[1],)
        + (0,)
        + (st.tm_wday,)
        + (st.tm_yday,)
        + (st.tm_isdst,)
    )
    # print(time.strftime("%H:%M:%S", systemzeit))
    # print(time.strftime("%H:%M:%S", from_start))
    # print(time.strftime("%H:%M:%S", to_end))
    if time.mktime(systemzeit) < time.mktime(from_start):
        # zu früh
        return False
    if time.mktime(systemzeit) > time.mktime(to_end):
        # zu spät
        return False
    return True

def solangeSpielAktivIst():
    print_hour_and_minute()
    while isSpielAn():
            print_hour_and_minute()
            log_to_file("Ist im Spiel")
            print("Spiel erkannt")
            PressA()
            warten()
            PressD()
            warten()
            PressW()

            # Tagesinvest
            if istImZeitraum((5,1),(5,3)):
                log_to_file("5 Uhr Invest und Fam")
                Investion8Stunden()
                print_hour_and_minute()
                FamAufgabe4Stunden()
                print_hour_and_minute()
                time.sleep(300)
                escbisspielbeginn()

            # 4 Uhr neustart
            if istImZeitraum((4,0),(4,2)):
                log_to_file("4 Uhr Server Neustart")
                print_hour_and_minute()
                SpielBeenden()
                time.sleep(300)
                escbisspielbeginn()

def escbisspielbeginn():
    for x in range(10): 
        if not isSpielAn():
            log_to_file("ESC bis im spiel")
            print_hour_and_minute()
            print("ESC bis im zum AFK Botten")
            keyboard.press_and_release('esc')
            time.sleep(2)
        else:
            print_hour_and_minute()
            break

def IstServerFull():
    for v in range(15):
        if IsServerFull():
            log_to_file("Server Full erneut login")
            print_hour_and_minute()
            print("Server ist überfüllt. Erneuter Login wird durchgeführt.")
            time.sleep(10)
            pyautogui.moveTo(651,678,duration=0.5)
            time.sleep(4)
            mouse.click('left')
        else:
            print_hour_and_minute()
            break
            
        time.sleep(0.5)


def loginfertig():
    for y in range(300): 
        print("Warte auf login screen")
        print_hour_and_minute()
       
        if ispasswordabfrage():
            print("Password eingabe erkannt")
            print_hour_and_minute()
            time.sleep(5)
            password()
            IstServerFull()
            time.sleep(5)
            SpawnPunkt()
            time.sleep(5)
            escbis20sdtSlider()
            time.sleep(5)
            GrandCoinSlider20hours()
            time.sleep(5)
            escbisspielbeginn()
            time.sleep(5)
            break
        time.sleep(1)

speicherZustand = prepare()

while True:    
    # warten bis eingabe dann start
    print("Zum Starten q drücken und e zum Pausieren.")
    while stop == True:
        time.sleep(1)
        # print("warten")

    while stop == False:
        solangeSpielAktivIst()
        time.sleep(5)          
        SpielBeenden()       
        time.sleep(5)   
        startding()
        time.sleep(5)     
        RageMPconnenct()
        print("Warten 300 Sekunden.")
        time.sleep(300)
        print("Fertig mit warten, login wird abgefragt.")
        # # 240 Sekunden warten bis er grün erkennt dann spawn def ausführen, wenn nicht neustart.
        loginfertig()
        time.sleep(5)



    
       