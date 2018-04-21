'''
Created on 9 Apr 2018

@author: BIKOYPOGI
'''
from testprogram.tp import Tp


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
        if (root.getroot().tag == 'PinRef'):
            tp.pintree = root
        elif (root.getroot().tag == 'TestRef'):
            tp.testtree = root
        return tp
        