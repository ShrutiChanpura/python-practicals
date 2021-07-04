# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import hashlib
mystring = input ('enter your string:')
hash_obj = hashlib.md5(mystring.encode())
print(hash_obj.hexdigest()

#algorithms
#hash with SHA-2 (SHA-256 & SHA-512)
print("SHA-256:", hashlib.sha256(mystring).hexdigest())
print("SHA-512:", hashlib.sha512(mystring).hexdigest())

#hash with SHA-3
print("SHA-3-256:", hashlib.sha3_256(mystring).hexdigest())
print("SHA-3-512:", hashlib.sha3-512(mystring).hexdigest())

#hash with BLAKE2
#256-bit BLAKE2 (or BLACK2s)
print("BLAKE2c:", hashlib.blake2s(mystring).hexdigest())