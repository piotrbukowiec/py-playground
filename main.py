import tkinter as tk
from tkinter import ttk
from utils.translator import get_target_lang_codes
from utils.copy_to_clipboard import copy_to_clipboard
from utils.handle_translation import handle_translation
from utils.tk.center_window import center_window
from utils.tk.fill_the_screen_with_window import fill_the_screen_with_window
from utils.tk.make_window_resizable import make_window_resizable
from utils.tk.update_title_on_change import update_title_on_change

root = tk.Tk()
fill_the_screen_with_window(root)
center_window(root)
make_window_resizable(root)
update_title_on_change(root)

frame_style = {"borderwidth": 2, "relief": "groove", "background": "#f0f0f0", "padx": 10, "pady": 10}

input_state = tk.StringVar(root)
target_lang_var = tk.StringVar(root)

input_frame = tk.Frame(root, **frame_style)
input_frame.pack(fill="x", padx=10, pady=10)

text_input = tk.Entry(input_frame, textvariable=input_state, width=50, bd=0, bg="black", fg="white", font=("Arial", 12))
text_input.pack(fill="both", expand=True, padx=10, pady=(10, 0))

options_frame = tk.Frame(root, **frame_style)
options_frame.pack(fill="x", padx=10, pady=(10, 0))

target_languages = get_target_lang_codes()
target_language_dropdown = ttk.Combobox(options_frame, textvariable=target_lang_var, values=target_languages, font=("Arial", 12))
target_language_dropdown.pack(side="left", padx=(10, 0), pady=(10, 0))
target_language_dropdown.current(0)

translate_button = tk.Button(options_frame, text="Tłumacz", command=lambda: handle_translation(input_state, target_lang_var, output_text_var), width=10, font=("Arial", 12))
translate_button.pack(side="left", padx=(10, 0), pady=(10, 0))

result_frame = tk.Frame(root, **frame_style)
result_frame.pack(fill="both", expand=True, padx=10, pady=(10, 0))

output_text_var = tk.StringVar(root)

output_text = tk.Entry(result_frame, textvariable=output_text_var, width=50, state="readonly", bd=0, bg="black", fg="white", font=("Arial", 12), justify="center")
output_text.pack(fill="both", expand=True)

output_text.bind("<Button-1>", lambda event: copy_to_clipboard(output_text_var=output_text_var))

root.mainloop()
