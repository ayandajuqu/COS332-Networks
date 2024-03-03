#reading from the file
with open('numbers.txt','r') as text:
    string=text.read()
    numString= string.split(',')
    numbers=[int(n) for n in numString]
print(numbers)

#fibonacci formula
temp=[numbers[1]-numbers[0],numbers[0],numbers[1]]
print (temp)



with open('numbers.txt', 'w') as text:
    text.write(','.join(map(str, temp)))


