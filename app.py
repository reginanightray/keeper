from tkinter import *
from random import randrange, randint


def move_ball():
    global score_count
    global game_flag
    global ball_speed
    canvas.move(ball, 0, ball_speed)
    if canvas.coords(ball)[3] >= HEIGHT - 50:
        bottom = canvas.coords(ball)[0] + 15
        if canvas.coords(keeper)[0] < bottom < canvas.coords(keeper)[2]:
            score_count += 1
            canvas.itemconfigure(score, text=str(score_count))
            ball_x = randint(0, WIDTH - 30)
            canvas.coords(ball, ball_x, 0, ball_x + 30, 30)
        else:
            game_flag = False


def move_keeper():
    if keeper_speed > 0 and canvas.coords(keeper)[2] < WIDTH - 5 or \
            keeper_speed < 0 and canvas.coords(keeper)[0] > 5:
        canvas.move(keeper, keeper_speed, 0)


def key_handle(event):
    global keeper_speed
    if event.keysym == 'Left':
        keeper_speed = -5
    elif event.keysym == 'Right':
        keeper_speed = 5
    elif event.keysym == 'space':
        keeper_speed = 0


def main():
    move_ball()
    move_keeper()
    if game_flag:
        if score_count < 5:
            root.after(30, main)
        elif score_count < 10:
            root.after(20, main)
        else:
            root.after(10, main)
    else:
        canvas.create_text(WIDTH / 2, HEIGHT / 2, text='Game Over!', font='Georgia 25', fill='yellow')


root = Tk()
root.title('keeper')
HEIGHT = 700
WIDTH = 400
canvas = Canvas(root, height=HEIGHT, width=WIDTH, bg='green')
canvas.pack()
ball = canvas.create_oval(WIDTH / 2 - 15, 0, WIDTH / 2 + 15, 30, fill='yellow', outline='yellow')
gate = canvas.create_rectangle(0, HEIGHT - 50, WIDTH, HEIGHT, fill='white', outline='white')
keeper = canvas.create_rectangle(0, HEIGHT - 50, 60, HEIGHT - 35, fill='black')
score_count = 0
score = canvas.create_text(WIDTH - 60, HEIGHT - 20, text=str(score_count), font='Georgia 14', fill='blue')
ball_speed = 5
keeper_speed = 0
canvas.bind('<KeyPress>', key_handle)
canvas.focus_set()
game_flag = True

main()

root.mainloop()
