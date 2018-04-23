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
        if (fullpath != None): self.fullpath = fullpath
                
    def load(self, tp=None):
        if tp is None: tp = Tp()
        self.tp = self.parse(self.fullpath, tp)
        return self.tp
            
    def parse(self, fullpath, oldtp):
        from lxml import etree
        root = etree.parse(fullpath)
        if (root.getroot().tag == 'Testprogram'):
            temp = Tp()
            for item in root.getroot().getchildren():
                newtp = self.split(item, temp)
        else:
            newtp = self.split(root.getroot(), oldtp)
        return newtp

    def split(self, root, tp):
        print(root.tag, ' => ' , root.get("name"))
        if (root.tag == 'PinRef'):
            tp.pintree = root
        elif (root.tag == 'TestRef'):
            tp.testtree = root
        return tp

        