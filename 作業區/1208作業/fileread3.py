fr1 = open("filewrite1.txt", "r")
print(fr1.read())
fr1.close()

fr2 = open("filewrite1.txt", "r")
print(fr2.read(5))
fr2.close()
