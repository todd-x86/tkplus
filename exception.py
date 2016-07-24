from form import Form
from button import Button
from label import Label
from memo import Memo

def handle_exception(ex):
    frm = Form(caption='Exception: {}'.format(ex.__class__.__name__),
               left=100, top=100, width=350, height=180)
    msg = Label(frm, left=5, top=5, width=345, height=70, caption=ex.message)

    def close_form():
        frm.close()
    
    btn = Button(frm, left=100, top=155, width=65, height=27, caption="Close")
    btn.on_click = close_form
    frm.show_modal()

class ExceptionHandler(object):
    def __init__(self, func, subst, widget):
        self._func = func
        self._subst = subst
        self._widget = widget

    def __call__(self, *args):
        try:
            if self._subst:
                return apply(self._func, args)
            else:
                return apply(self._func, args)
        except SystemExit, msg:
            raise SystemExit, msg
        except Exception as ex:
            handle_exception(ex)
