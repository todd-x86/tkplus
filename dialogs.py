from tkFileDialog import askopenfilename, asksaveasfilename, askdirectory

class BaseFileDialog(object):
    def __init__(self, parent, func, **kwargs):
        self._parent = parent
        self._opts = {'parent':parent._frame}
        self._filter = ''
        self._filename = None
        self._filenames = ()
        self._func = func

    @property
    def filenames(self):
        return self._filenames

    @property
    def filename(self):
        return self._filename

    @property
    def multiple(self):
        return bool(self._opts.get('multiple', 0))

    @multiple.setter
    def multiple(self, value):
        self._opts['multiple'] = 1 if value else 0

    @property
    def title(self):
        return self._opts.get('title')

    @title.setter
    def title(self, value):
        self._opts['title'] = value

    @property
    def initial_dir(self):
        return self._opts.get('initialdir')

    @initial_dir.setter
    def initial_dir(self, value):
        self._opts['initialdir'] = value

    @property
    def filter(self):
        return self._filter

    @filter.setter
    def filter(self, value):
        self._filter = value
        items = value.split('|')
        
        # NOTE: I think this is what Delphi/.NET does but I could be wrong...
        if len(items) % 2 != 0:
            items.append('*.*')

        # I'm sure there's a more Pythonic way of doing this
        file_types = []
        while len(items):
            file_types.append((items.pop(0), items.pop(0)))
            
        self._opts['filetypes'] = file_types

    @property
    def default_ext(self):
        return self._opts.get('defaultextension')

    @default_ext.setter
    def default_ext(self, value):
        self._opts['defaultextension'] = value

    def execute(self):
        tmpfile = self._func(**self._opts)
        if tmpfile:
            if self.multiple:
                self._filenames = tmpfile
                self._filename = None
            else:
                self._filenames = ()
                self._filename = tmpfile
            return True
        else:
            return False

class OpenDialog(BaseFileDialog):
    def __init__(self, parent, **kwargs):
        BaseFileDialog.__init__(self, parent, askopenfilename, **kwargs)

class SaveDialog(BaseFileDialog):
    def __init__(self, parent, **kwargs):
        BaseFileDialog.__init__(self, parent, asksavefilename, **kwargs)

class DirectoryDialog(object):
    def __init__(self, parent, **kwargs):
        self._opts = {'parent': parent._frame}
        self._directory = None

    @property
    def directory(self):
        return self._directory

    @property
    def title(self):
        return self._opts.get('title')

    @title.setter
    def title(self, value):
        self._opts['title'] = value

    @property
    def initial_dir(self):
        return self._opts.get('initialdir')

    @initial_dir.setter
    def initial_dir(self, value):
        self._opts['initialdir'] = value

    def execute(self):
        tmpfile = askdirectory(**self._opts)
        if tmpfile:
            self.directory = tmpfile
            return True
        else:
            return False
