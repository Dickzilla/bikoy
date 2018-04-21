'''
Created on 12 Apr 2018

@author: BIKOYPOGI
'''
from tkinter.ttk import Frame, Panedwindow, Labelframe
from tkinter.constants import HORIZONTAL, BOTH
from view.testprogramPane import TestprogramPane
from view.propertyPane import PropertyPane

class MainBody(Frame):
    '''
    classdocs
    '''

    def __init__(self, master, name = 'Test Program'):
        Frame.__init__(self, master)
        self.name = name
        self.window = Panedwindow(self, orient=HORIZONTAL)
        self.lframe = Labelframe(self)
        self.rframe = Labelframe(self)
        
    def show(self):
        self.lframe = TestprogramPane(self, '/Users/BIKOYPOGI/eclipse-workspace/ost/src/repo/tests.xml')
        self.lframe.config(text=self.name)
        self.rframe = PropertyPane(self, 'Test Properties')
        self.window.pack(fill=BOTH, expand=True)
        self.window.add(self.lframe, weight=1)
        self.window.add(self.rframe, weight=1)
        
        
        
        