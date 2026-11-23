#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Q1. Phone Contact Book

d={}
while True:
    print("1. Add contact")
    print("2. Search contact")
    print("3. Show all contacts")
    print("4. Exit")
    c = input("Enter choice: ")

    if c == "1":
        n = input("Enter name: ")
        if n in d:
            print("Contact already exists")
        else:
            d[n] = input("Enter phone number: ")
            print("Contact added")
    elif c == "2":
        n = input("Enter name to search: ")
        if n in d:
            print(n, ":", d[n])
        else:
            print("Contact not found")
    elif c == "3":
        for k, v in d.items():
            print(k, ":", v)
    elif c == "4":
        break
    else:
        print("Invalid choice")


# In[4]:


# 2 Unique Visitors on a Website
v = [101, 205, 101, 330, 205, 412, 101, 330, 509]
s = set(v)

print("Total visits:", len(v))
print("Unique visitors:", len(s))
print("Unique visitor IDs:", sorted(s))


# In[5]:


#3 Student Marks Dictionary
m = {"Aman": 82, "Priya": 91, "Rahul": 45, "Sneha": 67, "Kiran": 30}

for k, v in m.items():
    if v >= 40:
        print(k, "Pass")
    else:
        print(k, "Fail")

t = None
for k in m:
    if t is None or m[k] > m[t]:
        t = k
print("Topper:", t, "with", m[t])

p = {}
for k, v in m.items():
    if v >= 40:
        p[k] = v
print("Passed students:", p)


# In[6]:


#4 Common Friends
r = {"Aman", "Neha", "Karan", "Sita", "Vikram"}
a = {"Neha", "Vikram", "Pooja", "Aman", "Rohan"}

print("Mutual friends:", r.intersection(a))
print("Only Riya has:", r.difference(a))
print("All people:", r.union(a))
print("Suggestions for Riya:", a.difference(r))
# Trying to change Mumbai's latitude:
# c[1][1] = 20.0
# Error: TypeError: 'tuple' object does not support item assignment
# Reason: tuples are immutable, so their items cannot be changed after creation.


# In[7]:


#5 Character Counter
s = input("Enter text: ")
d = {}

for x in s:
    if x != " ":
        d[x] = d.get(x, 0) + 1
print(d)

h = None
for k in d:
    if h is None or d[k] > d[h]:
        h = k
print("Most frequent character:", h, "(" + str(d[h]), "times)")


# In[8]:


#6 Restaurant Menu Billing
m = {"dosa": 60, "idli": 40, "vada": 30, "coffee": 25, "tea": 15}
t = 0

while True:
    i = input("What would you like to order? ")
    if i == "bill":
        break
    if i in m:
        t += m[i]
    else:
        print("Item not available")

if t > 200:
    t = t - t * 10 / 100
    print("10% discount applied")
print("Total bill: Rs.", t)


# In[9]:


#7 City Coordinates (Tuples)
c = [("Hyderabad", 17.38, 78.48),
     ("Mumbai", 19.07, 72.87),
     ("Chennai", 13.08, 80.27),
     ("Delhi", 28.61, 77.20)]

for n, la, lo in c:
    print(n, "Latitude:", la, "Longitude:", lo)

f = c[0]
for x in c:
    if x[1] > f[1]:
        f = x
print("Farthest north:", f[0])


# In[1]:


#Q8. Library Book Tracker
b = {"Python Basics": 3, "Data Science 101": 0,
     "Machine Learning": 2, "SQL Guide": 1}

n = input("Enter book name to borrow: ")

if n not in b:
    print("Book not found")
elif b[n] == 0:
    print("Currently unavailable")
else:
    b[n] -= 1
    print("Book issued successfully")

print(b)


# In[2]:


# Q9. Group Employees by Department
e = [("Ravi", "IT"), ("Anjali", "HR"), ("Suresh", "IT"),
     ("Meena", "Finance"), ("Arun", "HR"), ("Divya", "IT")]

d = {}
for n, p in e:
    if p not in d:
        d[p] = []
    d[p].append(n)
print(d)

for k, v in d.items():
    print(k, ":", len(v), "employees")


# In[3]:


# Q10. Quiz Answer Checker
k = ("B", "C", "A", "D", "B")
w = set()
s = 0

for i in range(5):
    a = input("Enter answer for Q" + str(i + 1) + ": ").upper()
    if a == k[i]:
        print("Q" + str(i + 1), "Correct")
        s += 1
    else:
        print("Q" + str(i + 1), "Wrong")
        w.add(i + 1)

print("Wrong questions:", w)
print("Score:", s, "/ 5")

if s == 5:
    print("Excellent")
elif s >= 3:
    print("Good")
else:
    print("Needs improvement")

