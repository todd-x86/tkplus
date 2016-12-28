from exception import handle_exception, enable_handler

class Application(object):
    def __init__(self):
        pass
    
    def on_show(self):
        pass
    
    def run(self):
        enable_handler()
        try:
            self.on_show()
        except Exception as E:
            handle_exception(E)
