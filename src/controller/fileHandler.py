'''
Created on 9 Apr 2018

@author: BIKOYPOGI
'''
from testprogram.tp import Tp
from testprogram.pins.pinRef import PinRef
from testprogram.tests.testFlow import TestFlow


class FileHandler:
    '''
    This class handles all file processing.
    
    Attributes:
        filepath   Directory and filename in dirPath/fileName.ext format
    '''


    def __init__(self, fullpath = None):
        '''
        Constructor
        '''
        if (fullpath != None):
            self.fullpath = fullpath
                
    def load(self, tp: Tp) -> Tp:
        self.tp = self.parse(self.fullpath, tp)
        return self.tp
            
    def parse(self, fullpath: str, tp: Tp) -> Tp:
        from lxml import etree
        root = etree.parse(fullpath)
        # Print the loaded XML
        if isinstance(root, PinRef):
            tp.pinref = root
        elif isinstance(root, TestFlow):
            tp.testflow = root
        tp.testtree = root
        return tp
        