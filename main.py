import tkinter as tk

window = tk.Tk()
window.title("Disappearing Text App")
window.minsize(500, 500)

text = ""
counter = 0


def disappear_text():
    textbox.delete(1.0, tk.END)


def check_disappear():
    global counter, text
    if text == textbox.get(1.0, tk.END):
        if counter == 4:
            window.after(1000, disappear_text)
            counter = -1
        window.after(1000, check_disappear)
        counter += 1
    else:
        window.after(1000, check_disappear)
        text = textbox.get(1.0, tk.END)
        counter = 0


title = tk.Label(text="Welcome to the Disappearing Text App.", font=("Ariel", 20))
title.grid(row=0, column=0)
textbox = tk.Text(height=25, width=55)
textbox.focus()
textbox.grid(rowspan=3, pady=25, padx=10)
window.after(1000, check_disappear)

window.mainloop()
