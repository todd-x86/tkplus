from control import Control
from panel import Panel, BORDER_LOWERED
from Tkinter import RIGHT, BOTTOM, Y, X
from ttk import Sizegrip as TkSizeGrip

class StatusBar(Panel):
    def __init__(self, parent, **kwargs):
        Panel.__init__(self, parent, top=parent.height-30, left=0, width=parent.width, height=30)
        self.border_style = BORDER_LOWERED
        self._grip = TkSizeGrip(self._ctrl)
        self._grip.pack(side=RIGHT, fill=Y)
        self._ctrl.pack(side=BOTTOM, fill=X)
