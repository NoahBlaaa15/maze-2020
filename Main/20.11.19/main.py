#MAZE 2020 MAIN

#IMPORTS
import sys
import maze_serial as m_ser
import tile
import wall
import arduinodata
import history

#SETUP
m_ser.start                                                                                     #Serial Kommunikation starten
kachel = tile.Tile(None, None, None, None)                                                      #Initialkachel erstellen
kachel.set_coordinates(0, 0, 0)                                                                 #Initialkachel auf 0, 0, 0 setzen
aktueller_raum = kachel                                                                         #Raum von Kachel zu aktueller_raum verschieben

#ACTION
while True:
    m_ser.send('pls#')                                                                          #Daten von Arduino anfragen
    data = m_ser.receive('here')                                                                #Daten von Arduino empfangen
    
    data = arduinodata.decode(data)                                                             #Empfangene Daten entpacken
    wallsdata, victimsdata, environmentdata, motorsdata = arduinodata.analyze(data, 'all')      #Entpackte Daten analysieren
    #kameradaten jetzt auch analysieren
    
    if environmentdata[floor] == 'black':                                                       #Schwarze Platte checken
        aktueller_raum.set_type(black)
        aktueller_raum.set_top(wall.Wall())                                                     #OBEN ABRIEGELN
        aktueller_raum.set_rgt(wall.Wall())                                                     #RECHTS ABRIEGELN
        aktueller_raum.set_but(wall.Wall())                                                     #UNTEN ABRIEGELN
        aktueller_raum.set_lft(wall.Wall())                                                     #LINKS ABRIEGELN
        
        #befehl zum runterfahren geben
        #auf bestätigung warten
        aktueller_raum = history.get_last_tile()
        continue
        
    #rampe? -> rampenbefahrungsmodus
    #gibts undefinierte räume drumherum? -> erstellen und wände je nach WALLSDATA setzen
        #wenn keine wand da und unbefahren -> da hinfahren auf stack drauf
    #irgendwelche opfer hier? -> wände dementsprechend modifizieren/checken und wenn noch nicht gerettet kits abwerfen
    #checkpoint? -> letzter checkpoint variable aktualisieren
    
    #oberste stack aufgabe nehmen, entschlüsseln
    #genaue fahranweisung an arduino senden
    #Fotos machen mit ~15 FPS
    #auf bestätigung warten
    #Nach Bestätigung fotos stoppen
    #Objekterkennung starten
    #passen rotationswerte etc? -> sonst anpassungsbefehl schicken
    #letzte fahrt in history modul updaten
    #letztes tile in histoy modul updaten
    #standort updaten
