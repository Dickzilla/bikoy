'''
Created on 8 Apr 2018

@author: BIKOYPOGI
'''

class PinRef:
    '''
    This is a generic type pin reference.
    
    Attributes:
        name       String name of this pin or pingroup, either IO or PWR types
    '''


    def __init__(self, name: str = ''):
        '''
        Constructor
        '''
        self.name = name
        