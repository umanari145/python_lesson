#文字の出力
print("Hello World")
print(10)
#値の代入
var1 = 10

#ここはコメントなのでプログラムには関係がない

#条件分岐　もし・・だったら・・それ以外なら・・・
#ヘコミがないと正常にプログラムが動かない
if var1 == 10:
    print("10です。")
else:
    print("10ではありません。")

#文字と数字は違う
if var1 == "10":
    print("文字の10です。")
else:
    print("文字の10ではありません。")


score = 70
#３つ以上の条件分岐
if score >= 80:
    print("頑張りましたね")
elif score >= 60:
    print("もう一歩です")
else:
    print("ダメダメです")

#ifは複数の条件を使うこともできる
a = 10
c = 7
#両方の場合はand
if a == 10 and c == 8:
    print("OK")
else:
    print("NG")
#片方はorのみ
if a == 10 or c == 8:
    print("OK")
else:
    print("NG")

#繰り返し0から4までを表示
for i in range(5):
    print(i)
