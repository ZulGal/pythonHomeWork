import tkinter as tk
from tkinter import * #ttk

window = Tk()
window.title("Поиграем? ")
window.geometry('800x250')

# def callbackFunc(event):
#     print(comboExample.get())
#     print("New Element Selected")
     
# app = tk.Tk() 
# app.geometry('200x100')

# labelTop = tk.Label(app,
#                     text = "Choose your favourite month")
# labelTop.grid(column=0, row=0)

# comboExample = ttk.Combobox(app, 
#                             values=[
#                                     "January", 
#                                     "February",
#                                     "March",
#                                     "April"])


# comboExample.grid(column=0, row=1)
# comboExample.current(1)
# print(comboExample.get())
# comboExample.bind("<<ComboboxSelected>>", callbackFunc)

lbl1 = Label(window, text= 'label1', padx=5, pady=5).grid(column = 0, row = 0)

mainloop() #app.mainloop()