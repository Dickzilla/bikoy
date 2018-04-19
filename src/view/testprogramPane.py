'''
Created on 9 Apr 2018

@author: BIKOYPOGI
'''
from tkinter.ttk import Labelframe, Treeview
from testprogram.tp import Tp
from controller.fileHandler import FileHandler
from tkinter.constants import RIDGE, BOTH

class TestprogramPane(Labelframe):
    '''
    classdocs
    '''


    def __init__(self, master, path: str):
        '''
        Constructor
        '''
        Labelframe.__init__(self, master)
        fileHandler = FileHandler(path)
        self.tp = Tp()
        self.tp = fileHandler.load(self.tp)
        print(self.tp.testref.name)
        self.config(width=200, height=300, relief=RIDGE, text=self.tp.testref.name, padding=10)
        self.tree = Treeview(self)
        self.populate(self.tp.tree)
        self.tree.pack(fill=BOTH, expand=True)

        
    def populate(self, tp):
        for element in tp.iter():
            if (element.getparent() == None):
                print(element.getparent(), element.get("name"))
                self.tree.insert("", 'end', element.get("name"))
            else:
                print(element.getparent().get("name"), element.tag, element.get("name"))
                self.tree.insert(element.getparent().get("name"), 'end', element.get("name"))
        
#         test = self.testFlow.tests.pop()
#         tree.insert(self.testFlow.name, 'end', text=test)
        
    
        