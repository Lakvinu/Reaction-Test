from tkinter import *
import time
from decimal import Decimal
import random

def rgbtohex(r,g,b):
    return f'#{r:02x}{g:02x}{b:02x}'

window = Tk()
window.title("Reaction Test by Lakvinu")
window.configure(background=rgbtohex(43,135,209))
window.state('zoomed')
window.resizable(0,0)
main_label = Label(window, text = "When the red box turns green, click as quickly as you can,\n Click anywhere to start", bg=rgbtohex(43,135,209), fg='white', font=("Arial",40,'bold'))

main_label.place(anchor = "center", relx = 0.5, rely = 0.5)
begin_time = 0
end_time = 0
current_stage = 0

def start_stage():
    window.configure(background=rgbtohex(43, 135, 209))
    main_label['text'] = "When the red box turns green, click as quickly as you can,\n Click anywhere to start"
    main_label['bg'] = rgbtohex(43,135,209)


def wait_stage():
    window.configure(background=rgbtohex(206,38,54))
    main_label['text'] = "Wait for green"
    main_label['bg'] = rgbtohex(206,38,54)

def early_stage():
    window.configure(background=rgbtohex(43, 135, 209))
    main_label['text'] = "Too Soon"
    main_label['bg'] = rgbtohex(43, 135, 209)


def press_stage():

    global begin_time
    global current_stage

    if current_stage == 1:
        window.configure(background="light green")
        main_label['text'] = "Click me"
        main_label['bg'] = "light green"
        begin_time = time.perf_counter()
        current_stage = 2


def result_stage():
    global end_time
    end_time = time.perf_counter()
    main_label['text'] = str(int((end_time - begin_time) * 1000)) + ' ms\n Click to continue'


def command_function(event):

    global begin_time
    global current_stage

    # begin stage sending to the wait stage
    if current_stage == 0:
        wait_time = random.randint(3000,7000)
        current_stage = 1
        wait_stage()
        window.after(wait_time, press_stage)

    #in the middle of wait stage but if pressed too early
    elif current_stage == 1:
        current_stage = 3
        early_stage()

    #shows the result of your reaction time
    elif current_stage == 2:
        result_stage()
        current_stage = 3

    # resets to the front page or the start
    elif current_stage == 3:
        start_stage()
        current_stage = 0

window.bind("<Button-1>", command_function)

window.mainloop()