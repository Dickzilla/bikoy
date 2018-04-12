'''
Created on 9 Apr 2018

@author: BIKOYPOGI
'''
from tkinter.ttk import Labelframe, Treeview
# from testprogram.tests.testFlow import TestFlow
# from controller.fileHandler import FileHandler
from tkinter.constants import RIDGE, BOTH

class TestprogramPane(Labelframe):
    '''
    classdocs
    '''


    def __init__(self, master, testProgram):
        '''
        Constructor
        '''
        Labelframe.__init__(self, master)
        self.config(width=200, height=300, relief=RIDGE, text=testProgram, padding=10)
#         fileHandler = FileHandler(testProgram)
#         self.testFlow = fileHandler.load()
#         tp = self.testFlow.name

        tree = Treeview(self)
        tree.pack(fill=BOTH, expand=True)
        tree.insert('', 'end', 'start', text = 'START')
        tree.insert('', 'end', 'test1', text = 'Vdd18_PsShorts')
        tree.insert('', 'end', 'test2', text = 'Gpio18_PinCont', open = True)
        tree.insert('', 'end', 'end', text = 'END')
        tree.insert('test2', 'end', 'subtest1', text = 'Gpio18_Opens')
        tree.insert('test2', 'end', 'subtest2', text = 'Gpio18_Shorts')
        
        tree.heading('#0', text = 'Test Instance')
        tree.config(columns=('type'))
        tree.column('type', width = 200)
        tree.heading('type', text = 'Instance Type')
        
        tree.set('start', 'type', 'Start Device')
        tree.set('test1', 'type', 'Test Reference')
        tree.set('test2', 'type', 'Flow Reference')
        tree.set('subtest1', 'type', 'Test Reference')
        tree.set('subtest2', 'type', 'Test Reference')
        tree.set('end', 'type', 'End Device')
        
        
        
#         test = self.testFlow.tests.pop()
#         tree.insert(self.testFlow.name, 'end', text=test)
        
    
        