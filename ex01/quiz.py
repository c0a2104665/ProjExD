import random
from this import d

quiz = {}
quiz["ex1"] = {"問題文":"サザエさんの旦那の名前は?","選択":["益男","マスオ"],"正解":"マスオ"}
quiz["ex2"] = {"問題文":"カツオの妹の名前は?","選択":["ワカメ","わたあめ"],"正解":"ワカメ"}
quiz["ex3"] = {"問題文":"タラオはカツオから見てどんな関係?","選択":["甥っ子","姪っ子"],"正解":"甥っ子"}

key,value = random.choice(list(quiz.items()))
print(key,value["問題文"])
print("選択",end="")
for i in range(len(value["選択"])):
    print(f"{i+1}.{value["選択"][i]},end = ''")

print("")

answer = int(input("選択しな"))

if value["選択"][answer-1] == value["正解"]:
    print("正解!")
else:
    print(f"残念")


