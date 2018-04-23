import resources.props as props
from view import menuBar
from view.mainBody import MainBody
from tkinter.constants import BOTH

class OstApp():

    def __init__(self, master=None):
        self.master=master
        self.init_app()
        self.tp = None
        
    def init_app(self):
        self.master.title(props.mainTitle)
        self.master.geometry("600x300")
        menubar = menuBar.MenuBar(self)
        self.master.config(menu=menubar)
        self.master.iconbitmap('resources/image/koala_icon.ico')
        
        self.mainBody = MainBody(self)
        self.mainBody.show()
        self.mainBody.pack(fill=BOTH, expand=True)

        