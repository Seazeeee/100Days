import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label

label = tkinter.Label(text="Test", font=("Arial", 24, "bold"))
label.pack()

label["text"] = "New Text"
label.config(text="New Text")

# Button


def button_click():
    label.config(text="I got clicked")
    print(user_input.get())


button = tkinter.Button(text="Click Me", command=button_click)
button.pack()


# Entry

user_input = tkinter.Entry(width=10)
user_input.pack()


window.mainloop()
