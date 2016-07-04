from control import Control
from Tkinter import PhotoImage, Label

class Picture(object):
    def __init__(self, tk_hnd):
        self._img = None
        self._hnd = tk_hnd

    def open_file(self, filename):
        self._img = PhotoImage(file=filename)        
        self.refresh()

    def refresh(self):
        if not self._img:
            return
        self._hnd.configure(image=self._img)

    @property
    def width(self):
        if not self._img:
            return None
        else:
            return self._img.width()

    @property
    def height(self):
        if not self._img:
            return None
        else:
            return self._img.height()

class Image(Control):
    def __init__(self, parent, **kwargs):
        super(self.__class__, self).__init__()
        # Tk does not have a truly dedicated "Image" object
        # unless you install PIL
        self._ctrl = Label(master=parent._frame)
        self.left = kwargs['left']
        self.top = kwargs['top']
        self.width = kwargs['width']
        self.height = kwargs['height']
        self._picture = Picture(self._ctrl)
        if kwargs.get('file'):
            self._picture.open_file(kwargs['file'])

    @property
    def picture(self):
        return self._picture
