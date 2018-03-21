#str = r'\Delta \theta = \frac{U_\text{I}}{M^2}'


def remove_text(str):
    str[0] = '"'
    for n in range(len(str)):
         if str[n] == '}':
             str[n] = '"'
             break
    return str

def remove_frac(str):
    for n in range(len(str)):
         if str[n] == '}':
             str[n] = '/'
             break
    return str



def translate():
    str = entryin.get()
    str = str.replace(" ","")
    str = str.replace('\n','')
    str = list(str)

    for k in range(len(str)):
        if ''.join(str[k:k+5]) == r'\text':
            str = str[:k+5] + remove_text(str[k+5:])

    for k in range(len(str)):
        if ''.join(str[k:k+5]) == r'\frac':
            str = str[:k+5] + remove_frac(str[k+5:])

    nstr = ''.join(str)
    nstr = nstr.replace(r'\text','')
    nstr = nstr.replace(r'\frac','')
    nstr = nstr.replace('{','')
    nstr = nstr.replace('}','')
    entryout.delete(0,'end')
    entryout.insert(0,nstr)

from tkinter import *
window = Tk()
window.geometry('400x120')
entryin = Entry(window,font = ('Times',18))
entryin.insert(0,'copy MathTex code here')
entryout = Entry(window, font = ('Times',18))
entryout.insert(0,'Word equation code shown here')
button = Button(window,text = 'go', font = ('Times',18), command = translate)

entryin.pack(ipadx = 50)
entryout.pack(ipadx = 50)
button.pack(ipadx = 30)
window.mainloop()
