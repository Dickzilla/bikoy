'''
Created on 9 Apr 2018

@author: BIKOYPOGI
'''
from tkinter.ttk import Labelframe, Treeview
from tkinter.constants import RIDGE, BOTH

class PinsPane(Labelframe):
    '''
    classdocs
    '''


    def __init__(self, master, tp=None, name='Load TP -> Select Pinref'):
        '''
        Constructor
        '''
        Labelframe.__init__(self, master)
        self.name = name
        self.tp = tp
        self.tree = Treeview(self)
        self.tree.pack(fill=BOTH, expand=True)
        self.config(width=400, height=300, relief=RIDGE, text='Pin Definitions', padding=10)
#         self.tree.bind('<<TreeviewSelect>>', self.show_pinss)
#         self.pin_view = Labelframe(self)
        self.pins = {}
        self.pingroups = {}
        self.load()

    def load(self):
        self.tree.delete(*self.tree.get_children())
        if (self.tp == None):
            self.tree.insert("", 'end', 'Default', text=self.name)  
        else:
            self.populate(self.tp.pintree)
            
    def populate(self, tp):
        for element in tp.iter():
            if (element.tag == 'PinRef'):
                self.tree.insert("", 'end', element.get("name"), text=element.get("name"), open=True)
            else:
                if (element.tag == 'PinGroup'):
                    self.tree.insert(element.getparent().get("name"), 'end', element.get("name"), text=element.get("name"), open=True)
                    self.pingroups[element.get("name")] = {
                        'pintype': element.get("pintype"),
                        'pins': []
                        }
                elif (element.tag == 'Pins'):
                    self.tree.insert(element.getparent().get("name"), 'end', element.get("name"), text=element.get("name"), open=True)
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

        
        
        
    
        