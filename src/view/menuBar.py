'''
Created on 8 Apr 2018

@author: BIKOYPOGI
'''
from tkinter import Menu
import resources.props as props

class MenuBar(Menu):
    '''
    classdocs
    '''

    def __init__(self, master):
        Menu.__init__(self, master, tearoff=0)
        self.master = master
        
        file = Menu(master, tearoff=0)
        self.add_cascade(label= props.fileMenuLabel, menu = file)
        file.add_command(label = props.fileLoadCommand)
        file.add_command(label = props.fileUnloadCommand)
        
        testProgram = Menu(master, tearoff=0)
        self.add_cascade(label= props.testProgramMenuLabel, menu = testProgram)
        testProgram.add_command(label = props.testProgramPinsCommand)
        testProgram.add_command(label = props.testProgramPingroupsCommand)
        
        run = Menu(master, tearoff=0)
        self.add_cascade(label= props.runMenuLabel, menu = run)
        run.add_command(label = props.runAllCommand)
        run.add_command(label = props.runIoCommand)
        run.add_command(label = props.runPwrCommand)
        
        result = Menu(master, tearoff=0)
        self.add_cascade(label= props.resultMenuLabel, menu = result)
        result.add_command(label = props.resultIoCommand)
        result.add_command(label = props.resultPwrCommand)
        
        
        