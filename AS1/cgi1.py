
print("Content-Type:text/html")  # HTTP header specifying content type
print()  # Blank line indicates end of headers, beginning of conten

#reading from the file
with open('numbers.txt','r') as text:
    string=text.read()
    numString= string.split(',')
    numbers=[int(n) for n in numString]
#print(numbers)

#fibonacci formula
temp=numbers[1]+numbers[2]
#print (temp)

#overwrite the numbers
for i in range(0,2):
    numbers[i]=numbers[i+1]
numbers[2]=temp

with open('numbers.txt', 'w') as text:
    text.write(','.join(map(str, numbers)))
#print new arr



# HTML output
print("!DOCTYPE html")
print("<html lang='en'><head><title>Fibonacci Sequence</title></head>")
print("<body>")
print("<h1>Fibonacci Sequence</h1>")
print(f"<p>Current Numbers: {numbers[0]}, {numbers[1]}, {numbers[2]}</p>")
print("<a href='your_cgi_program_url'>Next</a>")  # Link to the same CGI program
print("</body></html>") 