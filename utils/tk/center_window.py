def center_window(root):
    root.update_idletasks()
    screen_width, screen_height = root.winfo_screenwidth(), root.winfo_screenheight()
    x = (screen_width - root.winfo_width()) // 2
    y = (screen_height - root.winfo_height()) // 2
    root.geometry(f"+{x}+{y}")
    dimensions_str = f"{root.winfo_width()}x{root.winfo_height()}"
    root.title(dimensions_str)