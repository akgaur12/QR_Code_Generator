from tkinter import *
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
import qrcode 

#Creating main window
root = Tk()
root.title("QR Code Generator")
root.geometry("450x520+550+50")
root.config(bg='#e4e8eb')
root.resizable(0,0)
logo = PhotoImage(file='logo.png')
root.iconphoto(False, logo)

Label(root, text='QR Code Generator', font=('Consolas', 24, ), bg='#e4e8eb', fg='blue').pack(pady=(15,18))
Label(root, text='Paste link or text to create QR Code', font=('Bahnschrift', 12), bg='#e4e8eb',).pack()




