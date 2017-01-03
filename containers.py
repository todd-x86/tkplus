from control import CustomControl, ALIGN_CLIENT, ALIGN_RIGHT
from scrollbar import BaseScrollBar
from Tkinter import LEFT, BOTH, RIGHT, Y

class ScrollContainer(CustomControl):
    def __init__(self, parent, **kwargs):
        CustomControl.__init__(self, parent, **kwargs)
        self._yscroll = BaseScrollBar(self, top=0, left=self.width, height=self.height, width=28)
        self._yscroll.align = ALIGN_RIGHT
        # TODO: Make an event handler
        self.on_show = self._reset_scrollbar

    def _init_container(self, control):
        control.align = ALIGN_CLIENT
        self._container = control
        self._bind()
        self._yscroll.refresh()
        #self._reset_scrollbar()

    def _reset_scrollbar(self):
        self._yscroll.set(*self._container._ctrl.yview())

    def _bind(self):
        # Pack container and eventually the scrollbar
        self._container._ctrl.pack(side=LEFT, fill=BOTH, expand=1)
        
        # Setup appropriate callbacks
        self._container._control_set('yscrollcommand', self._on_scroll_view)
        self._yscroll._control_set('command', self._on_scroll)
        self._yscroll.visible = False

        self._yscroll.refresh()
        self._container.refresh()

    def _show_scrollbar(self):
        self._yscroll.visible = True #_ctrl.pack(side=RIGHT, fill=Y)

    def _hide_scrollbar(self):
        self._yscroll.visible = False

    def _on_scroll_view(self, ymin, ymax):
        if self._yscroll.visible and float(ymax)-float(ymin) == 1.0:
            self._hide_scrollbar()
        elif not self._yscroll.visible and float(ymax)-float(ymin) != 1.0:
            self._show_scrollbar()
        return self._yscroll.set(ymin, ymax)
            
    def _on_scroll(self, *args):
        # Hacky way of chaining yview + on_scroll callback
        return self._container._ctrl.yview(*args)
