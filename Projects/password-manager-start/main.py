import tkinter

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0)
photo = tkinter.PhotoImage(file="Projects/password-manager-start/logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(column=1, row=2)


window.mainloop()
