#if statement
"""is_male=False
is_tall = False

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but you are tall")
else:
    print("You are either not male or not tall ")"""


#if statement and comparison

"""def max_num(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3

ans=max_num(9,7,9)
print(ans)"""

#Building a better Calculator
num1 = float(input("Enter first number:"))
op=input("Enter the operator:")
num2 = float(input("Enter second number:"))

if op=="+":
    print(num1+num2)
elif op=="-":
    print(num1-num2)
elif op=="/":
    print(num1/num2)
elif op=="*":
    print(num1*num2)
else:
    print("invalid operator")

