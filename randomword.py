# 영단어 사전에서 무작위의 단어를 받아
# 단어의 알파벳에 대응하는 수들의 합이 100이 되는지 판별하는 프로그램
import random

# ord(alp) % 96 = number of alp

word_file = "/usr/share/dict/words" # unix english word dict file
WORDS = open(word_file).readlines()
result = random.choice(WORDS).strip()
# choose random word from WORDS list, delete spaces by strip()
print(result)

sum = 0
for i in result:
    if i.isalpha():
        print(i)
        sum = sum + (ord(i)%96)
# a부터 z까지 1에서 26의 수를 부여
#단어의 각 알파벳에 해당하는 수들의 합을 연산
print(sum)
if sum == 100:
    print(result + " is 100WORDS")
else:
    print(result + " is not the 100WORDS")
