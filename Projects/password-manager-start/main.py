import tkinter
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():

    if (
        len(website_entry.get()) <= 0
        or len(email_entry.get()) <= 0
        or len(pass_entry.get()) <= 0
    ):
        messagebox.showwarning(
            title="Oops", message="Please don't leave any fields empty!"
        )
    else:
        is_ok = messagebox.askokcancel(
            title=website_entry.get(),
            message=f"These are the details entered: \nEmail: {email_entry.get()}"
            f"\nPassword: {pass_entry.get()} \nIs it ok to save?",
        )

        if is_ok:
            with open("Ignore/data.txt", encoding="utf-8", mode="a") as file:
                file.writelines(
                    f"{website_entry.get()} | {email_entry.get()} | {pass_entry.get()}\n"
                )

            website_entry.delete(0, tkinter.END)
            email_entry.delete(0, tkinter.END)
            pass_entry.delete(0, tkinter.END)


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0)
photo = tkinter.PhotoImage(file="Projects/password-manager-start/logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(column=1, row=0)

# Creation of all labels

website_label = tkinter.Label()
website_label.config(text="Website:", fg="black")
website_label.grid(column=0, row=1)

email_label = tkinter.Label()
email_label.config(text="Email/Username:", fg="black")
email_label.grid(column=0, row=2)

pass_label = tkinter.Label()
pass_label.config(text="Password:", fg="black")
pass_label.grid(column=0, row=3)

# Creation of Entry's

website_entry = tkinter.Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky="w")
website_entry.focus()

email_entry = tkinter.Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky="w")
email_entry.insert(tkinter.END, "matt@email.com")

pass_entry = tkinter.Entry(width=21, justify="left")
pass_entry.grid(column=1, row=3, sticky="w")

# Creation of buttons

generate_button = tkinter.Button(
    text="Generate Password", fg="black", border=0, width=14
)
generate_button.grid(column=2, row=3)

add_button = tkinter.Button(
    text="Add", fg="black", border=0, justify="center", width=35, command=save_password
)
add_button.grid(column=1, row=4, columnspan=2, sticky="w")

window.mainloop()
