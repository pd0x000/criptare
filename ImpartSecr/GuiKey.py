# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 13:21:17 2021

@author: Pavel
"""
import tkinter as tk
import random
root= tk.Tk()
root.resizable(0,0)
root.title('Impartirea secretelor by Pavel Dordea')
root.configure(bg='#164A41')
L1=tk.Label(root,text="Introdu cheia secreta s :",bg='#164A41',fg='#FFFFFF',font='Helvetica 14 bold').grid(row=0,column=0,sticky='w')
sec = tk.Entry(root,bg='white',fg='black',font='Helvetica 13 bold')
sec.grid(row=0,columnspan=3,sticky='ne')
L2=tk.Label(root,text="Introdu n (in cite parti va fi divizat secretul):",bg='#164A41',fg='#FFFFFF',font='Helvetica 14 bold').grid(row=1,column=0,sticky='w')
nec = tk.Entry(root,bg='white',fg='black',font='Helvetica 13 bold')
nec.grid(row=1,columnspan=3,sticky='ne')
L3=tk.Label(root,text="Introdu k (cite bucati sunt necesare pentru restabilirea cheii):",bg='#164A41',fg='#FFFFFF',font='Helvetica 14 bold').grid(row=2,column=0,sticky='w')
kec = tk.Entry(root,bg='white',fg='black',font='Helvetica 13 bold')
kec.grid(row=2,column=1)
b=[] 
L7=tk.Label(root,text="",bg='#164A41',fg='#FFFFFF',font='Helvetica 10 bold')
L7.grid(row=6,column=1,sticky='w')
def afla():
    s=sec.get()
    s = int(sec.get())
    k = int(kec.get())
    a = random.sample(range(1, 100), k)
    n = int(nec.get())
    def F(t):
        w = s
        for i in range(len(a)):
            w += a[len(a)-i-1]*pow(t,len(a)-i)
        return w
#a=[12,3,15,7,20,26]
    L5["text"]=str(a)
    for i in range (1,n+1):
        b.append(F(i))
    for i in range (0,n):
        L7["text"]+=("["+str(i+1)+"]   "+str(b[i])+" \n")
    L10['text']+="("+str(k+1)+' pozitii din lista de mai sus):'
x=[]
def calc():
    y=[] 
    final=0
    k = int(kec.get())
    for i in range(k+1):
        value = (nume.get())
        value = value.split(' ')
        x = [int(x) for x in value]
        y.append(b[x[i]-1])

    for g in range(k+1):
        p2=p1=1
        for r in range(k+1):
            if (g != r):
              p2 *= (x[g]-x[r])
              p1 *= x[r]
        final += ((p1*y[g])/p2)
    L12["text"]="CHEIA  RESTABILITA  ESTE:"
    L13["text"]=round(final)
button_afla = tk.Button(root,text="Crypteaza",command=afla,bg='#4D774E',fg='#FFFFFF',font='Helvetica 12 bold').grid(row=4,columnspan=3,sticky='we')
L4=tk.Label(root,text="Numerele aleatoare generate:",bg='#164A41',fg='#FFFFFF',font='Helvetica 12 bold').grid(row=5,column=0,sticky='w')
L5=tk.Label(root,text="",bg='#164A41',fg='#FFFFFF',font='Helvetica 10 bold')
L5.grid(row=5,column=1,sticky='w')
L6=tk.Label(root,text="Perechile de numere in care a fost impartita cheia:",bg='#164A41',fg='#FFFFFF',font='Helvetica 12 bold').grid(row=6,column=0,sticky='w')
L8=tk.Label(root,text="RESTABILIREA  CHEII:",bg='#164A41',fg='#FFFFFF',font='Helvetica 12 bold underline').grid(row=7,column=0,columnspan=3,sticky='n')
L9=tk.Label(root,text="Introduceti perechile de numere care participa la restabilirea cheii:",bg='#164A41',fg='#FFFFFF',font='Helvetica 12 bold').grid(row=8,column=0,sticky='w')
L10=tk.Label(root,text="Numarul de ordine a perechii ",bg='#164A41',fg='#FFFFFF',font='Helvetica 12 bold')
L10.grid(row=9,column=0,sticky='w')
nume=tk.Entry(root,bg='white',fg='black',font='Helvetica 13 bold')
nume.grid(row=9,column=1,sticky='w')
L12=tk.Label(root,text="",bg='#164A41',fg='red',font='Helvetica 12 bold')
L12.grid(row=11,column=0,columnspan=3,sticky='w')
L13=tk.Label(root,text="",bg='#164A41',fg='red',font='Helvetica 12 bold')
L13.grid(row=11,column=1,sticky='ne')
button_calc = tk.Button(root,text="Decrypteaza",command=calc,bg='#4D774E',fg='#FFFFFF',font='Helvetica 12 bold').grid(row=10,columnspan=3,sticky='we')
root.mainloop()