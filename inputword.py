# 사용자로부터 단어를 입력받아 판별하는 프로그램
# ord(alp) % 96 = number of alp
word = input("Enter the English word : ")
sum = 0
for i in word:
    if i.isalpha():
        print(i)
        sum = sum + (ord(i)%96)

print(sum)
if sum == 100:
    print(word + " is 100WORDS")
else:
    print(word + " is not the 100WORDS")
