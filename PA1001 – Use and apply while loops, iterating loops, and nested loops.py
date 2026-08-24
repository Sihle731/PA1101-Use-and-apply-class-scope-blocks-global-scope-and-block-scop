'''
Exercise 1

Use a while loop to print numbers from 1 to 10.
'''
num = 1
while(num <= 10):
    print(num)
    num = num + 1

'''
Exercise 2

Use a for loop to print even numbers from 2 to 20.
'''
for i in range(2, 21, 2):
    print(i)

'''
Exercise 3

Create an array of 5 names.

Use a for loop to print each name.
'''
names = ["Themba", "Sihle", "Palesa","Lerato","Karabo"]
for item in names:
    print(item)
    
'''
Exercise 4
Use nested loops to print:

*

**

***

****

*****

(Hint: inner loop prints stars)'''

rows = 5
i = 1
while i <= rows:
    j = 1
    while j <= i:
        print("*", end="")
        j += 1
    print()
    i += 1

