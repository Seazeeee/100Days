import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    countdown(5 * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, countdown, count - 1)


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


timer_label = tkinter.Label()
timer_label.config(
    text="Timer", font=(FONT_NAME, 40, "bold"), background=YELLOW, fg=GREEN
)
timer_label.grid(column=1, row=1)

check_label = tkinter.Label()
check_label.config(fg=GREEN, text="✔", background=YELLOW, font=(FONT_NAME, 20))
check_label.grid(column=1, row=4)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo = tkinter.PhotoImage(file="Projects/pomodoro-start/tomato.png")
canvas.create_image(100, 112, image=photo)
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(column=1, row=2)

start_button = tkinter.Button(
    text="Start",
    font=(FONT_NAME, 16),
    foreground="Black",
    background=YELLOW,
    border=0,
    justify="center",
    command=start_timer,
)

start_button.grid(column=0, row=3)

reset_button = tkinter.Button(
    text="Reset",
    font=(FONT_NAME, 16),
    foreground="Black",
    background=YELLOW,
    border=0,
    justify="center",
)

reset_button.grid(column=2, row=3)

window.mainloop()
