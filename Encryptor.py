import pyDes
import tkinter
import config
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import messagebox
from pathlib import Path
from pathlib import PurePath
from os import path

def not_empty(string):
    return string != None and string != ''

def show_info(title, msg, return_info='Program abort'):
    messagebox.showinfo(title, msg)
    return return_info

def print_no_newline(string):
    print(string, end='', flush=True)

dest_root = tkinter.Tk()
dest_root.withdraw()
destination = filedialog.askdirectory(parent=dest_root, title='Choose destination directory')
assert not_empty(destination), show_info('Error', 'Destination directory not selected')

files_root = tkinter.Tk()
files_root.withdraw()
files = filedialog.askopenfilenames(parent=files_root, title='Choose files to be encrypted')
assert not_empty(files), error_into('Error', 'Files to be encrypted not selected')
to_encrypt_list = files_root.tk.splitlist(files)

key = simpledialog.askstring('Password', 'Enter password (8 characters): ', show='*')
assert not_empty(key), show_info('Error', 'Password not entered')
assert len(key) == 8, show_info('Error', 'Password is not 8 characters')
des = pyDes.des(key, padmode=pyDes.PAD_PKCS5)

prev_length = 0
unit = 1 / len(to_encrypt_list)
total = 0

progress = '=' * int(total * 100) + '>' + ' {:.2%}'.format(total)
print_no_newline(progress)

for to_encrypt in to_encrypt_list:
    output_path = path.join(destination, config.prefix + PurePath(to_encrypt).name)
    with open(output_path, 'wb') as encrypted:
        with open(to_encrypt, 'rb') as content:
            encrypted.write(des.encrypt(content.read()))
        prev_length = len(progress)
        total += unit
    print_no_newline('\b' * prev_length)
    progress = '=' * int(total * 100) + '>' + ' {:.2%}'.format(total)
    print_no_newline(progress)
print('\n' + show_info('Finished successfully', 'Encryption complete!', 'Finished successfully'))

dest_root.destroy()
files_root.destroy()
