from control import ALIGN_CLIENT
from form import Form
from dialogs import OpenDialog, SaveDialog
from memo import Memo
from statusbar import StatusBar
from menu import MainMenu
import os
import sys

class NotepadForm(Form):
    def __init__(self, filename=None):
        Form.__init__(self, width=1024, height=768)
        self._set_caption(filename)
        self._status = StatusBar(self)
        self._editor = Memo(self, left=0, top=0, width=1280, height=1024)
        self._editor.align = ALIGN_CLIENT
        self._create_menubar()

    def _file_new(self):
        pass

    def _file_open(self):
        dlg = OpenDialog(self)
        if dlg.execute():
            self._editor.lines.open_file(dlg.filename)
            self._set_caption(dlg.filename)
    
    def _file_save(self):
        pass

    def _file_save_as(self):
        pass

    def _file_exit(self):
        sys.exit(0)

    def _toggle_statusbar(self, checked):
        self._status.visible = checked

    def _create_menubar(self):
        menu = MainMenu(self)
        with menu.create('File') as file_menu:
            file_menu.create('New', on_click=self._file_new)
            file_menu.create('Open', on_click=self._file_open)
            file_menu.create('Save', on_click=self._file_save)
            file_menu.create('Save As...', on_click=self._file_save_as)
            file_menu.separator()
            file_menu.create('Page Setup')
            file_menu.create('Print...')
            file_menu.separator()
            file_menu.create('Exit', on_click=self._file_exit)

        with menu.create('Edit') as edit_menu:
            pass

        with menu.create('Format') as format_menu:
            pass

        with menu.create('View') as view_menu:
            view_menu.create('Status Bar', checkbox=True, checked=True, on_click=self._toggle_statusbar)

        with menu.create('Help') as help_menu:
            pass
        


    def _set_caption(self, filename):
        if not filename:
            filename = 'Untitled'
        else:
            filename = os.path.basename(filename)
        self.caption = 'Notepad - {}'.format(filename)

if __name__ == '__main__':
    form = NotepadForm()
    form.show()
