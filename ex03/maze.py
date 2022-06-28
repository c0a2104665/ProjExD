import tkinter as tk
from tokenize import maybe
import maze_maker as mm

def key_down(event):
    global key
    key = event.keysym
    #print(f"{key}キーがおされました")
    main_proc()

def key_up(event):
    global key
    key = ""

def main_proc():
    global cx, cy
    global mx, my
    """
    delta = {     #キー：押されているkey/値：移動幅リスト[x,y]
            ""     :[0,0],
            "Up"   :[0,-20],
            "Down" :[0,+20],
            "Left" :[-20,0],
            "Right":[+20,0]
            }
    """
    if key == "Up":
        cy -= 100
    if key == "Down":
        cy += 100
    if key == "Left":
        cx -= 100
    if key == "Right":
        cx += 100
    #cx, cy = cx +delta[key][0], cy+ delta[key][1]
    canvas.coords("tori",cx,cy)
    root.after(1000, main_proc)

#def 


if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(root,
                    width = 1200,
                    height = 900,
                    bg = "black")
    #root.geometry("1200x900")
    canvas.pack()

    maze_bg = mm.make_maze(15, 9)
    #print(maze_bg)
    maze_sh = mm.show_maze(canvas, maze_bg) #canvasにmaze_bgを書く

    tori = tk.PhotoImage(file = "fig/6.png")

    mx, my = 1, 1
    cx, cy = mx*100+50, my*100+50
    canvas.create_image(cx,cy,image = tori, tag = "tori")

    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    main_proc()

    root.mainloop()
 