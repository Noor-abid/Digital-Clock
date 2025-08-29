from time import strftime
from tkinter import Label, Tk
from datetime import date

# Window config for Clock
window = Tk()
window.title("Digital Clock")
window.geometry("250x120")
window.configure(bg="black")
window.resizable(False, False)

# Time label
clock_label = Label(window, bg="black", fg="white",
                    font=("Times", 35, 'bold'), relief='flat')
clock_label.pack(pady=10)

# Date label
date_label = Label(window, bg="black", fg="white",
                   font=("Arial", 16))
date_label.pack()

def updating_label():
    current_time = strftime('%I:%M:%S %p')  # 12-hour format with AM/PM
    today = date.today().strftime("%A, %B %d, %Y")
    clock_label.configure(text=current_time)
    date_label.configure(text=today)
    clock_label.after(1000, updating_label)

updating_label()
window.mainloop()
