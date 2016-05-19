import tkMessageBox
from application import app
YES_NO_CANCEL = 0
YES_NO = 1
OK_CANCEL = 2

YES = True
OK = True
NO = False
CANCEL = None

def show(text, title="Message"):
    app.non_use()
    tkMessageBox.showinfo(title, text)
    return True

def error(text, title="Error"):
    app.non_use()
    tkMessageBox.showerror(title, text)
    return True

def warning(text, title="Warning"):
    app.non_use()
    tkMessageBox.showwarning(title, text)
    return True

def confirm(text, title="Confirmation", confirm_type=YES_NO_CANCEL):
    app.non_use()
    if confirm_type == YES_NO_CANCEL:
        return tkMessageBox.askyesnocancel(title, text)
    elif confirm_type == YES_NO:
        return tkMessageBox.askyesno(title, text)
    elif confirm_type == OK_CANCEL:
        return tkMessageBox.askokcancel(title, text)
    else:
        raise Exception('confirm_type must be YES_NO_CANCEL, YES_NO, or OK_CANCEL')
