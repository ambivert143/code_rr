import random
import string

def email_gen():
    chars_after_at = int(input("enter how much chars you want after @gmail.com between 4 and 20 max :"))

    if(chars_after_at < 4 and chars_after_at > 20):
        print('please enter between 4 and 20 char max!')
        exit()
    else:
        letters_list = [string.digits, string.ascii_lowercase, string.ascii_uppercase]
        letters_list_to_str = "".join(letters_list)
        email_format = "@gmail.com"
        email_generated = "".join(random.choice(letters_list_to_str, k=chars_after_at)) + email_format

        print(email_generated)

    email_gen()