f = open("lyrics.txt", "w")

f.write("ddd")
f.write("\nkkk")
f.write("\nmmm")

f.close()

fr = open("lyrics.txt", "r")

print(fr.read())

fr.close()
