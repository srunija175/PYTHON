#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Q1. Class Marks Report

marks = [78, 45, 92, 33, 67, 88, 51, 29]
p = 0
for i in marks:
    if i>=35:
        p += 1
print("Highest marks:", max(marks))
print("Lowest marks:", min(marks))
print("Class average:", sum(marks) / len(marks))
print("Students passed:", p)


# In[2]:


# Q2. Grocery Shopping List

shopping_list = []

while True:
    item = input("Enter item: ")
    if item == "done":
        break
    if item in shopping_list:
        print("Already added")
    else:
        shopping_list.append(item)

for i in range(len(shopping_list)):
    print(str(i + 1) + ". " + shopping_list[i])
print("Total items:", len(shopping_list))


# In[3]:


#Q3. Username Validator
u = input("Enter username: ")

if len(u) < 5 or len(u) > 12:
    print("Invalid: Username must be between 5 and 12 characters")
elif " " in u:
    print("Invalid: Username cannot contain spaces")
elif u[0].isdigit():
    print("Invalid: Username cannot start with a digit")
else:
    print("Valid username")


# In[4]:


#Q4. Vowel Counter for a Tweet

s = input("Enter a sentence: ")
v = 0
c = 0
b = 0

for x in s.lower():
    if x == " ":
        b += 1
    elif x in "aeiou":
        v += 1
    elif x.isalpha():
        c += 1

print("Vowels:", v)
print("Consonants:", c)
print("Spaces:", b)


# In[5]:


# Q5. Palindrome Name Checker

n = input("Enter your name: ")
s = n.lower()

f = True
for i in range(len(s) // 2):
    if s[i] != s[len(s) - 1 - i]:
        f = False
        break
if f:
    print("Bonus! Your name is a palindrome.")
else:
    print("Not a palindrome. No bonus.")


# In[6]:


#Q6. Temperature Tracker
t = [32, 35, 38, 41, 36, 29, 40]
d = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

print("Heat alert days (above 37):")
for i in range(len(t)):
    if t[i] > 37:
        print(d[i], t[i])

h = 0
for i in range(len(t)):
    if t[i] > t[h]:
        h = i
print("Hottest day:", d[h], "with", t[h], "C")

f = []
for x in t:
    f.append(x * 9 / 5 + 32)
print("Temperatures in Fahrenheit:", f)


# In[7]:


# Q7. Word Frequency in a Sentence

s = input("Enter a sentence: ")
w = s.split()
l = w[0]
sh = w[0]
c = 0
for x in w:
    if len(x) > len(l):
        l = x
    if len(x) < len(sh):
        sh = x
    if x[0].isupper():
        c += 1
print("Longest word:", l)
print("Shortest word:", sh)
print("Words starting with capital letter:", c)


# In[8]:


# Q8. Remove Negative Balances

b = [1500, -200, 3000, -50, 0, 750, -1000]
p = []
n = []
o = 0
for x in b:
    if x > 0:
        p.append(x)
    elif x < 0:
        n.append(x)
        o += -x
print("Positive accounts:", p)
print("Negative accounts:", n)
print("Total amount owed:", o)


# In[9]:


#Q9. Password Strength Checker

p = input("Enter password: ")

u = False
l = False
d = False
k = len(p) >= 8

for x in p:
    if x.isupper():
        u = True
    elif x.islower():
        l = True
    elif x.isdigit():
        d = True

c = 0
for x in [u, l, d, k]:
    if x:
        c += 1

if c == 4:
    print("Strong")
elif c >= 2:
    print("Medium")
else:
    print("Weak")


# In[1]:


#Q10. Simple Name Initials Generator

n = input("Enter full name: ")
w = n.split()

i = ""
for x in w:
    i += x[0].upper() + "."
print(i)

print(n.title())

s = ""
for j in range(len(w) - 1):
    s += w[j][0].upper() + ". "
s += w[-1].title()
print(s)

