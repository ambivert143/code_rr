from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry("500x500")
root.title("youtube video downloader app")

def download():
    try:
        myVar.set("downloading...")
        root.update()
        YouTube(link.get()).streams.first().download()
        link.set("video download successfully")
    except Exception as e:
        myVar.set("mistake")
        root.update()
        link.set("enter correct link")



Label(root, text= "welcome to youtube \n download app", font="consolas 15 bold").pack()
myVar = StringVar()
myVar.set("enter the link below")
Entry(root, textvariable= myVar, width=50).pack(pady=10)
link = StringVar()
Entry(root, textvariable= myVar, width=50).pack(pady=10)
Button(root, text="download video", command=download).pack()
root.mainloop()