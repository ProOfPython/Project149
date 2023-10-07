from tkinter import *
from random import randint

root = Tk()
root.title('Random Letters')
root.geometry('400x400')
root.configure(background = 'snow')

lblWord = Label(root, text = '', background = 'light blue')
lblWord.place(relx = 0.5, rely = 0.5, anchor = CENTER)

def makeWord():
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    word = ''
    for i in range(5):
        word += letters[randint(0, 25)]
    lblWord['text'] = word

btnMakeWord = Button(root, text = 'Make Random Word', command = lambda: makeWord())
btnMakeWord.place(relx = 0.5, rely = 0.4, anchor = CENTER)

root.mainloop()