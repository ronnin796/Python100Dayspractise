import string 
import random
letters = list(string.ascii_letters)
numbers = list(string.digits)
symbols = list(string.punctuation)
print('Welcome to Python Password Generator')
nr_length = int(input('Enter the length of your password: '))
nr_symbols = int(input('Enter the number of symbols: '))
nr_numbers = int (input('Enter number of numbers: '))

password = []
new_password=''
while len(password)<(nr_length-nr_symbols-nr_numbers):
      password.append(random.choice(letters))

for i in range(nr_symbols):
        password.append(random.choice(symbols))
for i in range(nr_numbers):
    password.append(random.choice(numbers))

random.shuffle(password)
print(password)
for i in password:
    new_password+=i
print('Your password is : ',new_password)