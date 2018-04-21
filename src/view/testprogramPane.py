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




    def __init__(self, master, path=None, name = 'No TP Loaded'):
        '''
        Constructor
        '''
        Labelframe.__init__(self, master)
        self.tp = Tp()
        self.tree = Treeview(self)
        self.tree.pack(fill=BOTH, expand=True)
        self.tree.delete(*self.tree.get_children())
        if (path != None):
            self.load(path)
        else:
            self.tree.insert("", 'end', 'Default', text=name)  
        self.config(width=200, height=300, relief=RIDGE, text=name, padding=10)

    def load(self, path):
        fileHandler = FileHandler(path)
        self.tp = fileHandler.load(self.tp)
        self.populate(self.tp.testtree)
        
    def populate(self, tp):
        for element in tp.iter():
            if (element.getparent() == None):
                self.tree.insert("", 'end', element.get("name"), text=element.get("name"))
            else:
                self.tree.insert(element.getparent().get("name"), 'end', element.get("name"), text=element.get("name"))
        
#         test = self.testFlow.tests.pop()
#         tree.insert(self.testFlow.name, 'end', text=test)
        
    
        