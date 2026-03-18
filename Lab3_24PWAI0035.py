#!/usr/bin/env python
# coding: utf-8

# # Task 1

# In[2]:


def welcome_message():
    print("Welcome to Python Programming Lab")

welcome_message()
    


# # Task 2

# In[4]:


def add_numbers(a,b):
    return a+b
add_numbers(2,3)


# # Task 3

# In[8]:


def functionB():
    print("Inside Function B")
def functionA():
    print("Inside Function A")
functionB()
functionA()
        


# # Task 4

# In[19]:


def greet(name="Student"):
    
    
    print("Hello", name)
greet()
greet("Shahzeb")


# # Task 5

# In[22]:


x=10
def show():
    print("Global x=",x)
    y=20
    print("Local y=",y)
show()



# # Task 6

# In[26]:


def total_numbers(*numbers):
    total=sum(numbers)
    return total
print("Total Numbers: ",total_numbers(1,4,67,23))


# # Task 7

# In[44]:


def student_info(**data):
    for key,value in data.items():
        print(key ,":",value)
student_info(name="Shahzeb",age=19)
    
    


# # Task 8

# In[36]:


Sq=lambda x:x*x
print("Square =",Sq(5))


# # Task 9

# In[38]:


numbers = [1,2,3,4,5]
sq=list(map(lambda x:x*x,numbers))
print(sq)


# # Task 10

# In[40]:


numbers = [45,67,82,30,90,55]
result=list(filter(lambda x:x>50,numbers))
print(result)


# # Task Mini Project: Student Marks Analyzer

# In[8]:


def get_marks():
    marks = list(map(int, input("Enter marks (comma separated): ").split(",")))
    return marks

def calculate_total(marks):
    return sum(marks)

def calculate_average(marks):
    return sum(marks) / len(marks)

def main():
    marks = get_marks()
    total = calculate_total(marks)
    average = calculate_average(marks)
    highest = max(marks, key=lambda x: x)
    
    print(f"Total Marks: {total}")
    print(f"Average Marks: {average:.2f}")
    print(f"Highest Mark: {highest}")

main()


# # AI Number Guessing Game Lite

# In[9]:


import random

print(" AI Number Guessing Game ")
print("I'm thinking of a number between 1 and 50.")
print("You have 7 attempts to guess it.\n")

secret = random.randint(1, 50)
attempts = 7

while attempts > 0:
    # Ask for guess and validate
    try:
        guess = int(input(f"Guess ({attempts} attempts left): "))
        if guess < 1 or guess > 50:
            print("Please enter a number between 1 and 50.")
            continue
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue
    
    # Check guess
    if guess > secret:
        print("Too high!")
    elif guess < secret:
        print("Too low!")
    else:
        print(f"\nCongratulations! You win in {7 - attempts + 1} attempts! Seems like someone's guessing game is strong :)")
        break
    
    attempts -= 1
    print()
else:
    print(f"\nGame over! The number was {secret}.\n")

print("Thanks for playing!")



# In[ ]:




