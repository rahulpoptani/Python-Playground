from tkinter import *

root = Tk()
root.title('Calculator App')
root.geometry('380x550+850+200')
root.resizable(False, False)

# Functions
def enterNumber(x):
    if entryBox.get() == '0':
        entryBox.delete(0, 'end')
        entryBox.insert(0, str(x))
    else:
        length = len(entryBox.get())
        entryBox.insert(length, str(x))

def enterOperator(x):
    if entryBox.get() != '0':
        length = len(entryBox.get())
        entryBox.insert(length, operators[x]['text'])

def clear():
    entryBox.delete(0, END)
    entryBox.insert(0, '0')

resultList = []
def funcOperator():
    content = entryBox.get()
    print(content)
    result = eval(content)
    print(result)
    entryBox.delete(0, END)
    entryBox.insert(0, str(result))
    resultList.append(content)
    resultList.reverse()
    statusBar.configure(text=f"History: {'|'.join(resultList[:5])}", font='verdana 11 bold')

def funcDelete(): 
    length = len(entryBox.get())
    entryBox.delete(length-1,'end')
    if length == 1:
        entryBox.insert(0,"O")

# Entry Box
entryBox = Entry(font='verdana 14 bold', width=25, bd=10, justify='right', bg='#e6e6fa')
entryBox.insert(0, '0')
entryBox.place(x=20, y=10)

# Number Buttons
numbers = []
for i in range(10):
    numbers.append(Button(width=4, text=str(i), font='times 15 bold', bd=5, command=lambda x=i: enterNumber(x)))

buttonText = 1
for i in range(3):
    for j in range(3):
        numbers[buttonText].place(x=25+j*90, y=70+i*70)
        buttonText += 1

zeroButton = Button(width=22, text='0', font='times 15 bold', bd=5, command=lambda x=0: enterNumber(x))
zeroButton.place(x=25, y=280)

# Operator Buttons
operators = []
for i in range(4):
    operators.append(Button(width=4, text=str(i), font='times 15 bold', bd=5, command=lambda x=i: enterOperator(x)))

operators[0]['text'] = '+'
operators[1]['text'] = '-'
operators[2]['text'] = '*'
operators[3]['text'] = '/'

for i in range(4):
    operators[i].place(x=290, y=70+i*70)

# Other Buttons
clearButton = Button(width=4, text='C', font='times 15 bold', bd=5, command=clear)
clearButton.place(x=25, y=340)

dotButton = Button(width=4, text='.', font='times 15 bold', bd=5, command=lambda x='.': enterNumber(x))
dotButton.place(x=110, y=340)

equalButton = Button(width=4, text='=', font='times 15 bold', bd=5, command=funcOperator)
equalButton.place(x=200, y=340)

icon = PhotoImage(file='Calculator/icons/arrow.png')
deleteButton = Button(width=65, height=30, bd=5, command=funcDelete, image=icon)
deleteButton.place(x=290, y=340)

# History Label
statusBar = Label(text='History:', relief='sunken', height=3, anchor=W, font='verdana 11 bold')
statusBar.pack(side='bottom', fill=X)

# Close window with Escape
def closeWindow(x): root.destroy()
root.bind('<Escape>', lambda x: closeWindow(x))

root.mainloop()