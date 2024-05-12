from tkinter import *

class About(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry('650x650+450+200')
        self.title('My People')
        self.resizable(False, False)
        frame = Frame(self,bg='#ffa500',width=550,height=550)
        frame.pack(fill=BOTH)
        text = Label(frame,text='This is our about us page you find more'
                              '\ninformation about us here'
                              '\nthis application was created for educational purposes'
                              '\nand we have learned a lot :)',font='ariall 14 bold',bg='#ffa500',fg='white')

        text.place(x=50,y=50)
        self.bind('<Escape>', lambda x: self.closeWindow())
    
    def closeWindow(self): self.destroy()


# class About:
#     def __init__(self,root):
#         self.root = root
#         frame=Frame(root,bg='#ffa500',width=550,height=550)
#         frame.pack(fill=BOTH)
        # text=Label(frame,text='This is our about us page you find more'
        #                       '\ninformation about us here'
        #                       '\nthis application was created for educational purposes'
        #                       '\nand we have learned a lot :)',
        #            font='ariall 14 bold',bg='#ffa500',fg='white')

        # text.place(x=50,y=50)
