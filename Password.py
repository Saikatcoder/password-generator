import random
letters =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w',
          'x','y','z']
number =['1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','(',')','+']

nr_letters = int(input("How many number do you want in your password?\n"))
nr_symbols = int(input("How many symbols do you want in your password?\n"))
nr_number = int(input("How many number do you want in your password?\n"))

password_list =[]
for char in range (1, nr_letters , +1):
    password_list +=random.choice(letters)

for char in range (1, nr_number , +1):
    password_list += random.choice(number)

for char in range (1, nr_symbols , +1):
    password_list += random.choice(symbols)

print(password_list)
random.shuffle(password_list)
print(password_list)

password =""
for char in password:
    password += char
print(f'your password is{password}')

