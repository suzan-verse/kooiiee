print("Hello World")

# Don’t forget parentheses in print()
# Strings need to be in quotes "like this"
# Indentation error is very common in Python!
# Python is case-sensitive: Name ≠ name

name="SUJAN KHADKA"
age=20
height=5.8
hobby="football,baketball,coding python"
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





