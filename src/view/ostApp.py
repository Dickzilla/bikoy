from tkinter import *
import resources.props as props
from view import menuBar

class OstApp(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master, relief=RIDGE, bd=2)   
        self.master=master
        self.init_window()
        
    def init_window(self):
        self.master.title(props.mainTitle)
        menubar = menuBar.MenuBar(self.master)
        self.master.config(menu=menubar)
        self.pack()

        