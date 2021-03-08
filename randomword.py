import random

# ord(alp) % 96 = number of alp

word_file = "/usr/share/dict/words"
WORDS = open(word_file).readlines()
result = random.choice(WORDS).strip()
print(result)

sum = 0
for i in result:
    if i.isalpha():
        print(i)
        sum = sum + (ord(i)%96)

print(sum)
if sum == 100:
    print(result + " is 100WORDS")
else:
    print(result + " is not the 100WORDS")