#!/usr/bin/env python
# coding: utf-8

# In[13]:


print("AI Password Strength Checker Lite")
attempts=5
while attempts!=0:
    password=input("Enter your password:")
    if len(password)<8:
        print("Must be at least 8 characters!")
    else:
        has_digit=False
        has_capital=False
    for char in password:
        if char >= "0" and char <= "9":
            has_digit=True
    for char in password:
        if char >= "A" and char <= "Z":
            has_capital=True
    length=len(password)>=8
    if length and has_digit  and has_capital:
        print("You created a strong password!AI Training Level: Beginner → Intermediate")
        break
    elif length or has_digit  or has_capital:
        print(f"Weak password.Try again you have {attempts-1} attempts left")
        attempts-=1
    elif length and has_digit or has_capital and length or has_digit and has_capital:
        print(f"Moderate password. Try again to make it strong,you have{attempts-1} attempts left")
        attempts-=1
    if attempts==0:
        print("Final Result: Password is not strong enough.")
     
        
            
    


# In[ ]:




