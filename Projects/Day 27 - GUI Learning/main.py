import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label

label = tkinter.Label(text="Test", font=("Arial", 24, "bold"))
label.pack()


window.mainloop()
