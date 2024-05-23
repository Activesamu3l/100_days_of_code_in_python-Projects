from tkinter import *

FONT = ("Arial", 15)


def miles_to_km():
    miles = float(miles_input.get())
    kilometers = miles * 1.60934.__round__()
    km_result_label.config(text=f"{kilometers}")


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

is_equal_to_label = Label(text="is equal to", font=FONT)
is_equal_to_label.grid(column=0, row=1)

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

km_result_label = Label(text="0", font=FONT)
km_result_label.grid(column=1, row=1)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

miles_label = Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=0)

km_label = Label(text="Km", font=FONT)
km_label.grid(column=2, row=1)






window.mainloop()