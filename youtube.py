from pytube import YouTube
import os, socket
from colorama import Fore
lg = Fore.CYAN
cls = lambda: os.system('cls')
cls()
banner = """
██╗  ██╗███████╗███╗   ██╗██████╗ ███████╗██████╗ ███████╗
██║ ██╔╝██╔════╝████╗  ██║██╔══██╗██╔════╝██╔══██╗██╔════╝
█████╔╝ █████╗  ██╔██╗ ██║██║  ██║█████╗  ██████╔╝█████╗  
██╔═██╗ ██╔══╝  ██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗██╔══╝  
██║  ██╗███████╗██║ ╚████║██████╔╝███████╗██║  ██║███████╗
╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝╚══════╝
"""
print(lg + banner)
print("Youtube MP3\n")
URL = input("Link: ")
yt = YouTube(URL)

try:
    print("\nLetöltés\n")
    vide = yt.streams.filter(only_audio=True).first()
    out_file = vide.download()

    base, ext = os.path.splitext(out_file)
    new_file = base + ".mp3"
    os.rename(out_file, new_file)
    print("\nSiker\n")
    os.startfile(new_file)

except:
    print("\nValami nem jó\n")
   
