import messagebox
from form import Form, TOOLWIN, SINGLE
from button import Button, BitBtn, SpinButton
from label import Label
from paintbox import PaintBox
from image import Image
from edit import Edit
from radio import RadioButton, RadioGroup
from checkbox import CheckBox
from memo import Memo
from scrollbar import ScrollBar, HORIZONTAL
from panel import Panel
from menu import MainMenu, PopupMenu
from progressbar import ProgressBar
from slider import Slider
from listbox import ListBox
from combobox import ComboBox
from statusbar import StatusBar
from listview import ListView
from treeview import TreeView
from dialogs import OpenDialog, DirectoryDialog
from app import Application
import logging
import sys


class TestApp(Application):
    def on_show(self):
        FORMAT = '%(asctime)s - %(levelname)s: %(message)s'
        logging.basicConfig(format=FORMAT, level=logging.DEBUG)

        log = logging.getLogger('tkplus-demo')

        def cool2():
            print "GREETZ"

        def cool():
            global f
            messagebox.show('hello world')
            f1 = Form(caption="New Form", left=320, top=200)
            btn1 = Button(f1, caption='Hello', left=5, top=5, width=200, height=100)
            btn1.on_click = cool2
            btn1.background = 'blue'
            f1.show_modal()
            print "I'm a cool app"

        log.debug('demo app starting')
        f = Form(caption="Hello", width=640, height=480)
        f.caption = "Greetings"
        f.resizable = True
        f.form_type = SINGLE

        #img = Image(f, left=0, top=0, width=400, height=400, file='ok.gif')
        #img2 = Image(f, left=20, top=20, width=30, height=30, file='ok.gif')
    
        b = Button(f, caption="&Click Me", left=0, top=0, width=120, height=35)
        b.on_click = cool
        b.default = True

        b2 = Button(f, caption="Click &Me 2", left=0, top=40, width=120, height=35)
        
        def on_new():
            print "HELLO"
            messagebox.show("NEW FILE")

        menu = MainMenu(f)
        filemenu = menu.create("File")
        filemenu.create("New", on_click=on_new)
        filemenu.separator()
        filemenu.create("Exit", on_click=f.close)

        def close_notify():
            print "CLOSING"

        popup1 = PopupMenu(f)
        popup1.create("Click me", on_click=on_new)

        popup2 = PopupMenu(f)

        dlg = OpenDialog(f)
        dlg.multiple = True
        dlg.title = 'Pick a file'
        dlg.filter = 'Text Documents|*.txt'
        def raise_ex(self):
            raise ValueError('If I had a nickel for every exception that was thrown...')
        b2.on_click = raise_ex

        f.icon = 'notepad.ico'

        tv1 = TreeView(f, top=80, left=5, width=600, height=300)
        item = tv1.items.add('C:')
        item.add('Documents and Settings')
        item.add('Users').add('Todd Suess').add('Desktop')
        item.add('Windows').add('system32')

        sb = StatusBar(f)

        f.left, f.top = 0, 0
        f.show()

if __name__ == '__main__':
    app = TestApp()
    app.run()
