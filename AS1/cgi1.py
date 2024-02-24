
print("Content-type: text/html\n") #cgi header

#reading from the file
with open('numbers.txt','r') as text:
    string=text.read()
    numString= string.split(' ')
    numbers=[int(n) for n in numString]
print(numbers)

#fibonacci formula
temp=numbers[1]+numbers[2]
print (temp)

#overwrite the numbers
for i in range(0,2):
    numbers[i]=numbers[i+1]
numbers[2]=temp

#print new arr
print(numbers)