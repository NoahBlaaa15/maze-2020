#MAZE 2020 MAIN

#IMPORTS
import sys
import datetime
import builtins

orig_stdout = sys.stdout                                                                        #Standardausgabestream speichern
log = open('log.txt', 'w')                                                                      #Logdatei öffnen
sys.stdout = log                                                                                #In diese schreiben

println = builtins.print                                                                        #Alte Methode sichern
def print(*args, **kwargs):                                                                     #Eigene Print Methode mit timestamps
    builtins.print(str(datetime.datetime.now()).split('.')[0], end = ": ")                      #Vor jedem Print wird der Timestamp gesetzt
    builtins.print(*args, **kwargs)                                                             #Normales Print der Nachricht

print("**********")
print("Log file openend")
print("**********")

import maze_serial as m_ser
import tile
import wall
import arduinodata
import history
import stack

#SETUP
m_ser.start
print("Serial Kommunikation gestartet")

kachel = tile.Tile(None, None, None, None)
print("Initialkachel erstellt")

kachel.set_coordinates(0, 0, 0)
print("Initialkachel auf 0, 0, 0 gesetzt")

aktueller_raum = kachel
print("Raum von Kachel zu aktueller_raum verschoben")

tasks = stack.Stack()
print("Stack initialisiert")

#ACTION
while True:
    m_ser.send('pls#')
    print("Daten von Arduino angefragt")
    data = m_ser.receive()
    print("Daten von Arduino empfangen")
    
    data = arduinodata.decode(data)
    print("Empfangene Daten entpackt: ")
    print(data)
    wallsdata, victimsdata, environmentdata, motorsdata = arduinodata.analyze(data, 'all')
    print("Entpackte Daten analysiert")
    for i in wallsdata:
        print(i, wallsdata[i])
    for i in victimsdata:
        print(i, victimsdata[i])
    for i in environmentdata:
        print(i, environmentdata[i])
    for i in motorsdata:
        print(i, motorsdata[i])
    #kameradaten jetzt auch analysieren
    
    if environmentdata[floor] == 'black':
        print("Schwarze Platte")
        aktueller_raum.set_type('black')
        print("Typ geändert")
        aktueller_raum.set_top(wall.Wall())
        print("OBEN ABGERIEGELT")
        aktueller_raum.set_rgt(wall.Wall())
        print("RECHTS ABGERIEGELT")
        aktueller_raum.set_but(wall.Wall())
        print("UNTEN ABGERIEGELT")
        aktueller_raum.set_lft(wall.Wall())
        print("LINKS ABGERIEGELT")
        
        tasks.add(history.get_last_tile())
        print("Runterfahren auf den Stack gepackt")
        print(tasks)
        print(tasks.all())
        #zum fahren springen
        
    #rampe? -> rampenbefahrungsmodus
    #gibts undefinierte räume drumherum? -> erstellen und wände je nach WALLSDATA setzen
        #wenn keine wand da und unbefahren -> da hinfahren auf stack drauf
    #irgendwelche opfer hier? -> wände dementsprechend modifizieren/checken und wenn noch nicht gerettet kits abwerfen
    #checkpoint? -> letzter checkpoint variable aktualisieren
    
    try:
       task_to_do = tasks.get()                                                                 #Probieren eine Aufgabe zu nehmen
    except:
        sys.stdout = orig_stdout
        f.close()
        #Lauf beenden
    #genommene aufgabe entschlüsseln
    #genaue fahranweisung an arduino senden
    #Fotos machen mit ~15 FPS
    #auf bestätigung warten
    #Nach Bestätigung fotos stoppen
    #Objekterkennung starten
    #passen rotationswerte etc? -> sonst anpassungsbefehl schicken
    #letzte fahrt in history modul updaten
    history.add_tile(aktueller_raum)                                                            #Letzten Raum im History Modul updaten
    #standort updaten
