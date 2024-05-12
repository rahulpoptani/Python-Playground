from tkinter import *
from tkinter import ttk

root = Tk()
entryName = ttk.Entry(root, width=30)
entryPass = ttk.Entry(root, width=30)
buttonSubmit = ttk.Button(root, text='Submit')
labelTitle = ttk.Label(text='Information System', font=(('Arial'),22))
labelName = ttk.Label(text='Enter Name:')
labelPass = ttk.Label(text='Enter Password:')

# Positioning
labelTitle.grid(row=0, column=0, columnspan=2)
labelName.grid(row=1, column=0, sticky=W)
labelPass.grid(row=2, column=0, sticky=W)
entryName.grid(row=1, column=1)
entryPass.grid(row=2, column=1)
buttonSubmit.grid(row=3, column=1, sticky=E, pady=5)

# Checkbox
def saveCredentials():
    if chvar.get() == 1: print('Credentials Saved')
    print(f'Gender: {genderVar.get()}')
chvar = IntVar()
chvar.set(0)
cbox = Checkbutton(root, text='Remember Me', variable=chvar, font='Arial 16').grid(row=4, column=1, sticky=E)
buttonSubmit.config(command=saveCredentials)

# Radio Button
genderVar = StringVar()
ttk.Radiobutton(root, text='Male', value='Male', variable=genderVar).grid(row=5, column=0)
ttk.Radiobutton(root, text='Female', value='Female', variable=genderVar).grid(row=5, column=1)

# ComboBox / DropDown
comboBoxVar = StringVar()
comboBox = ttk.Combobox(root, textvariable=comboBoxVar, values=(['Jan','Feb','Mar','Apr','May']), state='readonly').grid(row=6, column=0)

# Spinbox
spinBoxVar = StringVar()
Spinbox(root, from_=2000, to=2024, textvariable=spinBoxVar, state='readonly').grid(row=6,column=1)

root.geometry('500x400')
root.mainloop()