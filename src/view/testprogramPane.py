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

    def __init__(self, master, path=None, name='No TP Loaded'):
        '''
        Constructor
        '''
        Labelframe.__init__(self, master)
        self.name = name
        self.path = path
        self.tp = Tp()
        self.tree = Treeview(self)
        self.tree.pack(fill=BOTH, expand=True)
        self.config(width=200, height=300, relief=RIDGE, text=name, padding=10)
        self.tree.bind('<<TreeviewSelect>>', self.show_params)
        self.param_view = Labelframe(self)
        self.params = {}
        self.load()

    def load(self):
        self.tree.delete(*self.tree.get_children())
        if (self.path == None):
            self.tree.insert("", 'end', 'Default', text=self.name)  
        else:
            fileHandler = FileHandler(self.path)
            self.tp = fileHandler.load(self.tp)
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
            if (element.getparent() == None):
                self.tree.insert("", 'end', element.get("name"), text=element.get("name"))
            else:
                self.tree.insert(element.getparent().get("name"), 'end', element.get("name"), text=element.get("name"))
                if (element.tag == 'Test'):
                    self.params[element.get("name")] = {
                        'delay': element.get('delay'),
                        'force': element.get('force'),
                        'lolim': element.get('lolim'),
                        'hilim': element.get('hilim'),
                        'pinref': element.get('pinref'),
                        'testtype': element.get('testtype')
                        }
        
    def load_params(self, master, test):
        master.config(text = test)
        param_tree = Treeview(master)
        param_tree.pack(fill=BOTH, expand=True)
        param_tree.heading('#0', text = 'Parameter')
        param_tree.insert('', 'end', 'delay', text = 'DELAY')
        param_tree.insert('', 'end', 'force', text = 'FORCE')
        param_tree.insert('', 'end', 'lolim', text = 'LOLIM')
        param_tree.insert('', 'end', 'hilim', text = 'HILIM')
        param_tree.insert('', 'end', 'pinref', text = 'PINREF')
        param_tree.insert('', 'end', 'testtype', text = 'TESTTYPE')
        
        param_tree.config(columns=('value'))
        param_tree.column('value', width = 100)
        param_tree.heading('value', text = 'Value')
        param_tree.set('delay', 'value', self.params.get(test).get('delay'))
        param_tree.set('force', 'value', self.params.get(test).get('force'))
        param_tree.set('lolim', 'value', self.params.get(test).get('lolim'))
        param_tree.set('hilim', 'value', self.params.get(test).get('hilim'))
        param_tree.set('pinref', 'value', self.params.get(test).get('pinref'))
        param_tree.set('testtype', 'value', self.params.get(test).get('testtype'))
        
        
