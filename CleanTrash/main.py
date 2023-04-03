from win10toast import ToastNotifier
import os, shutil

os.system('rm -rf C:/Users/kolon/AppData/Local/Temp/*')

notification = ToastNotifier()

notification.show_toast(
    "CleanTrash",
    "Limpeza concluida.",
    duration = 20,
    icon_path = "icone.ico",
    threaded = True,
)