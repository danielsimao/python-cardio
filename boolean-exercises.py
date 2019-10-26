#---------- Boolean expressions ------------#

# Theory Question 1: What's the difference between n = 7 and n == 7

# Awnser: 

# Pratical Question 1: Write an isEven function, which should return true if the specified number if even and false if it is not

def isEven(number):
    return 1;


# Theory Question 2: What is the value of the following variables

val1 = isEven(10) #
val2 = str(val1) #
val3 = int(val2) #
val4 = int(isEven(3)) #
val5 = bool(0) #
val6 = bool(0.0) #
val7 = bool("") #
val8 = bool([]) #
val9 = bool(1) #
val10 = bool(val3) #
val11 = bool([val5]) #

#---------- Relational and logical operators ------------#


# Pratical Question 2:
# a) The following functions has three arguments, which should return true if y is between x and z inclusive. But it's not working properly
# b) Rewrite it using logical operators (and, or, not)

# Fun fact: this function uses only Relational operators
def isBetween(x,y,z):
    return x < y < z

# Pratical Question 3: Using logical operators, write a different way of presenting the following property

def checkAnwser(prop1, prop2):
    if prop1 == prop2:
        print("Correct!")
    else:
        print("Buuuuuh!")
    return;

prop1 = 2==3
prop2 = 2!=3

print(checkAnwser(prop1,prop2))

prop1 = 2>3
prop2 = 2<=3

print(checkAnwser(prop1,prop2))

# Theory Question 3: What is the value of the following variables

val12 = true and true
val13 = true or true
val14 = true and not true
val15 = true or not false
val16 = true not not not not not not val15

# Hint: Operators and and or only evaluate the second operand if needed! (short-circuit evaluation)

def function1(n):
    return n==0 or 3/n<4

function1(0) # What does this return? 
function1(3) # What about this one?

# Pratical Question 4: This function look terrible! Rearrange it please

def unCoolFunc():
    if a>=10:
        if b<3:
            return 2
        else:
            return 3
    else:
        return 1


# Theory Question 4: What is the output from the following trenary operator

p = 2
val17 = "odd" if p%2!=0 else "even"





