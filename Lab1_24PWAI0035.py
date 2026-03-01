#!/usr/bin/env python
# coding: utf-8

#  ## Activity 01

# # PART 1-Variables

# In[1]:


# Define variables
name = "Shahzeb Khan"
age = 19
city = "Peshawar"

# Print variable values
print("Name:", name)
print("Age:", age)
print("City:", city)

# Define number variables
num1 = 10
num2 = 5

# Print operations
print("Sum:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)


# # PART 2 – Input and Output

# In[2]:


# Take input from user
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Display message
print(f"Hello {name}, you are {age} years old")

# Take input of two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Print operations
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)


# # PART 3 – Comments

# In[3]:


# Take user name and age
name = input("Enter your name: ")
age = int(input("Enter your age: "))
# Display greeting message
print(f"Hello {name}, you are {age} years old")
'''
This program takes user input for name, age, and two numbers,
then displays a greeting and performs basic arithmetic operations.
'''
# Get two numbers for calculation
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)


# # PART 4- TYPE CHECK

# In[5]:


# Create variables of different types
var_int = 10
var_float = 3.14
var_str = "Hello"
var_bool = True
var_list = [1, 2, 3]
var_tuple = (1, 2, 3)
var_dict = {"name": "Shahzeb", "age": 19}

# Print types
print(type(var_int))    # <class 'int'>
print(type(var_float))  # <class 'float'>
print(type(var_str))    # <class 'str'>
print(type(var_bool))   # <class 'bool'>
print(type(var_list))   # <class 'list'>
print(type(var_tuple))  # <class 'tuple'>
print(type(var_dict))   # <class 'dict'>


# # PART 5 – Data Type

# In[6]:


# Ask age and print after 10 years
age = int(input("Enter your age: "))
print("Age after 10 years:", age + 10)

# Ask marks and print average
marks1 = int(input("Enter marks 1: "))
marks2 = int(input("Enter marks 2: "))
marks3 = int(input("Enter marks 3: "))
average = (marks1 + marks2 + marks3) / 3
print("Average marks:", average)


# ## PART 1 – Conditions

# # Task 1 – Even or Odd

# In[8]:


# Take a number from user
num = int(input("Enter a number: "))

# Check if number is even or odd
if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")


# # Task 2 – Grade System

# In[9]:


# Take marks from user
marks = int(input("Enter your marks: "))

# Apply grading system
if marks >= 80:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Fail")


# # Task 3 – Voting Eligibility

# In[10]:


age = int(input("Enter your age: "))
if age >= 18:
    print("You can vote")
else:
    print("Not eligible")


# # Task 4 – Print Numbers (For Loop)

# In[13]:


for i in range(1, 11):
    print(i)


# # Task 5 – Multiplication Table

# In[12]:


num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} × {i} = {num * i}")


# # Task 6 – Sum of First 10 Numbers

# In[14]:


total = 0
for i in range(1, 11):
    total += i
print("Sum:", total)


# # Task 7 – Password Checker (Combined Condition + Loop )

# In[15]:


password = ""
while password != "admin1234":
    password = input("Enter password: ")
print("Access granted!")


# # Task 8 – function

# In[16]:


def average(a, b, c):
    return (a + b + c) / 3

print(average(10, 20, 30))


# In[ ]:




