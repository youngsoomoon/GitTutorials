result = 0
f = open("lab01.txt")
for i in range(1,5):
    num = int(f.readline())
    print(num)
    result += num
f.close()
print(result)
