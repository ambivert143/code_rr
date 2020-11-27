import string
import random

def pass_gen():
    s_l = string.ascii_lowercase
    s_u = string.ascii_uppercase
    s_d = string.digits
    s_p = string.punctuation

    # empty list
    pass_list = []

    # add chars to the list
    pass_list.extend(s_l)
    pass_list.extend(s_u)
    pass_list.extend(s_d)
    pass_list.extend(s_p)

    #shuffle password list chars (reorganzine the order of the list otems)
    random.shuffle(pass_list)

    #get password length from user input
    pass_length = int(input("Enter password length: "))

    #convert password list to string from index 0 to password length enterd from user
    pass_result = "".join(pass_list[0:pass_length])

    #print password generated
    print("Password generated is : ", pass_result)

# call password generator function
pass_gen()