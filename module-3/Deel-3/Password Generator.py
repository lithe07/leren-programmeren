# import string
# import secrets

# symbols = ['@', '%', '$', '#', '&', '_', '?'] 

# password = ""
# for _ in range(21):
#     password += secrets.choice(string.ascii_lowercase)
# password += secrets.choice(string.ascii_uppercase)
# password += secrets.choice(string.digits)
# password += secrets.choice(symbols)
# print(password)
# print(len(password))



import random
import string

length = 24
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
    
all = lower + upper + num + symbols

temp = random.sample(all,length)

password = "".join(temp)

print(password)
print(len(password))




