import messagebox
from form import Form, TOOLWIN, SINGLE
from button import Button, BitBtn
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
import logging
import sys


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

if __name__ == '__main__':
    log.debug('demo app starting')
    f = Form(caption="Hello", width=640, height=480)
    f.caption = "Greetings"
    f.resizable = True
    f.form_type = SINGLE

    #img = Image(f, left=0, top=0, width=400, height=400, file='ok.gif')
    #img2 = Image(f, left=20, top=20, width=30, height=30, file='ok.gif')
    
    #b = BitBtn(f, caption="Click Me", left=0, top=0, width=120, height=35, image='ok.gif')
    #b.on_click = cool
    #b.default = True

    #lbl1 = Label(f, caption="Some text", left=15, top=45, width=100, height=30)

    #pbox = PaintBox(f, left=175, top=5, width=100, height=100)
    #pbox.pen.color = 'red'
    #pbox.pen.width = 3
    #pbox.line(0, 0, 100, 100)
    #pbox.brush.color = 'blue'
    #pbox.arc(15, 15, 65, 65, 0, 45)



    #e1 = Edit(f, left=5, top=155, width=120, height=30)
    #e1.text = "enter some crap here"

    #rg = RadioGroup()
    #r1 = RadioButton(f, caption="Red", left=135, top=5, width=100, height=20)
    #r2 = RadioButton(f, caption="Blue", left=135, top=25, width=100, height=20)
    #r3 = RadioButton(f, caption="Greengreen", left=135, top=45, width=100, height=20)
    #r1.group = rg
    #r1.value = 1
    #r2.group = rg
    #r2.value = 2
    #r3.group = rg
    #r3.value = 3

    #r2.checked = True
    #r3.checked = False

    #c1 = CheckBox(f, caption='CLICK ME', left=200, top=45, width=100, height=20)
    #c1.checked = True

    #m1 = Memo(f, left=0, top=200, width=200, height=200, text='Foo\nbar')
    #m1.text='fooey foo \n\tbar'

    #s = ScrollBar(f, left=15, top=5, width=200, height=20)
    #s.max = 10
    #s.window = 5
    #s.orientation = HORIZONTAL
    #def on_scroll(value, delta):
    #    print value, delta
    #s.on_scroll = on_scroll

    #p = Panel(f, left=5, top=5, width=200, height=200)
    #b = Button(p, left=0, top=0, width=60,height=22, caption='Hello')

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

    p1 = ProgressBar(f, left=125, top=5, width=130, height=24)

    def progress_done():
        p1.step(50)

    popup1.create("finish", on_click=progress_done)

    sl1 = Slider(f, left=25, top=100, width=150, height=90)

    f.on_close = close_notify
    f.popup_menu = popup1

    f.left, f.top = 0, 0
    f.show()
