from tkinter import *

class Helper:
    def getImage(name: str) -> PhotoImage:
        return PhotoImage(file=f'BillingManagement/icons/{name}')