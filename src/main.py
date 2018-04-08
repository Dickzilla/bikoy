'''
Created on 6 Apr 2018

@author: BIKOYPOGI
'''

from tkinter import Tk
import view.ostApp as ostApp

if __name__ == '__main__':
    root=Tk()
    root.geometry("400x300")
    app=ostApp.OstApp(root)
#     app.pack()
    root.mainloop()
    

