from form import Form
from button import Button
from label import Label
from image import Image
from memo import Memo
import os
import Tkinter as tk
import traceback

def handle_exception(ex, stacktrace=None):
    err_icon = os.path.join(os.path.dirname(__file__), 'graphics', 'icon_error.gif')
    frm = Form(caption='Exception: {}'.format(ex.__class__.__name__),
               left=100, top=100, width=350, height=180)
    frm.resizable = False
    msg = Label(frm, left=45, top=5, width=305, height=40, caption=ex.message)
    img = Image(frm, left=5, top=15, width=32, height=32, file=err_icon)
    trace = Memo(frm, left=5, top=55, width=335, height=90)
    trace.text = stacktrace

    def close_form():
        frm.close()
    
    btn = Button(frm, left=140, top=148, width=65, height=27, caption="Close")
    btn.on_click = close_form
    frm.show_modal()

def enable_handler():
    tk.CallWrapper = ExceptionHandler

class ExceptionHandler(object):
    def __init__(self, func, subst, widget):
        self._func = func
        self._subst = subst
        self._widget = widget

    def __call__(self, *args):
        try:
            if self._subst:
                return self._subst(*args)
            else:
                return self._func(*args)
        except SystemExit, msg:
            raise SystemExit, msg
        except Exception as ex:
            # TODO: Figure out how to ignore this section of code in stacktrace
            handle_exception(ex, traceback.format_exc())
