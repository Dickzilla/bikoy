'''
Created on 9 Apr 2018

@author: BIKOYPOGI
'''
from tkinter.ttk import Labelframe, Treeview
from testprogram.tp import Tp
from controller.fileHandler import FileHandler
from tkinter.constants import RIDGE, BOTH
from lxml import etree

class PinsPane(Labelframe):
    '''
    classdocs
    '''


    def __init__(self, master, name='Load TP -> Select Pinref'):
        '''
        Constructor
        '''
        Labelframe.__init__(self, master)
        self.name = name
        self.path = '/Users/BIKOYPOGI/eclipse-workspace/ost/src/repo/pins.xml'
        self.tp = Tp()
        self.tree = Treeview(self)
        self.tree.pack(fill=BOTH, expand=True)
        self.config(width=400, height=300, relief=RIDGE, text=name, padding=10)
#         self.tree.bind('<<TreeviewSelect>>', self.show_pinss)
#         self.pin_view = Labelframe(self)
        self.pins = {}
        self.pingroups = {}
        self.load()

    def load(self):
        self.tree.delete(*self.tree.get_children())
        if (self.path == None):
            self.tree.insert("", 'end', 'Default', text=self.name)  
        else:
            fileHandler = FileHandler(self.path)
            self.tp = fileHandler.load(self.tp)
            self.populate(self.tp.pintree)
            
    def populate(self, tp):
        for element in tp.iter():
            if (element.getparent() == None):
                self.tree.insert("", 'end', element.get("name"), text=element.get("name"))
            else:
                if (element.tag == 'PinGroup'):
                    self.tree.insert(element.getparent().get("name"), 'end', element.get("name"), text=element.get("name"))
                    self.pingroups[element.get("name")] = {
                        'pintype': element.get("pintype"),
                        'pins': []
                        }
                elif (element.tag == 'Pins'):
                    self.tree.insert(element.getparent().get("name"), 'end', element.get("name"), text=element.get("name"))
                    self.pingroups[element.get("name")] = {
                        'pins': []
                        }
                elif (element.tag == 'Pin' and element.getparent().tag == 'Pins'):
                    self.tree.insert(element.getparent().get("name"), 'end', 
                                     (element.getparent().get("name")+'.'+element.get("name")), text=element.get("name"))
                    self.pingroups[element.get("name")] = {
                        'channel': element.get('channel'),
                        'pintype': element.get('pintype')
                        }
                elif (element.tag == 'Pin' and element.getparent().tag == 'PinGroup'):
                    self.tree.insert(element.getparent().get("name"), 'end', 
                                     (element.getparent().get("name")+'.'+element.get("name")), text=element.get("name"))
                    self.pingroups[element.getparent().get('name')].get('pins').append(element.get("name"))
# 
#         tree = Treeview(self)
#         tree.pack(fill=BOTH, expand=True)
#         tree.heading('#0', text = 'Property')
#         tree.insert('', 'end', 'pinrefs', text = 'PINREFS', open = True)
#         tree.insert('pinrefs', 'end', 'pins', text = 'PINS', open = True)
#         tree.insert('pins', 'end', 'PWROK', text = 'PWROK')
#         tree.insert('pins', 'end', 'RST_L', text = 'RST_L')
#         tree.insert('pinrefs', 'end', 'pingroups', text = 'PINGROUPS', open = True)
#         tree.insert('pingroups', 'end', 'GpioPins', text = 'GpioPins')
#         tree.insert('', 'end', 'params', text = 'PARAMS', open = True)
#         tree.insert('params', 'end', 'lolim', text = 'LOW_LIMIT')
#         tree.insert('params', 'end', 'hilim', text = 'HIGH_LIMIT')
#         tree.insert('params', 'end', 'sweepStart', text = 'SWEEP_START')
#         tree.insert('params', 'end', 'sweepEnd', text = 'SWEEP_END')
#         tree.insert('params', 'end', 'stepSize', text = 'STEP_SIZE')
#         
#         tree.config(columns=('value'))
#         tree.column('value', width = 200)
#         tree.heading('value', text = 'Values')
#         
#         tree.set('GpioPins', 'value', 'TCK, TMS')
#         tree.set('lolim', 'value', '200mV')
#         tree.set('hilim', 'value', '1.5V')
#         tree.set('sweepStart', 'value', '10uA')
#         tree.set('sweepEnd', 'value', '400uA')
#         tree.set('stepSize', 'value', '4uA')
        
        
        
    
        