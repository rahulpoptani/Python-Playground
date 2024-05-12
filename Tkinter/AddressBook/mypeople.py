from tkinter import *
from tkinter import messagebox
import addpeople
from helper.helper import Helper

class MyPeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry('650x650+450+200')
        self.title('My People')
        self.resizable(False, False)
        self.bind('<Escape>', lambda x: self.closeWindow())

        # Frames
        self.topFrame = Frame(self, height=150, bg='white')
        self.topFrame.pack(fill=X)
        self.bottomFrame = Frame(self, height=500, bg='#fcc324')
        self.bottomFrame.pack(fill=X)

        # Heading, Image
        self.top_image = PhotoImage(file='AddressBook/icons/person_icon.png')
        self.top_image_label = Label(self.topFrame, image=self.top_image, bg='white')
        self.top_image_label.place(x=120, y=10)

        self.heading_label = Label(self.topFrame, text='My Peoples', font='arial 15 bold', fg='#003f8a', bg='white')
        self.heading_label.place(x=260, y=60)

        # List Box
        self.listBox = Listbox(self.bottomFrame, width=50, height=30)
        self.listBox.grid(row=0, column=0, padx=(40,0))

        # Scroll Bar
        self.sb = Scrollbar(self.bottomFrame, orient='vertical')
        self.sb.config(command=self.listBox.yview)
        self.listBox.config(yscrollcommand=self.sb.set)
        self.sb.grid(row=0, column=1, sticky=N+S)

        # Buttons
        buttonAdd = Button(self.bottomFrame, text='Add', width=12, font='Sans 12 bold', command=self.openAddPeople)
        buttonAdd.grid(row=0, column=2, sticky=N, padx=10, pady=10)
        
        buttonUpdate = Button(self.bottomFrame, text='Update', width=12, font='Sans 12 bold', command=self.updatePeople)
        buttonUpdate.grid(row=0, column=2, sticky=N, padx=10, pady=50)
        
        buttondisplay = Button(self.bottomFrame, text='Display', width=12, font='Sans 12 bold', command=self.displayPeople)
        buttondisplay.grid(row=0, column=2, sticky=N, padx=10, pady=90)
        
        buttonDelete = Button(self.bottomFrame, text='Delete', width=12, font='Sans 12 bold', command=self.deletePeople)
        buttonDelete.grid(row=0, column=2, sticky=N, padx=10, pady=130)

        # Populate List Box
        self.populateListBox()
    
    def populateListBox(self):
        allPeoples = Helper.executeQuery('SELECT * FROM PEOPLE')
        count = 0
        for people in allPeoples:
            self.listBox.insert(count, str(people[0]) + '-' + people[1] + ' ' + people[2])
            count += 1
    
    def closeWindow(self): self.destroy()

    def openAddPeople(self): 
        addPeople = addpeople.AddPeople()
        self.destroy()
    
    def updatePeople(self):
        current_selection = self.listBox.curselection()
        if current_selection:
            current_person = self.listBox.get(current_selection)
            person_id = current_person.split('-')[0]
            addpeople.AddPeople().populateEntries(person_id, True)
            self.destroy()
    
    def displayPeople(self):
        current_selection = self.listBox.curselection()
        if current_selection:
            current_person = self.listBox.get(current_selection)
            person_id = current_person.split('-')[0]
            addpeople.AddPeople().populateEntries(person_id, False)
            self.destroy()
    
    def deletePeople(self):
        current_selection = self.listBox.curselection()
        if current_selection:
            current_person = self.listBox.get(current_selection)
            person_id = current_person.split('-')[0]
            mbox = messagebox.askquestion('warning', 'Are you sure you want to delete the person?', icon='warning')
            if mbox == 'yes':
                Helper.executeQuery('DELETE FROM PEOPLE WHERE PEOPLE_ID = ?', (person_id))
                self.listBox.delete(0, END)
                self.populateListBox()




