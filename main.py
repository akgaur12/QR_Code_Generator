from tkinter import *
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
import qrcode 

#function to generate QR Code
def QR_Code():
    global qr_img
    qr_img = qrcode.make(en.get())
    qr_img.save('qr.png')

    img = Image.open('qr.png').resize((230,230))
    img = ImageTk.PhotoImage(img)
    lbl = Label(qr, image=img)
    lbl.place(x=5, y=5, width=210, height=210)
    lbl.image_names = img


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

def on_leave(e):
    if en.get()=='':
        en.insert(0, 'Enter text or url')

link = StringVar()
en = Entry(root,font=('Bahnschrift', 11), relief=GROOVE, bg='#ffffff', justify='center', textvariable=link, bd=2)
en.place(x=50, y=110, width=350, height=32)
en.insert(0, 'Enter text or url')
en.bind("<FocusIn>", lambda e: en.delete(0, END))
en.bind("<FocusOut>", on_leave)

btn_create = Button(root, text='Generate QR Code', font=('Bahnschrift', 14), bg='purple', fg='white', bd=0, relief=GROOVE, activebackground='light green', command=QR_Code)
btn_create.place(x=90, y=165, width=265, height=35)

qr = Frame(root, bg='light gray')
qr.place(x=115, y=220, width=220, height=220)

Label(root, text='File Name',  font=('Bahnschrift', 12), bg='#e4e8eb', bd=0,).place(x=50, y=465, )

file_name = StringVar()
en_file_name = Entry(root,font=('Bahnschrift', 12), relief=GROOVE, bg='#ffffff', textvariable=file_name, bd=2)
en_file_name.place(x=130, y=465,)

btn_save = Button(root, text='Save', font=('Bahnschrift', 12), bg='green', fg='white', bd=0, relief=GROOVE, activebackground='light green', command=save)
btn_save.place(x=340, y=462,)

root.mainloop()




