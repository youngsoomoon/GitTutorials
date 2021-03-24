
str1 = "안녕하세요\n\n"

#v2 = str1.endswith("요")
#v3 = str1.startswith("안녕1")


#print(str1.strip())

#print(len(str1))

filestream = open("lab00.txt")
contents = filestream.readline()
print(contents)

filestream.close()
