import tkinter as tk
import maze_maker as mm

def key_down(event):
    global key
    key = event.keysym
    print(f"{key}キーがおされました")
    

def key_up(event):
    global key
    key = ""

def main_proc():
    global cx, cy
    global mx, my
    
    delta = {     #キー：押されているkey/値：移動幅リスト[x,y]
            "Up"   :[0,-1],
            "Down" :[0,+1],
            "Left" :[-1,0],
            "Right":[+1,0]
            }
    """
    if maze_bg[my+delta[key][1]][mx+delta[key][0]] == 0:
        my, mx = my+delta[key][1],mx+delta[key][0]
    if key == "Up" and maze_bg[my-1][mx == 0]: my -= 1
    if key == "Down" and maze_bg[my-1][mx == 0]: my += 1
    if key == "Left" and maze_bg[my-1][mx == 0]: mx -= 1
    if key == "Right" and maze_bg[my-1][mx == 0]: mx -= 1
    """
    try:
        if maze_bg[my+delta[key][1]][mx+delta[key][0]] == 0:
            my, mx = my+delta[key][1],mx+delta[key][0]
    except:
        pass

    cx, cy = mx*100+50, my*100+50
    canvas.coords("tori",cx,cy)
    root.after(100, main_proc)

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
    mm.show_maze(canvas, maze_bg) #canvasにmaze_bgを書く
    tori = tk.PhotoImage(file = "fig/6.png")
    mx, my = 1, 1
    cx, cy = mx*100+50, my*100+50
    canvas.create_image(cx,cy,image = tori, tag = "tori")
    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    root.after(100,main_proc)
    root.mainloop()
 