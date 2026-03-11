#!/usr/bin/env python
# coding: utf-8

# ## Task 1:
# 

# In[61]:


#ask user for name 

name=input("Enter your name:")

#ask user for favourite colour 

colour=input("Enter your favourite colour")

#we didn't define datatype for name and colour because we need string here and in python "input()" returns string by default

#ask user for birthyear as int
birthyear=int(input("Enter your birthyear:"))

#now we print 3 nice lines using f-strings to enter the data taken as input into those lines

print(f"Good Morning Mr.{name}.")

print(f"Wow! your favourite colour is {colour},great choice i must admit. ")

print(f"Born in {birthyear},you are still quite young :).")


# ## Task 2:

# In[75]:


num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
operation=input("Enter your operation(+,-,*,/,**,%):")

if operation== "+":
    result=num1+num2
elif operation== "-":
    result=num1-num2
elif operation== "*":
    result=num1*num2
elif operation== "/":
    if num2 != 0:
        result=num1/num2
        print(f"{num1} {operation} {num2} = {result:.2f}")
    else:
        print("Cannot divide by zero!")
        
elif operation == "**":
    result=num1**num2
    print(f"{num1} {operation} {num2} = {result:.2f}")
elif operation=="%":
    if num2 != 0:
        result=num1%num2
    else:
        print("Cannot divide by zero!")
else:
    print("Invalid operator.")
print(f"{num1} {operation} {num2} = {result}")


# ## Task 3:
# # Part A:

# In[84]:


starting=int(input("Enter starting Number: "))
ending=int(input("Enter ending Number: "))
num=starting
while num<=ending:
    if num%7==0:
        num+=1
        continue
    if num%2==0 and num%5==0:
        print(f"{num} is Even and multiple of 5")
    elif num%5==0:
        print(f"{num} is multiple of 5")
    elif num%2==0:
        print(f"{num} is Even")
        
    num+=1


# # Part B:

# In[3]:


password = input("Enter a password: ")

if len(password) < 6:
    print("Too short!")
else:
    has_digit = False
    has_upper = False
    
    for letter in password:
        if letter >= '0' and letter <= '9':
            has_digit = True
        if letter >= 'A' and letter <= 'Z':
            has_upper = True
    
    if not has_digit:
        print("Add at least one number")
    elif not has_upper:
        print("Add at least one capital letter")
    else:
        print("Strong password – good choice!")


# In[ ]:




