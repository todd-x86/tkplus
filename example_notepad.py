from form import Form
from dialogs import OpenDialog, SaveDialog
from memo import Memo
from statusbar import StatusBar
from menu import MainMenu
import os
import sys

class NotepadForm(Form):
    def __init__(self, filename=None):
        Form.__init__(self, width=640, height=480)
        self._set_caption(filename)
        self._status = StatusBar(self)
        self._editor = Memo(self, left=0, top=0, width=self.width, height=self.height-self._status.height)
        self._create_menubar()

    def _file_new(self):
        pass

    def _file_open(self):
        dlg = OpenDialog(self)
        if dlg.execute():
            self._editor.lines.open_file(dlg.filename)
            self._set_caption(dlg.filename)

    def _file_exit(self):
        sys.exit(0)

    def _create_menubar(self):
        menu = MainMenu(self)
        with menu.create('File') as file_menu:
            file_menu.create('New', on_click=self._file_new)
            file_menu.create('Open', on_click=self._file_open)
            file_menu.create('Save')
            file_menu.create('Save As...')
            file_menu.separator()
            file_menu.create('Exit', on_click=self._file_exit)

    def _set_caption(self, filename):
        if not filename:
            filename = 'Untitled'
        else:
            filename = os.path.basename(filename)
        self.caption = 'Notepad - {}'.format(filename)

if __name__ == '__main__':
    form = NotepadForm()
    form.show()
