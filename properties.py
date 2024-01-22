import json
import tkinter
import os
from PIL import Image, ImageTk

class Functions:
    class General:
        def RenameFile(self, path, name):
            name = path.split('/'); name.reverse()
            name.remove(0); name.insert(0, name); name.reverse()
            name = '/'.join(name)
            os.rename(path, name)
    
    class Security:
        def Permitions(self, permitions=list[str], file=str, user=str):
            permit = {file: {user: permitions}}
            json.dump(permit, open('permitions.json', 'w'))

def Window(filelikeobject, path):
    page = 1
    deactive = 'light grey'; active = 'LavenderBlush2'
    
    window = tkinter.Tk()
    window.title(f'{filelikeobject} Properties')
    window.wm_resizable(False, False)
    canvas = tkinter.Canvas(window, width=300, height=500, bg='light grey')
    
    canvas.create_rectangle(30, 50, 270, 470, fill='LavenderBlush2', outline='grey')
    canvas.create_rectangle(30, 30, 80, 50, fill=deactive, outline='grey', activefill=active)
    canvas.create_text(55, 40, text='General')
    canvas.create_rectangle(80, 30, 130, 50, fill=deactive, outline='grey', activefill=active)
    canvas.create_text(105, 40, text='Security')
    canvas.create_rectangle(130, 30, 180, 50, fill=deactive, outline='grey', activefill=active)
    canvas.create_text(155, 40, text='Detail')
    canvas.create_rectangle(180, 30, 270, 50, fill=deactive, outline='grey', activefill=active)
    canvas.create_text(225, 40, text='Customisation')
    
    canvas.pack()
    window.mainloop()

Window('example.xml', 'example.xml')