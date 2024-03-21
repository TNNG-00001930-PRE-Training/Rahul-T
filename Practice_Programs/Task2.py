# 1. Program to find numbers divisible by 7 but not a multiple of 5:
res = []
for num in range(2000, 3201):
    if num % 7 == 0:
        if num %2 != 0:
            res += [str(num)]
temp = ','.join(res)
print(temp)

# 2. Program to generate a dictionary of squares:
res = {}
n = int(input('Enter a range of a number : '))
for i in range(1, n + 1):
    res[i] = i*i

print(res)

# 3. Program to generate a list and a tuple from comma-separated input:
n = input('Enter comma-seperated integers : ')
n = n.split(',')
print(n)
print(tuple(n))

# 4. Class with methods to get and print a string:
class A:
    def getString(self):
        self.string = input('Enter a String : ')
    def printString(self):
        print(f'Modified string : {self.string.upper()}')

def test_function():
    res = A()
    res.getString()
    res.printString()

test_function()

# 5. Program to sort words alphabetically:
string = input('Enter comma-seperated words : ')
L = string.split(',')
L.sort()
print(L)

# 6. Program to remove duplicates and sort words:
string = input('Enter a string : ')
L = string.split()
L = list(set(L))
res = sorted(L)
print(' '.join(res))

# 7. Program to find even digit numbers:
res = []
for num in range(1000, 3001):
    if all( int(digit)%2 == 0 for digit in str(num)):
        res.append(str(num))
print(','.join(res))

# 8. Program to count upper and lower case letters:
string = 'Hello world!'
upper = 0
lower = 0
for ch in string:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    else:
        continue
print(f'Upper letters in the string is : {upper}')
print(f'Lower letters in the string is : {lower}')

# 9. Program to validate passwords:
import re

def validate_password(password):
    if len(password) < 8:
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[$#@]", password):
        return False
    return True

passwords = input("Enter comma-separated passwords: ").split(",")
valid_passwords = [password for password in passwords if validate_password(password)]

if valid_passwords:
    print("Valid password(s):", ",".join(valid_passwords))
else:
    print("No valid passwords found.")
