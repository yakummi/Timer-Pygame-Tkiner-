import time
from tkinter import *
import pygame


def stop():
    btn_start.pack()
    btn_stop.pack_forget()
    pygame.mixer.music.pause()


def sound():
    btn_start.pack_forget()
    btn_stop.pack()
    pygame.mixer.music.play()


def start():
    duration = int(seconds.get())
    while duration:
        m, s = divmod(int(duration), 60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
        count_digit['text'] = min_sec_format
        count_digit.update()
        time.sleep(1)
        duration -= 1
    sound()


file = 'Boulevard_Depo_-_DRUG_(musmore.com).mp3'
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)

root = Tk()
root.title('Таймер')
root.geometry('150x150')
root.resizable(0, 0)

count_digit = Label(root, text='0', font='Arial 15 bold')
count_digit.pack()

seconds = Entry(root, font='Arial 15 bold', width=7)
seconds.pack(pady=10)

btn_start = Button(root, text='Старт', font='Arial 15 bold', command=start)
btn_start.pack()

btn_stop = Button(root, text='Выключить', font='Arial 15 bold', command=stop)

root.mainloop()