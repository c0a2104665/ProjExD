import tkinter as tk
import tkinter.messagebox as tkm

"""
def collback(btn):
    def nothing():
        btn.config(bg = "#008000")
    return nothing
"""

def button_click(event):
    btn = event.widget
    num = btn["text"]#クリックされた文字
    if num == "=":
        eqn = entry.get()
        sum = eval(eqn)
        entry.delete(0,tk.END)
        entry.insert(tk.END,f"{sum}")
        print(sum)

    elif num == "AC":
        entry.delete(0,tk.END)
        entry.insert(tk.END)

    elif num == "÷":
        entry.insert(tk.END,"/")

    elif num == "×":
        entry.insert(tk.END,"*")
    
    elif num == "^2":
        entry.insert(tk.END,"**")

    else:
        #tkm.showwarning("",f"[{num}]ボタンが押されました")
        entry.insert(tk.END,f"{num}")
        



if __name__ == "__main__":
    root = tk.Tk()
    root.title("シンプル電卓")
    #root.geometry("300x500")
                     
r,c = 1,0
ata = [9,8,7,"×","^2",6,5,4,"÷","//",3,2,1,"+","-","",0,".","=","AC"]
for i, num in enumerate([i for i in ata]):
    button = tk.Button(root,
                       text=f"{num}",
                       width=4,
                       height = 2,
                       font = ("Times New Roman", 30)
                    )
    button.bind("<1>",button_click)
    button.grid(row = r,column = c)
    c += 1
    if (i+1)%5 == 0:
        r += 1
        c = 0


        

entry = tk.Entry(root,justify="right",width = 17,font = ("Time New Roman",40))
entry.grid(row = 0,columnspan = 5)

root.mainloop()    
