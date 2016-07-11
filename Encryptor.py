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
files = filedialog.askopenfilenames(parent=files_root, title='Choose files to be encrypted')
to_encrypt_list = files_root.tk.splitlist(files)

key = simpledialog.askstring('Password', 'Enter password: ', show='*')
des = pyDes.des(key, padmode=pyDes.PAD_PKCS5)

for to_encrypt in to_encrypt_list:
    output_path = path.join(destination, config.prefix + PurePath(to_encrypt).name)
    print(output_path)
    with open(output_path, 'wb') as encrypted:
        with open(to_encrypt, 'rb') as content:
            encrypted.write(des.encrypt(content.read()))
