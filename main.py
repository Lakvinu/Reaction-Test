from tkinter import *
import time
from decimal import Decimal
import random

def rgbtohex(r,g,b):
    return f'#{r:02x}{g:02x}{b:02x}'

window = Tk()
window.title("Reaction Test by Lakvinu")
window.configure(background=rgbtohex(43,135,209))

start = Label(window, text = "When the red box turns green, click as quickly as you can,\n Click anywhere to start", bg=rgbtohex(43,135,209),
              fg='white', font=("Arial",20,'bold'))

start.place(anchor = "center", relx = 0.5, rely = 0.5)
check = False
length = 0
begin = 0


def reset():

    global start
    global check

    start['text'] = "When the red box turns green, click as quickly as you can,\n Click anywhere to start"
    start['bg'] = rgbtohex(43,135,209)
    start['fg'] = 'white'
    start['font'] = ("Arial",20,'bold')
    window.configure(background=rgbtohex(43,135,209))

    check = False


def left_click(event):
    global begin
    global check
    global length

    if check == None:
        reset()

    elif check == True:

        if start['bg'] == 'light green':
            check = None
            new_time = time.perf_counter() - begin
            start['text'] = 'Your Reaction speed is ' + str(int(new_time * 1000)) + ' ms'
            start['font'] = ("Arial", 50)



    elif check == False:

        check = True
        window.configure(background=rgbtohex(206,38,54))
        start['bg'] = rgbtohex(206,38,54)
        length = float(Decimal(random.randint(100,700) / 100))

        window.update()
        time.sleep(length)

        window.configure(background="light green")
        start['bg'] = 'light green'
        begin = time.perf_counter()

window.bind("<Button-1>", left_click)

window.mainloop()
