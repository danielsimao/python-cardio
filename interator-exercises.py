#---------- Iterators ------------#

# Question 1: The while statement tells Python to repeatedly execute some target statements for as long as a given condition is true.
# What is the problem with the following code?

n = 3

while(n > 0):
    print(n)
    n += 1

# Question 2: Explain the behavior of the following code. It is the job of the break keyword?

while True:
    line = input('Enter text? ')
    if line == 'done':
        break
    print(line)
print('The end')

# Hint: this is loop-and-a-half

# Question 3: for loop repeats statements once for each item in a collection of items, such as a list, a string or a tuple. Explain the way the code is processed
# in the following code:

for var in [1,4,5]:
    print(var)

# Question 4: What is the output from the following function?

print(range(2,4))

# Question 5: Write a function that sums all the numbers of a list with numbers from "start" to "end" parameters

# Question 6: Which are the three loop control statments?

# Question 7: What is the output from the following code

for var in range(2,11)
    if var%2==0
        print(var)
    else:
        continue

# Question 8: What is the output from the following code

for var in range(stop = 100)
    if var > 31
        break
    else:
        continue
