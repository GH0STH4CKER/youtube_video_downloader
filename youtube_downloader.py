#Script By GH0STH4CK3R
from pytube import YouTube
import time 
from colorama import Fore , init 
init()
Lgrn = Fore.LIGHTGREEN_EX
Lylw = Fore.YELLOW
Lred = Fore.RED

banner="""
█▄█ █▀█ █ █ ▀█▀ █ █ █▄▄ █▀▀   █▀▄ █▀█ █ █ █ █▄ █ █   █▀█ ▄▀█ █▀▄ █▀▀ █▀█
 █  █▄█ █▄█  █  █▄█ █▄█ ██▄   █▄▀ █▄█ ▀▄▀▄▀ █ ▀█ █▄▄ █▄█ █▀█ █▄▀ ██▄ █▀▄"""

print(Lred + "\n█▄█ █▀█ █ █ ▀█▀ █ █ █▄▄ █▀▀   ",end="")
print(Lylw + "█▀▄ █▀█ █ █ █ █▄ █ █   █▀█ ▄▀█ █▀▄ █▀▀ █▀█")
print(Lred + " █  █▄█ █▄█  █  █▄█ █▄█ ██▄   ",end="")
print(Lylw + "█▄▀ █▄█ ▀▄▀▄▀ █ ▀█ █▄▄ █▄█ █▀█ █▄▀ ██▄ █▀▄")
print(Fore.LIGHTYELLOW_EX + "-------------------- [+] Script by GH0STH4CK3R --------------------------")

print(Lgrn+"")
link = input("Enter Youtube Link : ")
yt = YouTube(link)

print(Fore.LIGHTYELLOW_EX + "\nTitle  : ",yt.title)
print("Views  : ",yt.views)
print("Length : ",yt.length)
print("Rating : ",yt.rating)

print(Lgrn + "\nDownload Options : \n\n[1] Audio Only\n[2] Video Highest Resolution\n[3] Video Lowest Resolution\n[4] Video Custom Resolution")
dt = int(input("\nDownload Type : "))

if dt == 1 :
    ys = yt.streams.get_audio_only()
elif dt == 2 :
    ys = yt.streams.get_highest_resolution()
elif dt == 3 :
    ys = yt.streams.get_lowest_resolution()
elif dt == 4 :
    dts = input("\nResolution (720p,480p,360p,240p,144p) : ")
    try:
        ys = yt.streams.get_by_resolution(dts)
    except Exception as er :
        print("Resolution Not Available !")
        time.sleep(8)
        exit()
else :
    print(Lred + "\nInvalid Option !")
    time.sleep(8)
    exit()
print(Lgrn + "")
dl = input("Location (leave empty = current directory) : ")

print("\nDownloading...")
try:
    if dl == "" :
        dsz = ys.filesize
        sid = "Bytes"
        if dsz >= 1024 :
            dsz = dsz / 1024
            sid = "KB" 
            if dsz >= 1024 :
                dsz = dsz / 1024
                sid = "MB" 
                if dsz >= 1024 :
                    dsz = dsz / 1024
                    sid = "GB" 
        print("\nSize : ",dsz,sid)
        ys.download()
    else :
        dsz = ys.filesize
        sid = "Bytes"
        if dsz >= 1024 :
            dsz = dsz / 1024
            sid = "KB" 
            if dsz >= 1024 :
                dsz = dsz / 1024
                sid = "MB" 
                if dsz >= 1024 :
                    dsz = dsz / 1024
                    sid = "GB" 
        print("\nSize : ",dsz,sid)
        ys.download(dl)  
except Exception as e:
    print(Lred + "Failed ,\nError ",e)
else :
    print(Lgrn + "\nSuccess !")    


input("\n\nExit >")
