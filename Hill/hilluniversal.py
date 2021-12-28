# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 16:34:26 2021

@author: Pavel
"""

import numpy as np
from egcd import egcd  # pip install egcd

alphabet = "abcdefghijklmnopqrstuvwxyz "

letter_to_index = dict(zip(alphabet, range(len(alphabet))))
index_to_letter = dict(zip(range(len(alphabet)), alphabet))


def matrix_mod_inv(matrix, modulus):
    """Găsim modulul matricei invers cu
     Pasul 1) Găsiți determinantul
     Pasul 2) Găsiți valoarea determinantului într-un anumit modul (de obicei lungimea alfabetului)
     Pasul 3) Luați acel det_inv ori det*matricea inversată (aceasta va fi apoi adjunctul) în mod 26
    """

    det = int(np.round(np.linalg.det(matrix)))  # Pas 1)
    det_inv = egcd(det, modulus)[1] % modulus  # Pas 2)
    matrix_modulus_inv = (
        det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % modulus
    )  # Pas 3)

    return matrix_modulus_inv


def encrypt(message, K):
    encrypted = ""
    message_in_numbers = []

    for letter in message:
        message_in_numbers.append(letter_to_index[letter])

    split_P = [
        message_in_numbers[i : i + int(K.shape[0])]
        for i in range(0, len(message_in_numbers), int(K.shape[0]))
    ]

    for P in split_P:
        P = np.transpose(np.asarray(P))[:, np.newaxis]

        while P.shape[0] != K.shape[0]:
            P = np.append(P, letter_to_index[' '])[:, np.newaxis]

        numbers = np.dot(K, P) % len(alphabet)
        n = numbers.shape[0]  # lungimea mesajului criptat (în cifre)

        # Harta înapoi pentru a obține text criptat
        for idx in range(n):
            number = int(numbers[idx, 0])
            encrypted += index_to_letter[number]

    return encrypted


def decrypt(cipher, Kinv):
    decrypted = ""
    cipher_in_numbers = []

    for letter in cipher:
        cipher_in_numbers.append(letter_to_index[letter])

    split_C = [
        cipher_in_numbers[i : i + int(Kinv.shape[0])]
        for i in range(0, len(cipher_in_numbers), int(Kinv.shape[0]))
    ]

    for C in split_C:
        C = np.transpose(np.asarray(C))[:, np.newaxis]
        numbers = np.dot(Kinv, C) % len(alphabet)
        n = numbers.shape[0]

        for idx in range(n):
            number = int(numbers[idx, 0])
            decrypted += index_to_letter[number]

    return decrypted


def main():
    message = input("Introduceti mesajul: ").lower()
    

   # K = np.matrix([[3, 3], [2, 5]])
    #K = np.matrix([[6, 24, 1], [13,16,10], [20,17,15]]) # for length of alphabet = 26
    K = np.matrix([[3,10,20],[20,19,17], [23,78,17]]) # for length of alphabet = 27
    Kinv = matrix_mod_inv(K, len(alphabet))

    encrypted_message = encrypt(message, K)
    decrypted_message = decrypt(encrypted_message, Kinv)

    print("Mesaj Clar: " + message)
    print("Mesaj Criptat: " + encrypted_message)
    print("Mesaj Decriptat: " + decrypted_message)


main()