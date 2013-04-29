
from functools import partial
from contextlib import contextmanager
import gtk

@contextmanager
def destroying (thing):
    try:
        yield thing
    finally:
        thing.destroy ()

def show_message_dialog (msg, long_msg, msg_type = gtk.MESSAGE_INFO):
    error_dlg = gtk.MessageDialog (
        type = msg_type,
        buttons = gtk.BUTTONS_CLOSE,
        message_format = long_msg)
    error_dlg.set_title (msg)
    res = error_dlg.run ()
    error_dlg.destroy ()
    return res

show_error_dialog = partial (show_message_dialog, msg_type = gtk.MESSAGE_ERROR)


