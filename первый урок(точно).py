import tkinter as tk


okno = tk.Tk()
okno.title("Шарик и треугольникk")


def move_circle():
    global dx, dy
    canvas.move(circle, dx, dy)
    canvas.move(triangle, dx / 2, dy / 2)


    x1, y1, x2, y2 = canvas.coords(circle)


    if x1 + dx < 0 or x2 + dx > 600:
        dx = -dx
    if y1 + dy < 0 or y2 + dy > 500:
        dy = -dy


    okno.after(30, move_circle)





canvas = tk.Canvas(okno, width=600, height=500, bg='white')
canvas.pack()


circle = canvas.create_oval(50, 50, 100, 100, fill='red', outline='black', tags='circle')

triangle = canvas.create_polygon(200, 150, 250, 250, 150, 250,
                                 fill='blue', outline='black', tags='triangle')

dx = 2
dy = 3
print("hello worldkkk")
move_circle()

okno.mainloop()