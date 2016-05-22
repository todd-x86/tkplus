import tkMessageBox
from form import check_handle
YES_NO_CANCEL = 0
YES_NO = 1
OK_CANCEL = 2

YES = True
OK = True
NO = False
CANCEL = None

@check_handle
def show(text, title="Message"):
    tkMessageBox.showinfo(title, text)
    return True

@check_handle
def error(text, title="Error"):
    tkMessageBox.showerror(title, text)
    return True

@check_handle
def warning(text, title="Warning"):
    tkMessageBox.showwarning(title, text)
    return True

@check_handle
def confirm(text, title="Confirmation", confirm_type=YES_NO_CANCEL):
    if confirm_type == YES_NO_CANCEL:
        return tkMessageBox.askyesnocancel(title, text)
    elif confirm_type == YES_NO:
        return tkMessageBox.askyesno(title, text)
    elif confirm_type == OK_CANCEL:
        return tkMessageBox.askokcancel(title, text)
    else:
        raise Exception('confirm_type must be YES_NO_CANCEL, YES_NO, or OK_CANCEL')
