import hashlib

user_entered_password = input('enter your password:')
salt = "5gz"
new_password= user_entered_password+salt
h = hashlib.md5(new_password.encode())
print(h.hexdigest())

