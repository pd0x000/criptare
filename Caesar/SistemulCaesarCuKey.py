# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 21:05:58 2021

@author: Pavel
"""

alphabet = "abcdefghijklmnopqrstuvwxyz "#declaram alfabetul
letter_to_index = dict(zip(alphabet, range(len(alphabet)))) #facem conversia din litere in numarul de ordine din alfabet
index_to_letter = dict(zip(range(len(alphabet)), alphabet)) #facem conversia din numarul de ordine din alfabet in litere


def encrypt(message, shift=3): # functia pentru criptare cu parametrii mesaj si keye
    cipher = "" # variabila pentru a salva mesajul criptat

    for letter in message:#cream un ciclu pentru fiecare litera din mesajul clar
        number = (letter_to_index[letter] + shift) % len(letter_to_index) #adunam numarul de ordine al literei cu keya apoi facem mod 26 (lungimea alfabetului)
        letter = index_to_letter[number] #facem conversia numarului in litera corespunzatoare din alfabet
        cipher += letter #o scrim in variabila noastra

    return cipher #returnam mesajul criptat


def decrypt(cipher, shift=3):# functia pentru decriptare cu parametrii mesaj si keye
    decrypted = "" # variabila pentru a salva mesajul decriptat

    for letter in cipher: #cream un ciclu pentru fiecare litera din mesajul criptat
        number = (letter_to_index[letter] - shift) % len(letter_to_index) #scadem din numarul de ordine al literei  keya apoi facem mod 26 (lungimea alfabetului)
        letter = index_to_letter[number] #facem conversia numarului in litera corespunzatoare din alfabet
        decrypted += letter #o scrim in variabila noastra

    return decrypted #returnam mesajul clar

def main():
     message = input("Introduceti un mesaj:\n") # citim de la tastatura mesajul clar
     key = int(input("Introduceti key-a:\n")) # citim de la tastatura key-a
     cipher = encrypt(message, shift=key) # salvam in variabila cipher raspunsul returnat de functia de criptare  (mesajul criptat)
     decrypted = decrypt(cipher, shift=key)  # salvam in variabila decrypted raspunsul returnat de functia de decriptare (mesajul decriptat)

     print('Mesaj Original: ' + message) # Afisam mesajul clar
     print('Mesaj Criptat: ' + cipher) #afisam mesajul criptat
     print('Mesaj Decriptat: ' + decrypted) #afisam mesajul decriptat

main()



