# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 21:10:52 2021

@author: Pavel
"""
import tkinter as tk
root= tk.Tk()
root.resizable(0,0)
root.title('Sistemul "Vigenere" by Pavel Dordea')
root.configure(bg='#164A41')

#___________________pentru user input_____________________________
L1=tk.Label(root,text="Introdu mesajul clar :",bg='#164A41',fg='#FFFFFF',font='Helvetica 14 bold')
clear_message = tk.Entry(root,bg='white',fg='black',font='Helvetica 13 bold')
L2=tk.Label(root,text="Introdu cheia secreta :",bg='#164A41',fg='#FFFFFF',font='Helvetica 14 bold')
cheie = tk.Entry(root,bg='white',fg='black',font='Helvetica 13 bold')

alphabet = "abcdefghijklmnopqrstuvwxyz "
letter_to_index = dict(zip(alphabet, range(len(alphabet))))#transformam din litere in numarul de ordine din alfabet
index_to_letter = dict(zip(range(len(alphabet)), alphabet))#transformam din numarul de ordine din alfabet in litere
message =''
key=''
def show_user():
    L1.grid(row=2,column=0,sticky="w")
    L2.grid(row=3,column=0,sticky="w")
    clear_message.grid(row=2,column=2,sticky='ne')
    cheie.grid(row=3,column=2,sticky='ne')
    L3.grid(row=5,column=0,sticky='w')
    button_crypt.grid(row=4,columnspan=3,sticky='we')
    L4.grid(row=6,columnspan=3,sticky='w')
    button_show.grid(row=7,column=2,sticky='ne')
    b1.grid_forget()
    l3.grid_forget()
    b2.grid_forget()
def show_file():
    L1.grid_forget()
    L2.grid_forget()
    clear_message.grid_forget()
    cheie.grid_forget()
    L3.grid_forget()
    button_crypt.grid_forget()
    L4.grid_forget()
    button_show.grid_forget()
    b1.grid(row=2,column=0,sticky='w')
    l3.grid(row=2,column=1)
    b2.grid(row=2,column=2,sticky='ne')
    crypted.grid_forget()
    
    L5.grid_forget()
    button_hide.grid_forget()
    L6.grid_forget()
    crypted_message.grid_forget()
    L7.grid_forget()
    reverse_key.grid_forget()
    button_decrypt.grid_forget()
    L8.grid_forget()
    clr_message.grid_forget()
def encrypt(message, key): #functia de criptare
    crypted.delete(0,tk.END)
    message = clear_message.get().lower()
    key = cheie.get().lower()
    encrypted = ""
    split_message = [
        message[i : i + len(key)] for i in range(0, len(message), len(key))
    ] # despartim mesajul in bucati de lungimea key-ului
    for each_split in split_message:
        i = 0
        for letter in each_split:
            number = (letter_to_index[letter] + letter_to_index[key[i]]) % len(alphabet)
            #convertim fiecare litera in numarul de oridne  adunam key-a (mod26)
            encrypted += index_to_letter[number]
            #convertim din numerele de ordine in literele corespunzatoare
            i += 1 
    L3["text"]="MESAJUL  CRIPTAT  ESTE :"
    crypted.insert(0,encrypted)
    crypted.grid(row=5,column=2,sticky='ne') #returnam mesajul criptat
def decrypt(cipher, key):
    cipher = crypted.get().lower()
    key =reverse_key.get().lower()
    decrypted = ""
    split_encrypted = [
        cipher[i : i + len(key)] for i in range(0, len(cipher), len(key))
    ] # despartim mesajul in bucati de lungimea key-ului

    for each_split in split_encrypted:
        i = 0
        for letter in each_split:
            number = (letter_to_index[letter] - letter_to_index[key[i]]) % len(alphabet)
            #convertim fiecare litera in numarul de oridne  si scadem key-a (mod26)
            decrypted += index_to_letter[number]
            #convertim din numerele de ordine in literele corespunzatoare
            i += 1
    L8.grid(row=12,column=0,sticky='w')
    clr_message.insert(0,decrypted)
    clr_message.grid(row=12,column=2,sticky='ne') #returnam mesajul criptat
def show():
    button_show.grid_forget()
    L5.grid(row=8,columnspan=3,sticky='w')
    button_hide.grid(row=7,column=0,sticky='w')
    L6.grid(row=9,column=0,sticky='w')
    crypted_message.grid(row=9,column=2,sticky='ne')
    L7.grid(row=10,column=0,sticky='w')
    reverse_key.grid(row=10,column=2,sticky='ne')
    button_decrypt.grid(row=11,columnspan=3,sticky='we')
def hide():
    L5.grid_forget()
    button_show.grid(row=7,column=2,sticky='ne')
    button_hide.grid_forget()
    L6.grid_forget()
    crypted_message.grid_forget()
    L7.grid_forget()
    reverse_key.grid_forget()
    button_decrypt.grid_forget()
    L8.grid_forget()
    clr_message.grid_forget()
#_______________________________________________________________

def show_crypt():
    key_crypt.delete(0,tk.END)
    L1['text']= 'Introdu cheia de criptare:'
    L1.grid(row=3,column=0,sticky="w")
    key_crypt.grid(row=3,column=2,sticky='ne')
    butt_crypt.grid(row=4,columnspan=3,sticky='we')
    l3["text"]="  "
def show_decrypt():
    key_crypt.delete(0,tk.END)
    L1['text']= 'Introdu cheia de decriptare:'
    L1.grid(row=3,column=0,sticky="w")
    key_crypt.grid(row=3,column=2,sticky='ne')
    butt_decrypt.grid(row=4,columnspan=3,sticky='we')
    l3["text"]="  "
def getmsg():
    message = open('Message.txt', 'r+').read().lower().replace('\n',' ')
    return message
def getkey():
    cheie = key_crypt.get()
    return cheie
def fencrypt(): #functia de criptare
    message=getmsg()
    key =getkey()
    encrypted = ""
    split_message = [
        message[i : i + len(key)] for i in range(0, len(message), len(key))
    ] # despartim mesajul in bucati de lungimea key-ului
    for each_split in split_message:
        i = 0
        for letter in each_split:
            number = (letter_to_index[letter] + letter_to_index[key[i]]) % len(alphabet)
            #convertim fiecare litera in numarul de oridne  adunam key-a (mod26)
            encrypted += index_to_letter[number]
            #convertim din numerele de ordine in literele corespunzatoare
            i += 1 
    f = open("Encrypted.txt", "w+")
    f.write(encrypted)#returnam mesajul criptat
    l3["text"]="Success !            "
    


def getenc():
    encrypted = open('Encrypted.txt', 'r+').read().lower().replace('\n',' ')
    return encrypted

def fdecrypt():
    cipher = getenc()
    key =getkey()
    decrypted = ""
    split_encrypted = [
        cipher[i : i + len(key)] for i in range(0, len(cipher), len(key))
    ] # despartim mesajul in bucati de lungimea key-ului

    for each_split in split_encrypted:
        i = 0
        for letter in each_split:
            number = (letter_to_index[letter] - letter_to_index[key[i]]) % len(alphabet)
            #convertim fiecare litera in numarul de oridne  si scadem key-a (mod26)
            decrypted += index_to_letter[number]
            #convertim din numerele de ordine in literele corespunzatoare
            i += 1
    f = open("Decrypted.txt", "w+")
    f.write(decrypted)
    l3["text"]="Success !            "

#_______________________________________________________________
#______________pentru user input______________________________
user = tk.Button(root,text="De la user",command=show_user ,bg='#4D774E',fg='#FFFFFF',font='Helvetica 12 bold')
user.grid(row=1,columnspan=3,padx=200,pady=10,sticky='we')
button_crypt = tk.Button(root,text="Cripteaza",command=lambda: encrypt(message, key) ,bg='#4D774E',fg='#FFFFFF',font='Helvetica 12 bold')
L3=tk.Label(root,text="",bg='#164A41',fg='red',font='Helvetica 12 bold')
crypted=tk.Entry(root,bg='white',fg='black',font='Helvetica 13 bold')
L4=tk.Label(root,text="_______________________________________________________________",bg='#164A41',fg='#ffffff',font='Helvetica 12 bold')
button_show = tk.Button(root,text="Mai mult",command=show ,bg='#4D774E',fg='#FFFFFF',font='Helvetica 7 bold')
button_hide = tk.Button(root,text="Mai putin",command=hide ,bg='#4D774E',fg='#FFFFFF',font='Helvetica 7 bold')
L5=tk.Label(root,text="_______________________________________________________________",bg='#164A41',fg='#ffffff',font='Helvetica 12 bold')
L6=tk.Label(root,text="Introdu mesajul criptat :",bg='#164A41',fg='#ffffff',font='Helvetica 12 bold')
crypted_message=tk.Entry(root,bg='white',fg='black',font='Helvetica 13 bold')
L7=tk.Label(root,text="Introdu cheia secreta :",bg='#164A41',fg='#ffffff',font='Helvetica 12 bold')
reverse_key=tk.Entry(root,bg='white',fg='black',font='Helvetica 13 bold')
button_decrypt=tk.Button(root,text="Decripteaza",command=lambda: decrypt(message, key) ,bg='#4D774E',fg='#FFFFFF',font='Helvetica 12 bold')
L8=tk.Label(root,text="MESAJUL  CLAR ESTE :",bg='#164A41',fg='red',font='Helvetica 12 bold')
clr_message = tk.Entry(root,bg='white',fg='black',font='Helvetica 13 bold')
#__________________________pentru fisiere____________________________________
fisiere = tk.Button(root,text="Din fisier",command=show_file ,bg='#4D774E',fg='#FFFFFF',font='Helvetica 12 bold')
fisiere.grid(row=0,columnspan=3,padx=200,pady=10,sticky='we')

Lf1=tk.Label(root,text="",bg='#164A41',fg='#FFFFFF',font='Helvetica 14 bold')
key_crypt = tk.Entry(root,bg='white',fg='black',font='Helvetica 13 bold')

b1 = tk.Button(root,text="Codificare",command= show_crypt ,bg='#4D774E',fg='#FFFFFF',font='Helvetica 12 bold')

l3=tk.Label(root,text="   ",bg='#164A41',fg='darkred',font='Helvetica 12 bold')

b2 = tk.Button(root,text="Decodificare",command= show_decrypt ,bg='#4D774E',fg='#FFFFFF',font='Helvetica 12 bold')

butt_crypt = tk.Button(root,text="Cripteaza",command= fencrypt ,bg='#4D774E',fg='#FFFFFF',font='Helvetica 12 bold')
butt_decrypt = tk.Button(root,text="Decripteaza",command= fdecrypt ,bg='#4D774E',fg='#FFFFFF',font='Helvetica 12 bold')

root.mainloop()