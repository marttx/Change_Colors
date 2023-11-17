import tkinter as tk
def button_click(color):
    input.config(bg=color)
win=tk.Tk()
win.config(bg="pink")
win.geometry("600x600")
input=tk.Entry(win, width=40)
input.place(x=90, y=112)
colors=['#CD5C5C', "#F08080", "Salmon", "DarkSalmon", "LightSalmon"]
for color in colors:
    but=tk.Button(win, text="Кнопка 1", bg='#CD5C5C', padx=10, pady=13, command=lambda color=color:button_click('#CD5C5C'))
but.place(x=5, y=12)
but1=tk.Button(win, text="Кнопка 2", bg="#F08080", padx=10, pady=13, command=lambda color=color:button_click("#F08080"))
but1.place(x=87, y=12)
but2=tk.Button(win, text="Кнопка 3", bg="Salmon", padx=10, pady=13, command=lambda color=color:button_click("Salmon"))
but2.place(x=169, y=12)
but3=tk.Button(win, text="Кнопка 4", bg="DarkSalmon", padx=10, pady=13, command=lambda color=color:button_click("DarkSalmon"))
but3.place(x=250, y=12)
but4=tk.Button(win, text="Кнопка 5", bg="LightSalmon", padx=10, pady=13, command=lambda color=color:button_click("LightSalmon"))
but4.place(x=332, y=12)
win.mainloop()