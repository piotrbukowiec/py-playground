from utils.tk.get_screen_dimensions import get_screen_dimensions

def update_title(root, event=None, width=None, height=None) -> str:
    if width is None or height is None:
        width, height = get_screen_dimensions(root)
    dimensions_str = f"Aplikacja tłumacza z wykorzystaniem DeepL Python. Wymiary: {width}x{height}"
    return root.title(dimensions_str)
