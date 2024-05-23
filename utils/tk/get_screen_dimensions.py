from app_types import ScreenDimensions


def get_screen_dimensions(root):
    screen_dimensions = ScreenDimensions(
        width=root.winfo_screenwidth(),
        height=root.winfo_screenheight()
    )
    return screen_dimensions
