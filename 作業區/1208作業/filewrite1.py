
fw = open("filewrite1.txt", "w")
fw.write("content")
fw.close()


fr = open("filewrite1.txt", "r")
print(fr.read())
fr.close()


