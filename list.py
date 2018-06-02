
#リスト 複数のデータを格納する
data = ["りんご", "かき", "みかん"]

#番号でアクセスするが0からスタートする
print(data[0])
#リスト全体をデバッグすることもできる
print(data)

#値の変更、追加ができる
data[2] = "なし"
data.append("パイナップル")
print(data)

print("----ループを用いた配列処理----")
#一般的にはループ処理でアクセスすることが多い
for i in range(3):
    print(data[i])

print("----タプル----")
#タプル
#リストと似ているが要素の変更、追加ができない
data2 = ("野球", "サッカー", "テニス")
print(data2[0])
#data2[0] = "バスケットボール"
#data2.append("バスケットボール")
#もし実行すると下記のようなエラーが起こる
#TypeError: 'tuple' object does not support item assignment

print("----セット型----")
data3 = [1, 1, 2, 2, 3]
setData = set(data3)
print(setData)
#要素の追加と削除
setData.add(4)
setData.remove(1)
print(setData)
#完全削除
setData.clear()
print(setData)
