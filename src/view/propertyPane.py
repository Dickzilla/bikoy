'''
Created on 9 Apr 2018

@author: BIKOYPOGI
'''
from tkinter.ttk import Labelframe, Treeview, Style
# from testprogram.tests.testFlow import TestFlow
# from controller.fileHandler import FileHandler
from tkinter.constants import RIDGE, BOTH

class PropertyPane(Labelframe):
    '''
    classdocs
    '''


    def __init__(self, master, name):
        '''
        Constructor
        '''
        Labelframe.__init__(self, master)
        self.config(width=400, height=300, relief=RIDGE, text=name, padding=10)
#         fileHandler = FileHandler(testProgram)
#         self.testFlow = fileHandler.load()
#         tp = self.testFlow.name


        tree = Treeview(self)
        tree.pack(fill=BOTH, expand=True)
        tree.heading('#0', text = 'Property')
        tree.insert('', 'end', 'pinrefs', text = 'PINREFS', open = True)
        tree.insert('pinrefs', 'end', 'pins', text = 'PINS', open = True)
        tree.insert('pins', 'end', 'PWROK', text = 'PWROK')
        tree.insert('pins', 'end', 'RST_L', text = 'RST_L')
        tree.insert('pinrefs', 'end', 'pingroups', text = 'PINGROUPS', open = True)
        tree.insert('pingroups', 'end', 'GpioPins', text = 'GpioPins')
        tree.insert('', 'end', 'params', text = 'PARAMS', open = True)
        tree.insert('params', 'end', 'lolim', text = 'LOW_LIMIT')
        tree.insert('params', 'end', 'hilim', text = 'HIGH_LIMIT')
        tree.insert('params', 'end', 'sweepStart', text = 'SWEEP_START')
        tree.insert('params', 'end', 'sweepEnd', text = 'SWEEP_END')
        tree.insert('params', 'end', 'stepSize', text = 'STEP_SIZE')
        
        tree.config(columns=('value'))
        tree.column('value', width = 200)
        tree.heading('value', text = 'Values')
        
        tree.set('GpioPins', 'value', 'TCK, TMS')
        tree.set('lolim', 'value', '200mV')
        tree.set('hilim', 'value', '1.5V')
        tree.set('sweepStart', 'value', '10uA')
        tree.set('sweepEnd', 'value', '400uA')
        tree.set('stepSize', 'value', '4uA')
        
        
#         test = self.testFlow.tests.pop()
#         tree.insert(self.testFlow.name, 'end', text=test)
        
    
        