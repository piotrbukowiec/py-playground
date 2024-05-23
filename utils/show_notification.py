import ctypes
from os import name, system as show_posix_system_notification


def show_notification_windows(title, message):
    MessageBox = ctypes.windll.user32.MessageBoxW
    MessageBox(None, message, title, 0x40 | 0x0)  # 0x40 to wartość dla MB_ICONINFORMATION


def show_notification(title="Powiadomienie", message="Tekst został skopiowany do schowka."):
    if name == "posix":  # Linux or macOS
        show_posix_system_notification('osascript -e \'display notification "{}" with title "{}"\''.format(message, title))
    elif name == "nt":  # Windows
        show_notification_windows(title, message)
    else:
        raise Exception(f'Unknown system: {name}')