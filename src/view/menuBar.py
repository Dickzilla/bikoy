'''
Created on 8 Apr 2018

@author: BIKOYPOGI
'''
from tkinter import Menu
import resources.props as props
# from testprogram.tests.testFlow import TestFlow
# from view.testprogramPane import FileMenu

class MenuBar(Menu):
    '''
    classdocs
    '''

    def __init__(self, master):
        Menu.__init__(self, master)
        self.master = master
        
        file = Menu(master)
        self.add_cascade(label= props.fileMenuLabel, menu = file)
        file.add_command(label = props.fileLoadCommand)
        file.add_command(label = props.fileUnloadCommand)
        
        testProgram = Menu(master)
        self.add_cascade(label= props.testProgramMenuLabel, menu = testProgram)
        testProgram.add_command(label = props.testProgramIoPinsCommand)
        testProgram.add_command(label = props.testProgramIoPingroupsCommand)
        testProgram.add_separator()
        testProgram.add_command(label = props.testProgramPwrPinsCommand)
        testProgram.add_command(label = props.testProgramPwrPingroupsCommand)
        testProgram.add_separator()
        testProgram.add_command(label = props.testProgramIoTestsCommand)
        testProgram.add_command(label = props.testProgramPwrTestsCommand)
        
        run = Menu(master)
        self.add_cascade(label= props.runMenuLabel, menu = run)
        run.add_command(label = props.runAllCommand)
        run.add_command(label = props.runIoCommand)
        run.add_command(label = props.runPwrCommand)
        
        result = Menu(master)
        self.add_cascade(label= props.resultMenuLabel, menu = result)
        result.add_command(label = props.resultIoCommand)
        result.add_command(label = props.resultPwrCommand)
        
#     def displayFlow(self, master, testFlow):
#         fileMenu = FileMenu(master, testFlow)
        
        