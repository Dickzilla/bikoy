'''
Created on 12 Apr 2018

@author: BIKOYPOGI
'''
from tkinter.ttk import Frame, Panedwindow
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
        self.show_default(self.name)
        
    def show_default(self, name):
        self.window = Panedwindow(self, orient=HORIZONTAL)
        self.window.pack(fill=BOTH, expand=True)
        lframe = TestprogramPane(self, '/Users/BIKOYPOGI/eclipse-workspace/ost/src/repo/tests.xml')
        rframe = PropertyPane(self, 'Test Properties')
        self.window.add(lframe, weight=1)
        self.window.add(rframe, weight=1)
        
        
        
        