import string
passwd = input()
passwd_len = len(passwd)
len_passwd_check = False
punctuation_check = False
digit_check = False
lowercase_check = False
uppercase_check = False
if passwd < 6 or i > 10:
 	check = True
for i in passwd:    
    if i in string.punctuation: 
        punctuation_check = True
    if i in string.digits:
        digit_check = True 
    if i in string.ascii_lowercase:
        lowercase_check = True
    if i in string.ascii_uppercase:
        upercase_check = True
if len_passwd_check and punctuation_check and digit_check and lowercase_check and uppercase_check:
    print("Valid Password")
    print("Strength = ", end="")
    print(passwd_len)
    if passwd_len < 7:
        print("Weak")
    elif passwd_len < 9:
        print("Medium")
    else:
        print("Strong")
else:
    print("Invalid password")