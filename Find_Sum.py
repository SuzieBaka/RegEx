import re
fname = str(input("Enter a file name: "))
fhand = open(fname)
numbers = re.findall('[0-9]+', fhand.read())
sum = 0
for number in numbers:
    number = int(number)
    sum += number
print(sum)