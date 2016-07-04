import messagebox
from form import Form, TOOLWIN, SINGLE
from button import Button
from label import Label
from paintbox import PaintBox
from image import Image
from edit import Edit
from radio import RadioButton, RadioGroup
from checkbox import CheckBox
from memo import Memo
import logging


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

    img = Image(f, left=0, top=0, width=400, height=400, file='how_internet1.gif')
    
    b = Button(f, caption="Click Me", left=55, top=255, width=120, height=35)
    b.on_click = cool
    b.default = True

    lbl1 = Label(f, caption="Some text", left=15, top=45, width=100, height=30)

    pbox = PaintBox(f, left=175, top=5, width=100, height=100)
    pbox.pen.color = 'red'
    pbox.pen.width = 3
    pbox.line(0, 0, 100, 100)
    pbox.brush.color = 'blue'
    pbox.arc(15, 15, 65, 65, 0, 45)



    e1 = Edit(f, left=5, top=155, width=120, height=30)
    e1.text = "enter some crap here"

    rg = RadioGroup()
    r1 = RadioButton(f, caption="Red", left=135, top=5, width=100, height=20)
    r2 = RadioButton(f, caption="Blue", left=135, top=25, width=100, height=20)
    r3 = RadioButton(f, caption="Greengreen", left=135, top=45, width=100, height=20)
    r1.group = rg
    r1.value = 1
    r2.group = rg
    r2.value = 2
    r3.group = rg
    r3.value = 3

    r2.checked = True
    r3.checked = False

    c1 = CheckBox(f, caption='CLICK ME', left=200, top=45, width=100, height=20)
    c1.checked = True

    m1 = Memo(f, left=0, top=200, width=200, height=200, text='Foo\nbar')
    m1.text='fooey foo \n\tbar'

    f.left, f.top = 0, 0
    f.show()
