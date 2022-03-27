from tkinter import *
from tkinter import ttk
import threading
from pytube import YouTube
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image

root = Tk()
root.title('Pandabear Youtube Downloader')
root.iconbitmap('C:/Users/panda/Downloads/panda.ico')
root.geometry("350x500+515+106")
root.resizable(0, 0)

def progressbar(streams, chunk, bytes_remaining):
    ukuran = ya.filesize
    besar = ((ukuran - bytes_remaining) / ukuran) * 100
    persentase['value'] = besar

def dc(event):
    masukan = listdata.get(ANCHOR)
    masuk = str(masukan)
    keluar = masuk.split("\"")
    itagku.delete(0,END)
    itagku.insert(0, keluar[1])
    
def dy(event):
    threading.Thread(target=chckl).start()

def chckl():
    yt = YouTube(link.get())
    messagebox.showinfo("Pandabear", f"link anda {yt.title} sedang di check di server youtube mohon tunggu sebentar")
    c = str(yt.streams.all)
    d = c.split(",")
    listdata.delete(0, END)
    for x in d:
        listdata.insert(END, x)
    my_button.config(text="Download", command=lambda: threading.Thread(target=downloadyutub).start())

def simpanfile():
    global dir
    dir = filedialog.askdirectory()

def downloadyutub():
    global yt, ya
    yt = YouTube(link.get(), on_progress_callback=progressbar)
    messagebox.showinfo("Pandabear", f"{yt.title} sedang didownload mohon tunggu sebentar")
    itagnya = str(itagku.get())
    ya = yt.streams.get_by_itag(itagnya)
    ya.download(dir)
    messagebox.showinfo("Pandabear", f"file anda telah selesai di download")
    my_button.config(text="Check Link", command=lambda: threading.Thread(target=chckl).start())
    
bg = PhotoImage(file="C:/Users/panda/Pictures/pandasaja1.png")
canbg = Canvas(root, width=350, height=500, bd=0, highlightthickness=0)
canbg.pack(fill="both", expand=True)
canbg.create_image(0,0, image=bg, anchor="nw")

canbg.create_text(345, 20, text="Pandabear YouTube Downloader", font=("Cooper Black", 15), anchor=NE)

canbg.create_text(238, 60, text="Masukan Link Youtube (Ctrl+V)", font=("Cooper Black", 10), anchor=NE)

link = Entry(root, font=("Cooper Black", 14), bd=5, width=27, bg="#dff9d6")
link.pack(padx=5, pady=5)
link.bind('<Return>', dy)
link_window = canbg.create_window(175, 92, window=link)

canbg.create_text(175, 118, text='''Pilih Video Dengan Double Click ListData''', font=("Cooper Black", 11), anchor=N)

listdata = Listbox(root, width=55, bg="#dff9d6")
listdata.pack(pady=10)

listdata_window = canbg.create_window(175, 218, window=listdata)
listdata.bind('<Double-Button-1>', dc)

itagku = Entry(root, font=("Cooper Black", 14), bd=0, width=3, bg="#c0f2cf")
itagku.pack(pady=5)
itagku_window = canbg.create_window(175, 355, window=itagku)

persentase = ttk.Progressbar(root, orient=HORIZONTAL, length=200, mode='determinate')
persentase.pack(pady=5)
persentase_window = canbg.create_window(175, 320, window=persentase)

my_button = Button(root, text="Check Link", command=lambda: threading.Thread(target=chckl).start(), font=("Cooper Black", 15), bg="#dff9d6")
my_button.pack(pady=10, padx=10)
my_button_window = canbg.create_window(98, 440, window=my_button)

st = Button(root, text="Lokasi Save", command=lambda: threading.Thread(target=simpanfile).start(), font=("Cooper Black", 15), bg="#dff9d6")
st.pack(pady=10, padx=10)

st_window = canbg.create_window(256, 440, window=st)

canbg.create_text(347, 480, text="Coded By Pandabear", font=("Cooper Black", 10), width=350, anchor=NE)
canbg.create_text(3, 480, text="Version 1.3", font=("Cooper Black", 10), width=350, anchor=NW)

root.mainloop()
