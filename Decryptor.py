import pyDes
import tkinter
import config
from tkinter import filedialog
from tkinter import simpledialog
from pathlib import Path
from pathlib import PurePath
from os import path

dest_root = tkinter.Tk()
dest_root.withdraw()
destination = filedialog.askdirectory(parent=dest_root, title='Choose destination directory')

files_root = tkinter.Tk()
files_root.withdraw()
files = filedialog.askopenfilenames(parent=files_root, title='Choose files to be decrypted')
to_decrypt_list = files_root.tk.splitlist(files)

key = simpledialog.askstring('Password', 'Enter password: ', show='*')
des = pyDes.des(key, padmode=pyDes.PAD_PKCS5)

for to_decrypt in to_decrypt_list:
    output_path = path.join(destination, PurePath(to_decrypt).name[len(config.name) : ])
    with open(output_path, 'wb') as decrypted:
        with open(to_decrypt, 'rb') as content:
            decrypted.write(des.decrypt(content.read()))
