from application import app
import messagebox
from form import Form, TOOLWIN, SINGLE
from button import Button
from label import Label
from paintbox import PaintBox
from image import Image
from edit import Edit

def cool2():
    print "GREETZ"

def cool():
    global f
    messagebox.show('hello world')
    f1 = Form("New Form", 320, 200)
    btn1 = Button(f1, 'Hello', 5, 5, 200, 100)
    btn1.on_click = cool2
    f1.show_modal()
    print "I'm a cool app"

if __name__ == '__main__':
    f = Form("Hello", 640, 480)
    f.caption = "Greetings"
    f.resizable = True
    f.form_type = SINGLE
    
    b = Button(f, "Click Me", 55, 55, 120, 35)
    b.on_click = cool

    lbl1 = Label(f, "Some text", 100, 5, 100, 30)

    pbox = PaintBox(f, 175, 5, 100, 100)
    pbox.pen.color = 'red'
    pbox.pen.width = 3
    pbox.line(0, 0, 100, 100)
    pbox.brush.color = 'blue'
    pbox.arc(15, 15, 65, 65, 0, 45)

    img = Image(f, 275, 5, 200, 200, 'how_internet1.gif')

    e1 = Edit(f, 5, 55, 120, 30)
    e1.text = "enter some crap here"
    
    app.run(f, 15, 15)
