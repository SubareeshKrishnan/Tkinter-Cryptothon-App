from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
from cryptography.fernet import Fernet
from cryptography.fernet import base64
import hashlib
import getpass


root = Tk()
root.title('Cryptothon')
root.resizable(False, False)
root.iconbitmap('icon.ico')

encrypt_frame = LabelFrame(root, text='Encrypter', padx=10, pady=10)
encrypt_frame.grid(row=0, column=0, padx=20, pady=20)

Label(encrypt_frame, text="Message", pady=5).grid(row=0, column=0, columnspan=4)
message = scrolledtext.ScrolledText(encrypt_frame, borderwidth=2, wrap=WORD, height=10, width=100, font = ("Calibri", 13))
message.grid(row=1, column=0, columnspan=4)
message.focus_set()

Label(encrypt_frame, text="Password", pady=5).grid(row=2, column=0, columnspan=4)
global password
password = Entry(encrypt_frame, show="*", width=60, borderwidth=2, font = ("Calibri", 13))
password.grid(row=3, column=0, columnspan=4)

def encrypt():
    try:
        global password
        global message
        p = password.get()
        m = message.get('1.0', END)
        if len(p) > 4:
            input_keyword = str.encode(str(p))
            input_key = hashlib.sha3_256(input_keyword)
            key_bytes = input_key.digest()
            key = base64.urlsafe_b64encode(key_bytes)

            text = str.encode(str(m))
            file1 = open('Encryptkey.txt','wb')
            file1.write(key)
            file1.close()

            cipher = Fernet(key)
            encrypted_text = cipher.encrypt(text)

            file = open('EncryptedText.txt','wb')
            file.write(encrypted_text)
            file.close()
            global l
            messagebox.showinfo("Encrypt","\tEncrypted Successfully!\nEncryped Message and Key file is generated!")
        else:
            messagebox.showerror("Invalid", "Password must have atleast 5 characters!")
            password.focus()

    except Exception as e:
        messagebox.showerror("Encrypt", "Encryption Unsuccessful")

encrypt_btn = Button(encrypt_frame, text="Encrypt",bg='black',fg='white', width = 10, command=encrypt)
encrypt_btn.grid(row=3, column=3, columnspan=4)

################################################################################

decrypt_frame = LabelFrame(root, text='Decrypter', padx=10, pady=10)
decrypt_frame.grid(row=1, column=0, padx=20, pady=5)

Label(decrypt_frame, text="Encrypted message file name: ", pady=5).grid(row=0, column=0, columnspan=4)
message_file = Entry(decrypt_frame, width=20, borderwidth=2, font = ("Calibri", 13))
message_file.grid(row=0, column=2, columnspan=4, pady=5)

Label(decrypt_frame, text="Key file name: ", pady=5).grid(row=1, column=0, columnspan=4)
key_file = Entry(decrypt_frame, show="*", width=20, borderwidth=2, font = ("Calibri", 13))
key_file.grid(row=1, column=2, columnspan=4, pady=5)
global mess
global k

def decrypt():
    global message_file
    global key_file
    global en_message
    if len(str(message_file.get())) <= 1 or len(str(key_file.get())) <= 1:
        messagebox.showerror("Decrypt", "Invalid Entry!")
    else:
        try:
            ke = key_file.get()
            m = message_file.get()

            k_file = str(ke)+'.txt'
            encrypted_file_name = str(m)+'.txt'

            file = open(encrypted_file_name,'rb')
            mess = file.read()
            file.close()


            file1 = open(k_file,'rb')
            k = file1.read()
            file1.close()

            cipher = Fernet(k)
            s = cipher.decrypt(mess)
            string = s.decode()
            #for i in string:
            en_message.insert(END, string)
        except FileNotFoundError as e:
            messagebox.showerror("Decrypt", "File not found!")


decrypt_btn = Button(decrypt_frame, text="Decrypt",bg='black',fg='white', width = 10, command=decrypt)
decrypt_btn.grid(row=2, column=2, columnspan=4, pady=5)

Label(decrypt_frame, text="Encrypted Message", pady=5).grid(row=3, column=2, columnspan=4)
en_message = scrolledtext.ScrolledText(decrypt_frame, borderwidth=2, wrap=WORD, height=10, width=100, font = ("Calibri", 13))
en_message.grid(row=4, column=2, columnspan=4, pady=5)

Label(root, text="Project by Subareesh", fg='red').grid(row=2, column=0, columnspan=4, pady=5)

root.mainloop()
