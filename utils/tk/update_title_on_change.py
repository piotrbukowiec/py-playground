from utils.tk.update_title import update_title


def update_title_on_change(root):
    root.bind("<Configure>", lambda event: update_title(root, event, root.winfo_width(), root.winfo_height()))