from pyautogui import press,click,locateOnScreen,move,hotkey,typewrite,moveTo
from time import sleep 
from random import randint
from threading import Thread,Event
from sys import executable
from os import path,remove
from tkinter import Tk, Listbox, END, IntVar,Entry,Button,NORMAL,DISABLED
from base64 import b64decode

direccion = path.dirname(executable)
exit_event = Event()
def times(seg): 
    sleep(seg) 

def programDigitask(Number):
    x = 0
    v1 = ['claim','continue']
    times(5)
    while x < Number:
        y = 0
        i=330
        while y < 2:
            hotkey('ctrl','g') 
            typewrite(v1[y])
            times(2)
            press('esc')
            if(y == 0):
                iamnotrobot = locateOnScreen(direccion + '\img\iamthree.png', region=(0,0,1000,1000), confidence=0.5)
                if iamnotrobot is None:
                    while i < 950:
                        i+=14
                        moveTo(i,500,0.1)
                        click()
                else:
                    click(iamnotrobot.left + 22,iamnotrobot.top + 18)
            click(locateOnScreen(direccion + f'\img\claim{y}.PNG',confidence = 0.5))
            times(6)
            if exit_event.is_set(): 
                insert_line_finish(x)
                break
            y+=1
        insert_line_status(x)
        x+=1
        times(18)
        if exit_event.is_set(): 
            insert_line_finish(x)
            break
    exit_event.set()
    insert_line_finish(x)
    butonInic['state'] = NORMAL

def button():
    if(type(user.get()) == int and user.get() <= 100):
        Number = user.get()
        butonInic['state'] = DISABLED
        exit_event.clear()
        listbox.insert(0,'Iniciando claim automaticos')
        Thread(target=programDigitask,args=(Number,)).start()
    else:
        listbox.insert(0,'El numero suministrado debe ser menor a 100')
def exits():
    exit_event.set()
    butonInic['state'] = NORMAL

def exitsfinish():
    exit_event.set()
    ventana.destroy()

def insert_line_status(number):
    listbox.insert(0,f'Claim numero: {number + 1}')

def insert_line_finish(numberFinish):
    listbox.insert(0,f'Aplicacion finalizada con: {numberFinish} claim reclamados.')

ventana = Tk()
ventana.geometry("320x180")
ventana.resizable(width=False, height=False)
ventana.configure(bg='#DCDCDC')
ventana.title('AutoClaim Dogecoin 0.1')
ventana.protocol('WM_DELETE_WINDOW',exitsfinish)
listbox = Listbox(ventana,bg = 'black',fg='green')
listbox.insert(END,"Bienvenido a AutoClain Digitask")
listbox.place(relx=0.01,rely=0.03,relwidth=0.98,relheight=0.6)
user = IntVar()
cuadroTex = Entry(ventana,width= 29,textvariable=user)
cuadroTex.place(relx= 0.2, rely= 0.67)
butonInic = Button(ventana,text="Inicio de script",command=button)
butonInic.place(relx= 0.2,rely=0.84)
butonFinish = Button(ventana,text="Detener Script",command=exits)
butonFinish.place(relx= 0.5,rely=0.84)
ventana.mainloop()