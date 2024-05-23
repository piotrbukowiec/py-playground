import tkinter as tk
from tkinter import ttk

from translator import get_target_lang_codes, translate_text
from utils.tk.center_window import center_window
from utils.tk.fill_the_screen_with_window import fill_the_screen_with_window
from utils.tk.make_window_resizable import make_window_resizable
from utils.tk.update_title_on_change import update_title_on_change


def handle_translation():
    text = input_state.get()
    target_lang_code = target_lang_var.get()
    result = translate_text(text, target_lang_code)
    print(result)
    output_text_var.set(result)


root = tk.Tk()
fill_the_screen_with_window(root)
center_window(root)
make_window_resizable(root)
update_title_on_change(root)

# Zmienna StringVar do przechowywania stanu pola tekstowego
input_state = tk.StringVar(root)

# Zmienna StringVar do przechowywania kodu wybranego języka
target_lang_var = tk.StringVar(root)

# Ramka dla pola tekstowego do wprowadzania tekstu
input_frame = tk.Frame(root, highlightbackground="black", highlightthickness=5)
input_frame.pack(padx=10, pady=(10, 0), side="top")

# Pole tekstowe do wprowadzania tekstu
text_input = tk.Entry(input_frame, textvariable=input_state, width=50)
text_input.pack(side="left", padx=10, pady=(10, 0))

# Ramka dla listy rozwijanej i przycisku
options_frame = tk.Frame(root)
options_frame.pack(padx=10, pady=(10, 0), side="top")

# Lista rozwijana z kodami języków
target_languages = get_target_lang_codes()
target_language_dropdown = ttk.Combobox(options_frame, textvariable=target_lang_var, values=target_languages, width=40)
target_language_dropdown.pack(side="left", padx=10, pady=(10, 0))
target_language_dropdown.current(0)  # Ustawienie domyślnej wartości

# Przycisk Tłumacz
translate_button = tk.Button(options_frame, text="Tłumacz", command=handle_translation, width=10)
translate_button.pack(side="left", padx=(10, 0), pady=(10, 0))

# Zmienna StringVar do przechowywania tekstu wyjściowego
output_text_var = tk.StringVar(root)

# Ramka dla pola tekstowego z wynikiem
result_frame = tk.Frame(root, highlightbackground="black", highlightthickness=5)
result_frame.pack(padx=10, pady=(10, 10))

# Pole tekstowe z wynikiem (zablokowane do edycji)
output_text = tk.Entry(result_frame, textvariable=output_text_var, width=50, state="readonly")
output_text.pack(fill="both", expand=True)

root.mainloop()
