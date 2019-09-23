#!/usr/bin/python
# -*- coding: utf-8 -*-
# Applies shift to message using the message and shared key
import random

def apply_shift(message, key):
    cipher = ''

    # Gets letters in message

    for c in message:

        # each letter is converted into unicode, and the key is added to it, thus shifting each letter by the key

        number = ord(c) + key

        # Puts full encoded message together by running it through chr()

        cipher += chr(number)

        # return cipher variable (encoded message)

    return cipher


def remove_shift(cipher, key):
    message = ''

    # Gets letters in cipher

    for c in cipher:

        # each letter is converted into unicode, and the key is removed from it, thus shifting each letter back by the key

        number = ord(c) - key

        # Puts full plaintext message together by running it through chr()

        message += chr(number)

        # return message variable (decoded message)

    return message


def find_shared_key(private_key, public_key):

    # create sharing key = public_key^private_key%(remainder)public_modulus

    shared_key = public_key ** private_key % public_modulus
    return shared_key


# sign the message with messages and 2 keys

def sign_message(messages, keys):
    message_int = 0

    # Gets letters in message

    for c in messages:

        # each letter is converted into unicode, and the key is added to it, thus shifting each letter by the key

        message_int += ord(c)

    # a and b keys for encoding, allows easy way to change keys

    a = keys[0]
    b = keys[1]

    # create mac tag from (a*encoded message+b)%491(modulus)

    mac_tag = (a * message_int + b) % p

    # return mac_tag for future usage

    return mac_tag


# check the digital signature by comparing old and new mac tags

def check_mac(old_mac, new_mac):

    # if they are the same, the message is safe

    if old_mac == new_mac:
        print('Message is secure.')
        # the passage between alice and bob, recieve from public to private key

        bob_shared_key = find_shared_key(bob_private_key, alice_public_key)

        # remove shift function to ciphered message using sharing key

        bob_message = remove_shift(alice_cipher, bob_shared_key)
        print("Message Recieved: " + bob_message)


    else:

    # otherwise, the message is compromised

        print('Message compromised')



# base for all public keys

public_base = 8

# modulus for all public keys

public_modulus = 29

# modulus variable

p = 491

# key list

key = [random.randint(1,50), random.randint(1,50)]

# exponential values in public keys/ private keys


bob_private_key = 7

# message from alice to bob
print("============================")
alice_message = input("Please type in a message to encrypt and decrypt: ")
alice_private_key = int(input("Please choose a private key (Level of Encryption): "))
print()

# creation of public keys = public_base^private_key%(remainder)public_modulus

alice_public_key = public_base ** alice_private_key % public_modulus
bob_public_key = public_base ** bob_private_key % public_modulus

# the passage between bob and alice, send from private to public key

alice_shared_key = find_shared_key(alice_private_key, bob_public_key)

# apply shift function to message using sharing key

alice_cipher = apply_shift(alice_message, alice_shared_key)

# final ciphered message: print(alice_cipher)

# message 1

message1 = alice_cipher

# message 2

# message2 = 'Hello World'

# sign the message using the message and key list (2 keys)

mac = sign_message(alice_cipher, key)
print("Unique MAC Tag: " + str(mac))
print()

# sign message 1 and recieve mac_tag 1 (uses the same key)

mac1 = sign_message(message1, key)

# compare original mac with mac_tag 1

check_mac(mac, mac1)

"""
# sign message 2 and recieve mac_tag 2 (uses the same key)

mac2 = sign_message(message2, key)

# compare original mac with mac_tag 2

check_mac(mac, mac2)
"""
print("============================")