import tkinter as tki
import time

clicks=0
start_cps=0
end_cps=0

def btn_click():
    global clicks, start_cps, end_cps

    clicks +=1
    end_cps = time.time()

    if end_cps - start_cps >= 1:
        btn.config(text=clicks)
        clicks=0
        start_cps=time.time()

window = tki.Tk()
window.title("cps clicker")
window.geometry("300x300")

btn = tki.Button(
    window,
    text = 0,
    font = "consolas 20",
    command=btn_click
)
btn.place(
    x = 0,
    y = 0,
    width=300,
    height=300
)

window.mainloop()