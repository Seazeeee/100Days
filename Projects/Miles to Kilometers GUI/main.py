"""Module that houses the main function."""

import tkinter

# Creation of them main screen
tk = tkinter.Tk()
tk.title("Mile to Km Converter")
tk.maxsize(width=300, height=100)
tk.config(padx=20, pady=20)

# Creation of Entry

miles_entry = tkinter.Entry(width=10)
miles_entry.grid(column=1, row=0)

# Creation of labels

# Is Equal To

equal_to = tkinter.Label()
equal_to.config(text="is equal to")
equal_to.grid(column=0, row=1)

# Miles
miles_label = tkinter.Label()
miles_label.config(text="Miles")
miles_label.grid(column=3, row=0)

# Km
miles_label = tkinter.Label()
miles_label.config(text="Km")
miles_label.grid(column=3, row=1)

# Creation of button


def get_km():
    miles_amount = int(miles_entry.get())
    final_km = round(miles_amount * 1.609)

    return_value = tkinter.Label()
    return_value.config(text=final_km)
    return_value.grid(column=1, row=1)


calc_button = tkinter.Button(text="Calculate", command=get_km)
calc_button.grid(column=1, row=3)


tk.mainloop()
