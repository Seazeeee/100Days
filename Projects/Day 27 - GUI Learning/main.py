import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label

label = tkinter.Label(text="Test", font=("Arial", 24, "bold"))
label.grid(row=0, column=0)

label["text"] = "New Text"
label.config(text="New Text")

# Button


def button_click():
    label.config(text="I got clicked")
    print(user_input.get())


button = tkinter.Button(text="Click Me", command=button_click)
button.grid(column=1, row=2)

button_2 = tkinter.Button(text="New Button")
button_2.grid(column=3, row=0)


# Entry

user_input = tkinter.Entry(width=10)
user_input.grid(column=4, row=3)


window.mainloop()
