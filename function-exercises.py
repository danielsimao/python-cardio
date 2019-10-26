#---------- Functions ------------#

# Question 1: What's wrong with the following function? What is x?

def square(x): # What is the name of the this part of the function
y = x**2 # What about this one?
return y

# Questions 2: What's the difference between the the previous function the following

print(square(2))

# Question 3: What happens if the function is defined but not used? Is it gone?

# Question 4: What happens in the following functions?

def eatCake():
    print("Yummy")

def repeatCake():
    eatCake()
    print("Feeling Guilty")
    eatCake()
    print("Go to gym")

# Question 5: The square function returns a value, so it produces something. What about print function? Does it return a value?

# Question 6: What will print ouput in the following function?

def epicFunction():
    return;

print(epicFunction())

# Question 7: The variable total in the following code serve the same purpose? What is the difference between them?

total = 0

def add(a, b):
    total = a + b 
    print("Inside the function local total: ", total)
    return total

print( add(10, 20))
print("Outside the function global total: ", total)

# Question 8: Some aspects seem odd on the following function. Make the following function executable.

def printinfo1():
    print("Name:", name)
    print("Age:", age)

printinfo1( age=50, name="miki" )

# Question 9: What is the output of the following function when executed?

def printinfo2(name="Sophie", age=17):
    print("Name:", name)
    print("Age:", age)

printinfo2()

# Question 10: What is the output of the following function when executed? What is the purpose of the " * "?

def printVariableLength( arg1, *args ):
    print(arg1)
    for var in args:
        print(var)

printVariableLength( "Jane" )
printVariableLength( "Sophie", "Jane", "Pousinho" )

# Question 11: A lambda expression is an expression whose result is a function. What makes it different from the functions we have been using? 


# Question 12: Write a isEven as a lambda function (lambda p: ...)
