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
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():

    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    check_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if (reps % 8) == 0:
        countdown(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif (reps % 2) == 0:
        countdown(short_break_sec)
        timer_label.config(text="Break", fg=GREEN)
    else:
        countdown(work_sec)
        timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        if reps % 2 == 0 or reps % 8 == 0:
            check_label["text"] += "✔"


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
check_label.config(fg=GREEN, background=YELLOW, font=(FONT_NAME, 20))
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
    command=reset_timer,
)

reset_button.grid(column=2, row=3)

window.mainloop()
