import string                
import random
import time

tray = 5   #実行回数
all = 10   #アルファベットの数
mai = 2    #欠損の数

s = random.sample(string.ascii_lowercase[:all],k = all)

def main():
    st = time.perf_counter()
    for _ in range(tray):
        ans = s.sample(mai)
    en = time.perf_counter()

def kaitou():
    num = int(input("欠損文字は、何文字ですか?:"))
    if num != mai:





        

    
    





























