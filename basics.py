print("Hello World")

# Don’t forget parentheses in print()
# Strings need to be in quotes "like this"
# Indentation error is very common in Python!
# Python is case-sensitive: Name ≠ name

name="SUJAN KHADKA"
age=20
height=5.8
hobby="football,baketball,coding python, barista"
feeling_rn=True
print(f"""HI, MY NAME IS {name} and I am {age} years old.
     My hobbies are {hobby} and height is {height}ft.""")  #fstring for smart printing


print(type(name))
print(type(age))
print(type(height))
print(type(feeling_rn))
print(type(6666.666))
print(type("77.77"))
# Variable names must start with a letter or _
# Can include numbers after the first letter
# No spaces or symbols like @, -, .

# TYPE CONVERSION (IMPLICIT {AUTOMATIC BY PY} AND EXPILICIT{MANUAL FOR PY} CONVERSION )

num="100"            #Example 1
int_num= int(num)
print(int_num)

pin="20202.6"        #Example 2
int_pin=int(float(pin))
# string is converted to integer here
# in eg.2 can’t convert string float directly to int so we must convert to float first

val= 10
new_val= float(val)
print(new_val)
# integer is converted to floating value here

sum= 888888.909
n_sum= int(sum)
print(n_sum)
# floating value is converted to integer here
# this basically removes decimal part- not rounds, just cuts

age= 30
text= str(age)
print(text)
# integer is converted to string here 

print(bool(0))        # False
print(bool(1))        # True
print(bool(""))       # False
print(bool("Hello"))  # True
print(bool(None))     #False
print(bool("Hero"))   #True
# converting anything to boolean 
# here "0","0.0","[]","None"  gives false and other gives True

# conditional statement  (if-elif-else)
# condition is any expression that evaluate to either True/False. Baically, it is a test where the output is yes/no.

# for example   5>3 (True), "cat"=="dog" (False), 3!=5 (True), "5"*3 == 111*5 (True)
# lets use if elif else statement in python

balance= int(input("Entre the balance:"))   #example 1

if balance >=10000:
    print("High Income")

elif 5000<= balance <=10000:
    print("Average Income")

else :
    print("Below average")


num1= int(input("Entre the first number:"))  #example 2
num2= int(input("Entre the second number:"))

if num1>num2 :
    print(f"The number {num1} is greater.")

elif num2 > num1 :
    print(f"The number {num2} is greater.")

else :
    print(f"The number {num1} and {num2} are equal. ")    
 
income = 50000   #nested if (example 3)
age = 30

if income > 40000:
    if age > 22:
        print("Eligible for loan")
    else:
        print("Too young")
else:
    print("Income too low")

# operators (comparision & logical)
# == (equal to) , != (not equal to) , >= (greater or euqal to) , <= (less 0r equal to)

# and operator (only runs if both conditions are true)
# or operator (runs even if only one condition is true)
# not operator (reverse the condition true becomes false and vice -versa)

age =int(input("Entre the age:"))  #example 1 and operator
citizen = False

if age>18 and citizen:
    print("you can vote.")
else:
    print("you are not eligible.")


hey=int(input("Entre the number:"))  #example 2 or operator

if hey <1 or hey>10:
    print("out of range.")
else:
    print("With in range.")



