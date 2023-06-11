import tkinter as tk
from tkinter import *
from tkinter import messagebox
from pytube import YouTube

DOWNLOADER = tk.Tk()
DOWNLOADER.title("DOWNLOADER")
DOWNLOADER.minsize(400,300)
DOWNLOADER.maxsize(400,300)

İNFO = "PLEASE ENTER A LİNK:"

def VİDEO_DOWNLOAD():
    data = DOWNLOAD_AREA.get()
    try:
        video = YouTube(data)
        stream = video.streams.get_highest_resolution()
        Title = video.title
        msg = Tk()
        msg.withdraw()
        messagebox.showwarning("WARNİNG!","VİDEO İS DOWNLOADİNG...")
        stream.download()
        messagebox.showinfo("İMFORMATİON","THE VİDEO SUCCESSFULLY DOWNLOADED\n"+"("+str(Title)+")")
        return 0
    
    except Exception as e:
        msg = Tk()
        msg.withdraw()
        messagebox.showerror("ERROR!","SOMETHİNG İS WRONG!\nPLEASE TRY AGAİN!")
        return 0
    
def MUSİC_DOWNLOAD():
    data = DOWNLOAD_AREA.get()
    try:
        audio = YouTube(data)
        audio_stream = audio.streams.filter(only_audio=True).first()
        Title = audio.title
        msg = Tk()
        msg.withdraw()
        messagebox.showwarning("WARNİNG!","AUDİO İS DOWNLOADİNG...")
        audio_stream.download(output_path='.', filename_prefix='audio')
        messagebox.showinfo("İMFORMATİON","THE AUDİO SUCCESSFULLY DOWNLOADED\n"+"("+str(Title)+")")
        return 0
    
    except Exception as e:
        msg = Tk()
        msg.withdraw()
        messagebox.showerror("ERROR!","SOMETHİNG İS WRONG!\nPLEASE TRY AGAİN!")
        return 0

DOWNLOAD_İNFO = tk.Label(DOWNLOADER,text = İNFO,fg = "blue",bg = "white",font = "Arial 20")
DOWNLOAD_İNFO.place(width = 400,height = 100,x = 0,y = 0)

DOWNLOAD_AREA = tk.Entry(DOWNLOADER,fg = "black",bg = "lime",font = "Arial 25")
DOWNLOAD_AREA.place(width = 400,height = 100,x = 0,y = 100)

DOWNLOAD_VİDEO_BUTTON = tk.Button(DOWNLOADER,text = "DOWNLOAD\n(VİDEO)",fg = "lime",bg = "black",font = "Arial 20",command = VİDEO_DOWNLOAD)
DOWNLOAD_VİDEO_BUTTON.place(width = 200,height = 100,x = 0,y = 200)

DOWNLOAD_MUSİC_BUTTON = tk.Button(DOWNLOADER,text = "DOWNLOAD\n(MUSİC)",fg = "lime",bg = "black",font = "Arial 20",command = MUSİC_DOWNLOAD)
DOWNLOAD_MUSİC_BUTTON.place(width = 200,height = 100,x = 200,y = 200)

DOWNLOADER.mainloop()
