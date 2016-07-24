from exception import ExceptionHandler, handle_exception
import Tkinter as tk

class Application(object):
    def __init__(self):
        pass
    
    def on_show(self):
        pass
    
    def run(self):
        tk.CallWrapper = ExceptionHandler
        try:
            self.on_show()
        except Exception as E:
            handle_exception(E)
