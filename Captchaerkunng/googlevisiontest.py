import re

import auswahl_erkenner
from google.cloud import vision_v1
from google.cloud.vision_v1 import types


def recognize_text_google_cloud(image_path, api_key_path):
    client = vision_v1.ImageAnnotatorClient.from_service_account_file(api_key_path)

    with open(image_path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations

    if texts:
        return texts[0].description
    else:
        return "Text nicht erkannt"
    
    
def text_to_numbers(input:str):
    foundmatches_number = re.finditer("\w+[^\W]{1}", input)
    foundmatches_operator = re.search("[\\+|\\-|\\*|\\:|\/]", input)
    # print(each)
    
    zahlenfolge = []    
    for each in foundmatches_number:
        
        match each.group():
            case "NULL":
                    zahlenfolge.append(0)
            case "EINS":
                    zahlenfolge.append(1)
            case "ZWEI":
                    zahlenfolge.append(2)
            case "DREI":
                    zahlenfolge.append(3)
            case "VIER":
                    zahlenfolge.append(4)
            case "FÜNF":
                    zahlenfolge.append(5)
            case "SECHS":
                    zahlenfolge.append(6)
            case "SIEBEN":
                    zahlenfolge.append(7)
            case "ACHT":
                    zahlenfolge.append(8)
            case "NEUN":
                    zahlenfolge.append(9)
            case "ZEHN":
                    zahlenfolge.append(10)
    print(str(zahlenfolge))
    summe = 0
    
    for index, zahl in enumerate(zahlenfolge):
        if index == 0:
            summe = zahl
        else:
            
            match foundmatches_operator.group():
                case "+":
                        summe = summe + zahl
                case "-":
                        summe = summe - zahl
                case ":":
                        summe = summe / zahl
                case "/":
                        summe = summe / zahl        
                case "*":
                        summe = summe * zahl
    return summe

def text_to_list(input:str):
    foundmatches_number = re.finditer("\w+[^\W]{1}", input)
    foundmatches_operator = re.search("[\\+|\\-|\\*|\\:|\/]", input)

    ergebnis = [] # TODO: implementieren
    # Filter alle Zeichen raus. Nur noch Zahlen
    # Zahlen in ergebnis appenden (hinzufügen)
    # print(ergebnis)  --> [ 13, 6, 9, 10, 7] 
    return ergebnis

if __name__ == "__main__":
    image_path = "C:/Users/lukas/Pictures/Captchabilder/klein.png"  # Ihr Pfad hier
    api_key_path = "D:/Wichtige sachen/repo/gta_scripts/Captchaerkunng/peppy-aileron-411511-017c4287b754.json"
    auswahl_bild = "D:/Wichtige sachen/repo/gta_scripts/Captchaerkunng/image.png"
    # recognized_text = recognize_text_google_cloud(image_path, api_key_path)
    recognized_text = "ACHT+VIER = ?"

    print("Erkannter Text:")
    print(recognized_text)
    ergebnis = text_to_numbers(recognized_text)
    print(ergebnis)

#     auswahl_zahlen_liste = auswahl_erkenner.get_auswahl(print_file=True)
#     auswahl_list_als_text = recognize_text_google_cloud(auswahl_bild, api_key_path)
    auswahl_list_als_text = "13 + 6 + 9 + 10 + 7"
    zahlen_in_liste = text_to_list(input=auswahl_list_als_text)
    print(auswahl_list_als_text)
