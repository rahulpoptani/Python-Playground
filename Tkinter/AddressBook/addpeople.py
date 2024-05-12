from tkinter import *
from tkinter import messagebox
from helper.helper import Helper

class AddPeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry('650x650+550+200')
        self.title('Add People')
        self.resizable(False, False)
        self.bind('<Escape>', lambda x: self.closeWindow())

        # Frames
        self.topFrame = Frame(self, height=150, bg='white')
        self.topFrame.pack(fill=X)
        self.bottomFrame = Frame(self, height=500, bg='#fcc324')
        self.bottomFrame.pack(fill=X)

        # Heading, Image
        self.top_image = PhotoImage(file='AddressBook/icons/addperson.png')
        self.top_image_label = Label(self.topFrame, image=self.top_image, bg='white')
        self.top_image_label.place(x=120, y=10)

        self.heading_label = Label(self.topFrame, text='Add/Update People', font='arial 15 bold', fg='#003f8a', bg='white')
        self.heading_label.place(x=260, y=60)

        # Lables, Entries and Save Button
        self.label_name = Label(self.bottomFrame, text='Name', font='arial 15 bold', fg='white', bg='#fcc324')
        self.label_name.place(x=40, y=40)
        self.entry_name = Entry(self.bottomFrame, width=30, bd=4)
        self.entry_name.place(x=150, y=40)

        self.label_surname = Label(self.bottomFrame, text='Surname', font='arial 15 bold', fg='white', bg='#fcc324')
        self.label_surname.place(x=40, y=80)
        self.entry_surname = Entry(self.bottomFrame, width=30, bd=4)
        self.entry_surname.place(x=150, y=80)

        self.label_email = Label(self.bottomFrame, text='Email', font='arial 15 bold', fg='white', bg='#fcc324')
        self.label_email.place(x=40, y=120)
        self.entry_email = Entry(self.bottomFrame, width=30, bd=4)
        self.entry_email.place(x=150, y=120)

        self.label_phone = Label(self.bottomFrame, text='Phone', font='arial 15 bold', fg='white', bg='#fcc324')
        self.label_phone.place(x=40, y=160)
        self.entry_phone = Entry(self.bottomFrame, width=30, bd=4)
        self.entry_phone.place(x=150, y=160)

        self.label_address = Label(self.bottomFrame, text='Address', font='arial 15 bold', fg='white', bg='#fcc324')
        self.label_address.place(x=40, y=200)
        self.text_address = Text(self.bottomFrame, width=30, height=10, wrap='word', bd=4)
        self.text_address.place(x=150, y=200)

        self.saveButton = Button(self.bottomFrame, text='Save', command=self.addPerson)
        self.saveButton.place(x=270, y=460)
    
    def addPerson(self):
        name = self.entry_name.get()
        surname = self.entry_surname.get()
        email = self.entry_email.get()
        phone = self.entry_phone.get()
        address = self.text_address.get(1.0, END) # 'end-1c'
        
        if name and surname and email and phone and address != '':
            try: 
                if self.person_id:
                    query = 'UPDATE PEOPLE SET FNAME = ?, LNAME = ?, EMAIL = ?, PHONE = ?, ADDRESS = ? WHERE PEOPLE_ID = ?'
                    Helper.executeQuery(query, (name, surname, email, phone, address, self.person_id))
                else:
                    query = 'INSERT INTO PEOPLE (FNAME, LNAME, EMAIL, PHONE, ADDRESS) VALUES (?, ?, ?, ?, ?)'
                    Helper.executeQuery(query, (name, surname, email, phone, address))
                response = messagebox.showinfo('Success', 'Successfully added to database', icon='info')
                if response == 'ok': self.destroy()
            except Exception as ex:
                print(ex)
                messagebox.showerror('Error', 'Cannot add to database', icon='warning')
        else:
            messagebox.showerror('Error', 'Fields cannot be empty', icon='warning')
    
    def populateEntries(self, id, updatable):
        query = 'SELECT FNAME, LNAME, EMAIL, PHONE, ADDRESS FROM PEOPLE WHERE PEOPLE_ID = ?'
        resultset = Helper.executeQuery(query, (id))[0]
        fname, surname, email, phone, address = resultset
        self.person_id = id
        self.entry_name.insert(0, fname)
        self.entry_surname.insert(0, surname)
        self.entry_email.insert(0, email)
        self.entry_phone.insert(0, phone)
        self.text_address.insert(1.0, address)
        if not updatable: 
            self.entry_name.config(state='disabled')
            self.entry_surname.config(state='disabled')
            self.entry_email.config(state='disabled')
            self.entry_phone.config(state='disabled')
            self.text_address.config(state='disabled')
            self.saveButton.config(state='disabled')

    def closeWindow(self): self.destroy()

