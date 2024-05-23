import tkinter as tk
from tkinter import ttk
import pyperclip
from translator import get_target_lang_codes
from utils.handle_translation import handle_translation
from utils.show_notification import show_notification
from utils.tk.center_window import center_window
from utils.tk.fill_the_screen_with_window import fill_the_screen_with_window
from utils.tk.make_window_resizable import make_window_resizable
from utils.tk.update_title_on_change import update_title_on_change

root = tk.Tk()
fill_the_screen_with_window(root)
center_window(root)
make_window_resizable(root)
update_title_on_change(root)

input_state = tk.StringVar(root)
target_lang_var = tk.StringVar(root)

input_frame = tk.Frame(root, highlightbackground="black", highlightthickness=5)
input_frame.pack(padx=10, pady=(10, 0), side="top")

text_input = tk.Entry(input_frame, textvariable=input_state, width=50)
text_input.pack(side="left", padx=10, pady=(10, 0))

options_frame = tk.Frame(root)
options_frame.pack(padx=10, pady=(10, 0), side="top")

target_languages = get_target_lang_codes()
target_language_dropdown = ttk.Combobox(options_frame, textvariable=target_lang_var, values=target_languages, width=40)
target_language_dropdown.pack(side="left", padx=10, pady=(10, 0))
target_language_dropdown.current(0)

translate_button = tk.Button(options_frame, text="Tłumacz", command=lambda: handle_translation(input_state, target_lang_var, output_text_var), width=10)
translate_button.pack(side="left", padx=(10, 0), pady=(10, 0))

output_text_var = tk.StringVar(root)

result_frame = tk.Frame(root, highlightbackground="black", highlightthickness=5)
result_frame.pack(padx=10, pady=(10, 10))

output_text = tk.Entry(result_frame, textvariable=output_text_var, width=50, state="readonly")
output_text.pack(fill="both", expand=True)

def copy_to_clipboard(event=None):
    text_to_copy = output_text_var.get()
    pyperclip.copy(text_to_copy)
    show_notification()


output_text.bind("<Button-1>", func=copy_to_clipboard)

root.mainloop()
