import random
from tkinter import *

# ord(alp) % 96 = number of alp

root = Tk()
root.title("Find 100WORDS")
root.geometry("360x480")

root.resizable(False, False)

display = Entry(root)
display.pack()

word_file = "/usr/share/dict/words"
WORDS = open(word_file).readlines()

def btn_rdm_word_cmd():
    result = random.choice(WORDS).strip()
    display.delete(0, END)
    display.insert(0, result)

def btn_chk_cmd():
    input_word = display.get()
    sum = 0
    for i in input_word:
        if i.isalpha():
            print(i)
            sum = sum + (ord(i)%96)

    print(sum)
    if sum == 100:
        print(input_word + " is 100WORDS")
    else:
        print(input_word + " is not the 100WORDS")

btn_rdm_word = Button(root, text="Random Word", command=btn_rdm_word_cmd)
btn_rdm_word.pack()

btn_chk = Button(root, text="Check", command=btn_chk_cmd)
btn_chk.pack()


root.mainloop()