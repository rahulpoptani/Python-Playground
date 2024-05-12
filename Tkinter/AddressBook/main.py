from tkinter import *
import mypeople, addpeople, about as aboutPage
from helper.helper import Helper
from datetime import datetime

class Application(object):
    def __init__(self, master) -> None:
        self.master = master

        Helper.dataBootstrap()

        # Frames
        self.topFrame = Frame(master, height=150, bg='white')
        self.topFrame.pack(fill=X)
        self.bottomFrame = Frame(master, height=500, bg='#adff2f')
        self.bottomFrame.pack(fill=X)

        # Heading, Image and Date
        self.top_image = PhotoImage(file='AddressBook/icons/book.png')
        self.top_image_label = Label(self.topFrame, image=self.top_image, bg='white')
        self.top_image_label.place(x=120, y=10)

        self.heading_label = Label(self.topFrame, text='My Address Book App', font='arial 15 bold', fg='#ffa500', bg='white')
        self.heading_label.place(x=260, y=60)

        self.date_label = Label(self.topFrame, text=f'Date: {datetime.now().date()}', font='arial 12 bold', fg='#ffa500', bg='white')
        self.date_label.place(x=500, y=10)

        # Buttons
        self.myPeopleButtonIcon = PhotoImage(file='AddressBook/icons/man.png')
        self.myPeopleButton = Button(self.bottomFrame, text='My People', font='arial 12 bold', command=self.openMyPeople)
        self.myPeopleButton.config(image=self.myPeopleButtonIcon, compound='left')
        self.myPeopleButton.place(x=250, y=10)
        
        self.addPeopleButtonIcon = PhotoImage(file='AddressBook/icons/add.png')
        self.addPeopleButton = Button(self.bottomFrame, text='Add People', font='arial 12 bold', command=self.openAddPeople)
        self.addPeopleButton.config(image=self.addPeopleButtonIcon, compound='left')
        self.addPeopleButton.place(x=250, y=70)

        self.aboutUsButtonIcon = PhotoImage(file='AddressBook/icons/info.png')
        self.aboutUsButton = Button(self.bottomFrame, text='About Us', font='arial 12 bold', command=self.openAbout)
        self.aboutUsButton.config(image=self.addPeopleButtonIcon, compound='left')
        self.aboutUsButton.place(x=250, y=130)
    
    def openMyPeople(self):
        myPeople = mypeople.MyPeople()
    
    def openAddPeople(self):
        addPeople = addpeople.AddPeople()
    
    def openAbout(self):
        about = aboutPage.About()

def main():
    root = Tk()
    app = Application(root)
    root.title('Address Book App')
    root.geometry('650x650+350+200')
    root.resizable(False, False)
    root.bind('<Escape>', lambda x: closeWindow(root))
    root.mainloop()

def closeWindow(x): x.destroy()

if __name__ == '__main__':
    main()