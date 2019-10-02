from tkinter import *





win = Tk()



def exitProgram():
	print("Exit Button pressed")

	win.quit()	


win.title("First GUI")
win.geometry('800x480')

exitButton  = Button(win, text = "Exit")
exitButton.pack(side=BOTTOM)

Fahren = Button(win, text = "Fahren")
Fahren.pack(side=LEFT)

Stop = Button(win, text = "Stop")
Stop.pack(side=RIGHT)

Start = Button(win, text = "Start")
Start.pack(side=TOP)

mainloop()
