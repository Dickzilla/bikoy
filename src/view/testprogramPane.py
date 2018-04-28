'''
Created on 9 Apr 2018

@author: BIKOYPOGI
'''
from tkinter.ttk import Labelframe, Treeview
from tkinter.constants import RIDGE, BOTH


class TestprogramPane(Labelframe):
    '''
    classdocs
    '''

    def __init__(self, master, tp=None, name='No TP Loaded'):
        '''
        Constructor
        '''
        Labelframe.__init__(self, master)
        self.name = name
        self.tp = tp
        self.tree = Treeview(self)
        self.tree.pack(fill=BOTH, expand=True)
        self.config(width=200, height=200, relief=RIDGE, text='Test Program', padding=10)
        self.tree.bind('<<TreeviewSelect>>', self.show_params)
        self.param_view = Labelframe(self)
        self.pins_view = Labelframe(self)
        self.params = {}
        self.pins = {}
        self.load()

    def load(self):
        self.tree.delete(*self.tree.get_children())
        if (self.tp == None):
            self.tree.insert("", 'end', 'Default', text=self.name)  
        else:
            self.populate(self.tp.testtree)
            
    def show_params(self, event):
        self.param_view.destroy()
        if (self.params.get(self.tree.selection()[0], None) != None):
            self.param_view = Labelframe(self)
            self.load_params(self.param_view, self.tree.selection()[0])
            self.param_view.config(text='Test Parameters')
            self.param_view.pack(fill=BOTH, expand=True)
        
    def populate(self, tp):
        for element in tp.iter():
            if (element.tag == 'TestRef'):
                self.tree.insert("", 'end', element.get("name"), text=element.get("name"), open=True)
            else:
                self.tree.insert(element.getparent().get("name"), 'end', element.get("name"), text=element.get("name"), open=True)
                if (element.tag == 'Test'):
                    self.params[element.get("name")] = {
                        'delay': element.get('delay'),
                        'force': element.get('force'),
                        'lolim': element.get('lolim'),
                        'hilim': element.get('hilim'),
                        'pinref': element.get('pinref'),
                        'testtype': element.get('testtype')
                        }
                    
    def fetch_pins(self, tp, pinref):
        for element in tp.iter():
            if (element.get("name") == pinref):
                self.pins[element.get("name")] = {
                        'pintype': element.get("pintype"),
                        'pins': []
                        }
            else:
                if (element.tag == 'Pin' and element.getparent().get("name") == pinref):
                    self.pins[pinref].get('pins').append(element.get("name"))
# 
        
    def load_params(self, master, test):
        master.config(text = test)
        self.param_tree = Treeview(master)
        self.param_tree.pack(fill=BOTH, expand=True)
        self.param_tree.heading('#0', text = 'Parameter')
        self.param_tree.config(columns=('value'))
        self.param_tree.column('value', width = 100)
        self.param_tree.heading('value', text = 'Value')
        
        self.param_tree.insert('', 'end', 'delay', text = 'DELAY', values = self.params.get(test).get('delay'))
        self.param_tree.insert('', 'end', 'force', text = 'FORCE', values = self.params.get(test).get('force'))
        self.param_tree.insert('', 'end', 'lolim', text = 'LOLIM', values = self.params.get(test).get('lolim'))
        self.param_tree.insert('', 'end', 'hilim', text = 'HILIM', values = self.params.get(test).get('hilim'))
        self.param_tree.insert('', 'end', 'pinref', text = 'PINREF', values = self.params.get(test).get('pinref'))
        self.param_tree.insert('', 'end', 'testtype', text = 'TESTTYPE', values = self.params.get(test).get('testtype'))
        if self.pins_view : self.pins_view.destroy()
        self.pins_view = Labelframe(self)
        self.param_tree.bind('<<TreeviewSelect>>', self.show_pins)
        
    def show_pins(self, event):
        self.pins_view.destroy()
        self.pins_view = Labelframe(self)
        pinref = self.param_tree.item(self.param_tree.selection()[0], "value")[0]
        self.fetch_pins(self.tp.pintree, pinref)
        if (self.pins.get(pinref, None) != None):
            self.pins_view = Labelframe(self)
            self.load_pins(self.pins_view, pinref)
            self.pins_view.config(text='Pin Parameters')
            self.pins_view.pack(fill=BOTH, expand=True)
        
    def load_pins(self, master, pinref):
        pins_tree = Treeview(master)
        pins_tree.pack(fill=BOTH, expand=True)
        pins_tree.heading('#0', text = (next(iter(self.pins)), ' PinType: ', self.pins.get(pinref).get('pintype')))
        for p in self.pins.get(pinref).get('pins'):
            pins_tree.insert('', 'end', p, text = p)      
