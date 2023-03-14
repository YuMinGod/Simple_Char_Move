import tkinter

key = ""
def key_down(e):
    global key
    key = e.keysym
def key_up(e):
    global key 
    key = ""

cx = 400
cy = 300

def main_proc():
    global cx, cy
    if key == "Up":
        cy = cy - 20
    elif key == "Down":
        cy = cy + 20
    elif key == "Left":
        cx = cx - 20
    elif key == "Right":
        cx = cx + 20
    canvas.coords("Bazzi", cx, cy)
    root.after(10, main_proc)

root = tkinter.Tk()
root.title("Test")
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)
canvas = tkinter.Canvas(width=800, height=600, bg="skyblue")
canvas.pack()
img = tkinter.PhotoImage(file="bazzi.png")
canvas.create_image(cx, cy, image=img, tag="Bazzi")
main_proc()
root.mainloop()