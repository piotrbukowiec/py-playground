from pyperclip import copy

from utils.show_notification import show_notification


def copy_to_clipboard(event=None, output_text_var=None):
    text_to_copy = output_text_var.get()
    copy(text_to_copy)
    show_notification()