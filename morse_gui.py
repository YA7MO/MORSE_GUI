from tkinter import *
import gpiozero
from gpiozero import LED
import time

led = LED(2)

moresCodes = {'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',
        }

win = Tk()
win.title("morese code gui")

label = Label(win, text = "Enter Your word")
label.pack()
 
textField = Entry(win, width = 10);
textField.pack()
      

def dash():
    print("here dash")
    led.on()
    time.sleep(1)
    led.off()
    time.sleep(1)
    
def dot():
    print("here dot")
    led.on()
    time.sleep(0.5)
    led.off()
    time.sleep(0.5)
    
def text():
        
        textVal= textField.get()
        textVal = textVal.upper()
        print(textVal)
        textLenght = len(textVal);
        
        if(textLenght <= 12):
            for i in range(textLenght):
                for chars in moresCodes[textVal[i]]:
                    print(i)
                    if(chars == '-'):
                        dash()
                    elif(chars == '.'):
                        dot()
        elif(textLenght > 12):
            error = Label(win,text = "word has to be 12 or less", bg = "red")
            error.pack()

convertBtn = Button( text = "convert to morse code" , height = 1, width=20, command= text)
convertBtn.pack()
win.mainloop()


