import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder

Phonenumber = input("Enter your phone number: ")

number = phonenumbers.parse(Phonenumber)

print(geocoder.description_for_number(number, 'vi'))

print(carrier.name_for_number(number, 'vi'))
