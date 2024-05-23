from utils.tk.get_screen_dimensions import get_screen_dimensions


def fill_the_screen_with_window(root):
    width, height = get_screen_dimensions(root)
    return root.geometry(f"{width}x{height}")
