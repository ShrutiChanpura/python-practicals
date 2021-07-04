# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import hashlib
mystring = input ('enter your string:')
hash_obj = hashlib.md5(mystring.encode())
print(hash_obj.hexdigest())