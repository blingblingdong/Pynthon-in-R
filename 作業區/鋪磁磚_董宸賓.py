#定義變數
totalWidth = int(100)
tileWidth = int(5)

#計算
pairsoftiles = int((totalWidth-tileWidth)/(2*tileWidth))
numberOftiles = 1+(2*pairsoftiles)
Gap = (totalWidth - numberOftiles*tileWidth)/2

#打印
print(pairsoftiles)
print(numberOftiles)
print(Gap)
