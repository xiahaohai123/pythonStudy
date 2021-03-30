str1 = "abcdefg"
for c in str1:
    if c == 'c':
        break
    print(c)

for c in str1:
    if c == 'c':
        continue
    print(c)
else:
    print("ccc")

num = 1
while num < 5:
    print(num)
    num += 1
else:
    print("ccc")
