from tkinter import *
from tkinter import ttk
from helper.Helper import Helper

class Main(object):
    def __init__(self, master) -> None:
        self.master = master

        # Main Frame
        mainFrame = Frame(self.master)
        mainFrame.pack()

        # Top Frame
        topFrame = Frame(mainFrame, width=1350, height=70, bg='#f8f8f8', padx=20, relief='sunken', borderwidth=2)
        topFrame.pack(side=TOP, fill=X)

        # Center Frame
        centerFrame = Frame(mainFrame, width=1350, height=680, relief='ridge')
        centerFrame.pack(side=TOP)

        # Center Left Frame
        centerLeftFrame = Frame(centerFrame, width=900, height=700, bg='#e0f0f0', borderwidth=2, relief='sunken')
        centerLeftFrame.pack(side=LEFT)
        
        # Center Right Frame
        centerRightFrame = Frame(centerFrame, width=450, height=700, bg='#e0f0f0', borderwidth=2, relief='sunken')
        centerRightFrame.pack()

        # Search Bar
        searchBar = LabelFrame(centerRightFrame, width=440, height=75, text='Search Box', bg='#9bc9ff')
        searchBar.pack(fill=BOTH)
        self.labelSearch = Label(searchBar, text='Search:', font='arial 12 bold', bg='#9bc9ff', fg='white')
        self.labelSearch.grid(row=0, column=0, padx=20, pady=10)
        self.entrySearch = Entry(searchBar, width=30, bd=5)
        self.entrySearch.grid(row=0, column=1, columnspan=3, padx=10, pady=10)
        self.buttonSearch = Button(searchBar, text='Search', font='arial 12', bg='#fcc324', fg='white')
        self.buttonSearch.grid(row=0, column=4, padx=20, pady=10)

        # List Bar
        listBar = LabelFrame(centerRightFrame, width=440, height=175, text='List Box', bg='#fcc324')
        listBar.pack(fill=BOTH)
        self.labelList = Label(listBar, text='Sort By', font='times 16 bold', fg='#2488ff', bg='#fcc324')
        self.labelList.grid(row=0, column=2)

        #########################################################################################################################

        # Add Book Button
        self.iconBook = Helper.getImage('addbook')
        self.buttonBook = Button(topFrame, text='Add Book', image=self.iconBook, compound=LEFT, font='arial 12 bold')
        self.buttonBook.pack(side=LEFT, padx=10)
        
        # Add Member Button
        self.iconMember = Helper.getImage('users')
        self.buttonMember = Button(topFrame, text='Add Member', image=self.iconMember, compound=LEFT, font='arial 12 bold')
        self.buttonMember.pack(side=LEFT, padx=10)
        
        # Give Book Button
        self.iconGive = Helper.getImage('givebook')
        self.buttonGive = Button(topFrame, text='Give Book', image=self.iconGive, compound=LEFT, font='arial 12 bold')
        self.buttonGive.pack(side=LEFT, padx=10)



def main():
    root = Tk()
    app = Main(root)
    root.title('Library Management System')
    root.geometry('1350x750+350+200')
    root.attributes('-zoomed', True)
    root.bind('<Escape>', lambda x: closeWindow(root))
    root.mainloop()

def closeWindow(x): x.destroy()

if __name__ == '__main__':
    main()