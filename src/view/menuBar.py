'''
Created on 8 Apr 2018

@author: BIKOYPOGI
'''
from tkinter import Menu, filedialog
import resources.props as props
from view.testprogramPane import TestprogramPane
from tkinter.ttk import Panedwindow
from tkinter.constants import HORIZONTAL
from view.pinsPane import PinsPane
from view.mainBody import MainBody
# from testprogram.tests.testFlow import TestFlow
# from view.testprogramPane import FileMenu

class MenuBar(Menu):
    '''
    classdocs
    '''

    def __init__(self, parent):
        Menu.__init__(self, parent.master)
        self.parent = parent
        self.option_add('*tearOff', False)
        
        file = Menu(parent.master)
        self.add_cascade(label= props.fileMenuLabel, menu = file)
        file.add_command(label = props.fileLoadCommand, command=self.load)
        file.add_command(label = props.fileUnloadCommand, command=self.unload)
        
        testProgram = Menu(parent.master)
        self.add_cascade(label= props.testProgramMenuLabel, menu = testProgram)
        testProgram.add_command(label = props.testProgramIoPinsCommand)
        testProgram.add_command(label = props.testProgramIoPingroupsCommand)
        testProgram.add_separator()
        testProgram.add_command(label = props.testProgramPwrPinsCommand)
        testProgram.add_command(label = props.testProgramPwrPingroupsCommand)
        testProgram.add_separator()
        testProgram.add_command(label = props.testProgramIoTestsCommand)
        testProgram.add_command(label = props.testProgramPwrTestsCommand)
        
        run = Menu(parent.master)
        self.add_cascade(label= props.runMenuLabel, menu = run)
        run.add_command(label = props.runAllCommand)
        run.add_command(label = props.runIoCommand)
        run.add_command(label = props.runPwrCommand)
        
        result = Menu(parent.master)
        self.add_cascade(label= props.resultMenuLabel, menu = result)
        result.add_command(label = props.resultIoCommand)
        result.add_command(label = props.resultPwrCommand)
        
    def load(self):
        filepath = filedialog.askopenfile()
        newBody= MainBody(self.parent.master)
        newBody.window = Panedwindow(self.parent.master, orient=HORIZONTAL)
        newBody.rframe = PinsPane(newBody.window, 'Test Properties')
        newBody.lframe = TestprogramPane(newBody.window, filepath)
        self.parent.mainBody.window.destroy()
        self.parent.mainBody.destroy()
        self.parent.mainBody = newBody
        self.parent.mainBody.show()
        
    def unload(self):
        newBody= MainBody(self.parent.master)
        newBody.window = Panedwindow(self.parent.master, orient=HORIZONTAL)
        newBody.rframe = PinsPane(newBody.window, 'Test Properties')
        newBody.lframe = TestprogramPane(newBody.window)
        self.parent.mainBody.window.destroy()
        self.parent.mainBody.destroy()
        self.parent.mainBody = newBody
        self.parent.mainBody.show()
        
        
#     def displayFlow(self, master, testFlow):
#         fileMenu = FileMenu(master, testFlow)
        
        