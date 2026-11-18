#!/usr/bin/env python
# coding: utf-8

# In[1]:


#  Movie Ticket Counter
age =int(input("enter your age:")) 
if age < 5:
    print("Free")
elif age <= 17:
    print("Your ticket price is Rs. 100")
elif age<=59 :
    print("Your ticket price is Rs. 200")
else:
    print("Your ticket price is Rs. 120")


# In[2]:


# Electricity Bill Calculator

units = int(input("Enter units consumed: "))
bill = 0

while units > 0:
    if units > 200:
        bill = bill + (units - 200) * 8
        units = 200
    else:
        if units > 100:
            bill = bill + (units - 100) * 5
            units = 100
        else:
            bill = bill + (units * 3)
            units = 0

print("Total bill: Rs.", bill)


# In[3]:


# Multiplication Table for a Kid

n = int(input())
i = 1
while i<=10:
    print(n*i)
    i=i+1
 
    
    



# In[4]:


# Savings Piggy Bank

savings = 0
n=0
while savings < 1000:
    t_savings = int(input('enter your savings:'))
    savings= savings+t_savings
    n=n+1
    
print(f"Goal reached in {n} days! Total saved: Rs. {savings}")
    


# In[1]:


# ATM PIN Check
a =3
Pin = 4321
while a>0:
    N_pin = int(input("Enter pin:"))
    if N_pin == Pin:
        print('Access Granted')
        break
    else:
        print("wrong pin")
        a= a-1
if a==0:
    print("card blocked")


# In[6]:


# Even and Odd Counter
n = int(input())
i=1
even = 0
odd = 0
while i<=n:
    if i%2==0:
        even = even+1
        i=i+1
    else :
        odd = odd+1
        i=i+1
print("even count:",even)
print("odd count:",odd)
        


# In[2]:


# secret number

s = 27
n= int(input("guess the number:"))
c=1
while n !=s:
    if n > 27:
        print("too high")
    else:
        print("too low")
    n=int(input("guess the number:"))
    c=c+1
print(f"Correct! You took {c} guesses.")


# In[4]:


# Exam Result with Grade
g = int(input())
if g >= 90:
    print('A')
elif g>=75:
    print('B')
elif g>=74:
    print('C')
elif g>=49:
    print('D')
elif g<35:
    print('FAIL')
else:
    print('Invalid marks')


# In[5]:


# Sum of Digits on a Bill Number

bill = int(input("Enter bill number: "))
original_bill = bill  
s = 0
while bill > 0:
    d = bill % 10
    s = s + d
    bill = bill // 10

print(f"Sum of digits of {original_bill}: {s}")
if s > 20:
    print("Congratulations! You win a free gift.")
else:
    print("Sorry, no free gift this time.")


# In[10]:


# Staircase Pattern
n= int(input())
for i in range (1,n+1):
    for j in range(i):
        print('*', end=" ")
    print()

