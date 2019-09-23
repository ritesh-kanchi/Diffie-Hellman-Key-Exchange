# Applies shift to message using the message and shared key
def apply_shift(message, key):
    cipher = ""
    # Gets letters in message
    for c in message:
        # each letter is converted into unicode, and the key is added to it, thus shifting each letter by the key
        number = ord(c) + key
        # Puts full encoded message together by running it through chr()
        cipher += chr(number)
        # return cipher variable (encoded message)
    return cipher

def remove_shift(cipher, key):
    message = ""
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
    shared_key = public_key**private_key%public_modulus
    return shared_key

# base for all public keys
public_base = 8
# modulus for all public keys
public_modulus = 29

# exponential values in public keys/ private keys
alice_private_key = 5
bob_private_key = 7

# message from alice to bob
alice_message = "Hello"

# creation of public keys = public_base^private_key%(remainder)public_modulus
alice_public_key = public_base**alice_private_key%public_modulus
bob_public_key = public_base**bob_private_key%public_modulus

# the passage between bob and alice, send from private to public key
alice_shared_key = find_shared_key(alice_private_key,bob_public_key)
# apply shift function to message using sharing key
alice_cipher = apply_shift(alice_message,alice_shared_key)
# final ciphered message
print(alice_cipher)

# ADD MAC SYSTEM

# the passage between alice and bob, recieve from public to private key
bob_shared_key = find_shared_key(bob_private_key,alice_public_key)
# remove shift function to ciphered message using sharing key
bob_message = remove_shift(alice_cipher,bob_shared_key)
print(bob_message)
