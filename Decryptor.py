import pyDes
import tkinter
import config
from tkinter import filedialog
from tkinter import simpledialog
from pathlib import Path
from pathlib import PurePath
from os import path

def not_empty(string):
    return string != None and string != ''

def error_info(title, msg):
    messagebox.showinfo(title, msg)
    return 'Program abort'

def print_no_newline(string):
    print(string, end='', flush=True)

dest_root = tkinter.Tk()
dest_root.withdraw()
destination = filedialog.askdirectory(parent=dest_root, title='Choose destination directory')
assert not_empty(destination), error_info('Error', 'Destination directory not selected')

files_root = tkinter.Tk()
files_root.withdraw()
files = filedialog.askopenfilenames(parent=files_root, title='Choose files to be decrypted')
assert not_empty(files), error_into('Error', 'Files to be decrypted not selected')
to_decrypt_list = files_root.tk.splitlist(files)

key = simpledialog.askstring('Password', 'Enter password: ', show='*')
assert not_empty(key), error_info('Error', 'Password not entered')
des = pyDes.des(key, padmode=pyDes.PAD_PKCS5)

prev_length = 0
unit = 1 / len(to_decrypt_list)
total = 0

progress = '=' * int(total * 100) + '>' + ' {:.2%}'.format(total)
print_no_newline(progress)

for to_decrypt in to_decrypt_list:
    output_path = path.join(destination, PurePath(to_decrypt).name[len(config.prefix) : ])
    with open(output_path, 'wb') as decrypted:
        with open(to_decrypt, 'rb') as content:
            decrypted.write(des.decrypt(content.read()))
        prev_length = len(progress)
        total += unit
    print_no_newline('\b' * prev_length)
    progress = '=' * int(total * 100) + '>' + ' {:.2%}'.format(total)
    print_no_newline(progress)
print('\nDecryption completed')

dest_root.destroy()
files_root.destroy()
