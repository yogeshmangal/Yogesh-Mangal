import random

digits="0123456789"
lcase="abcdefghijklmnopqrstuvwxyz"
ucase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols="@#$%^&*"

max_len=int(input("Enter the length of password: "))

combined_string=digits+lcase+ucase+symbols

'''choice method work for string,list,tuple,etc.'''

rand_digit=random.choice(digits)    
rand_lcase=random.choice(lcase)
rand_ucase=random.choice(ucase)
rand_symbols=random.choice(symbols)

temp_pass=rand_digit+rand_lcase+rand_ucase+rand_symbols
'''Now we have 4 digit temporary password each from digit,lcase,ucase,symbols.
   So we have to generate password of length of password-4'''

for x in range(max_len-4):
    temp_pass=temp_pass+random.choice(combined_string)
    
''' Now, we have 8 digit password in string format, but it is arranged. So we have to
    shuffle it. So, we use shuffle method. But shuffle method works only for list. So,
    first we have to conver this string into list and then shuffle and then again into string'''

temp_pass_list=[i for i in temp_pass]
random.shuffle(temp_pass_list)
password=""
for i in temp_pass_list:
    password+=i
print("Generated password is:",password)
