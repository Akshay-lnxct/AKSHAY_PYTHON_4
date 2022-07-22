
#count a string

list = []

count = 0

for i in range(5):
    i = str(input("enter anything : "))
    list.append(i)

for i in list:
    if len(i) > 2 and i[0] == i[-1]:
        count += 1
    else:
        count

print(list)
print("your result is : " , count)



print(" * " * 50)


#remove duplicate from list


a = [1,2,3,4,5,1,2,3]

x = list(set(a))
print(x)


print(" * " * 50)


#check list is empty or not

list = []

if list[0:] == []:
    print("your list is empty ")
else:
    print(list)


print(" * " * 50)



#first 5 and last 5 value square

n = list()

for i in range(1,31):
    n.append(i**2)


x = n[:5]
y = n[-5:]

print(x+y)


print(" * " * 50)


#list to str


a = ['a','b','c']

str = ''.join(a)

print(str)



print(" * " * 50)



#random choice from list

import random

n = ['axay', 'mitanshu', 'henil', 'vasu', 'jaydev']

print(random.choice(n))



print(" * " * 50)



#second smallest num in list


li = []

n = int(input(" enter the number : "))

for i in range(1,n+1):
    a = int(input(" enter the number : "))
    li.append(a)

li.sort()

print("sorted list : " ,li)
print("the second smallest number in list : " , li[1])



print(" * " * 50)


#unique value from list

a = [10,20,30,10,40,50,20,60]
b = list(set(a))

print("unique value from list : " ,b)



print(" * " * 50)



#list contains a sub list


list = [1,2,3,4,5]
sublist = [2,4]

print("original list : " + str(list))
print("original sublist : " + str(sublist))

flag = 0

if (all(x in list for x in sublist)):
    flag = 1

if(flag):
    print("yes list is a sublist of other.")
else:
    print("no. list is not sublist of other.")



print(" * " * 50)




#split list into variable

list = [('sun' , 'mon' , 'tue') , ('abc' , 'def' , 'hij') , ('aaa' , 'bbb' , 'ccc')]
var1, var2, var3 = list
print(var1)
print(var2)
print(var3)

print(" * " * 50)



#creat a tuple with different data type

tuple = ('mitanshu' , 12 , 12.45 , False)
print(tuple)


print(" * " * 50)


#creat a tuple with number


n = 1,2,3,5
print(tuple(n))

print(" * " * 50)



#convert tuple to sring

n = ('a','x','a','y')
str = ''.join(n)
print(str)


print(" * " * 50)


#check whether an element exists within a tuple

tuple = ('a' , 'b' , 'c' , 12 ,15)
print('a' in tuple)
print(10 in tuple)


print(" * " * 50)



#length of tuple

n = (12,23,34,45,56)
print(len(n))


print(" * " * 50)


#convert list to tuple

n = [1,2,3,4]
print(n)
tuple = tuple(n)
print(tuple)



print(" * " * 50)



#reverse tuple


n = (110,20,30,40,50)
m = reversed(n)
print(tuple(m))


print(" * " * 50)


#replace last value of tuple in list


l = [(10,20,30) , (40,50,60) , (70,80,90)]
print([t[:-1] + (100,) for t in l ])


print(" * " * 50)


#find a repeated iteam in tuple

n = (1,2,3,4,5,2,6,2,7,2,8,2)
print(n)
count = n.count(2)
print(count)

print(" * " * 50)


#remove empty tuple of list


n = [(1,2,3) ,() , (34,4,56), (234,45)]
x = n.remove(())
print(n)

       #or

n = [t for t in n if t]
print(n)


print(" * " * 50)


#unzip a list of tuple into individual list

l = [(1,2) ,(3,4) ,(8,9)]
print(list(zip(*l)))


print(" * " * 50)

#convert list of tuple into dictonary


tup = [("mitu", 10), ("vasu", 12), ("henil" ,15), ("mitanshu",20)]
dictonary = {}
dictonary = dict(tup)
print(dictonary)


   #or

n = [("x",1), ("x",2),("x",3),("y",1),("y",2),("z",1)]
d = {}
for a , b in n :
    d.setdefault(a, []).append(b)
print(d)



print(" * " * 50)




#ascending descending dict value


import operator

d = {1:2, 3:4, 4:3, 2:1, 0:0}

print("original dictionary : " , d)

sorted_d = sorted(d.items(), key=operator.itemgetter(1))
print("dictonary in ascending order : " , sorted_d)

sorted_d = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))
print("dictonary in descending order : " , sorted_d)



print(" * " * 50)




#check multiple key exists into dic

student = {
          'name' : 'mitanshu',
          'class ' : 'v',
          'roll no': '1'
}
print(student.keys() >= {'class' ,'name'})
print(student.keys() >= {'name' ,'mitanshu'})
print(student.keys() >= {'roll no' ,'name'})


print(" * " *

#merge teo dict


d1 = {'a':100, 'b':200 }
d2 = {'c':300, 'd':400}

d1.update(d2)

print(d1)

print(" * " * 50)


#two list into dict

list1 = ['axay','mitanshu','henil']
list2 = ['mech','ele','it']

d = dict(zip(list1,list2))
print(d)

print(" * " * 50)


#sem key adding two dict

d1 = {'a':100, 'b':200, 'c':300}
d2 = {'a':200, 'b':100, 'd':500}

d = dict(d1)

d.update(d2)

for i,j in d1.items():

    for x,y in d2.items():

        if i==x:
            d[i] =(j+y)

print(d)


print(" * " * 50)


#unique value in dic

a = [{'axay':'mech', 'mitanshu':'ele', 'vasu':'mech', 'jaydev':'chem', 'uttam':'mech'}]
print("original list : " , a)
k = set(val for dic in a for val in dic.values())
print("unique values : " ,k)


print(" * " * 50)


#combination of latter

import itertools
d = {'1':['a','b'], '2':['c','d']}
for combo in itertools.product(*[d[k] for k in sorted(d.keys())]):
    print(''.join(combo))



print(" * " * 50)


#three largest value in dict

from collections import Counter

my_dict = { 'A': 67, 'B': 23, 'C':45,
            'D':56, 'E':12, 'F':69}

k = Counter(my_dict)

high = k.most_common(3)

print("dictonary with 3 highest values: ")
print("key : value")

for i in high:
    print(i[0], " :" ,i[1], " ")



print(" * " * 50)


#combine a values in python list of dictonary


from collections import Counter

item_list = [{'item':'item1', 'amount':400}, {'item':'item2', 'amount':300}, {'item':'item1', 'amount':750}]
result = Counter()
for d in item_list:
    result[d['item']] += d['amount']
print(result)



print(" * " * 50)



#create a dictonary from string


from collections import defaultdict, Counter

string = 'w3resource'

dic = {}

for i in string:
    dic[i] = dic.get(i, 0) + 1
print(dic)


print(" * " * 50)


#python function to calculate factorial

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
n = int(input("enter the number : "))
print(factorial(n))


print(" * " * 50)


#python function to check whether a num is givien range

def test_range(n):
    if n in range(1,6):
        print(f"num {n} is the givien range")
    else:
        print("num is not in range")

test_range(5)


print(" * " * 50)


#num is perfect or not check by python function

def perfect_number(n):
    sum = 0
    for i in range(1,n):
        if n%i ==0:
            sum += i
    return sum == n
print(perfect_number(6))


print(" * " * 50)


#check string is palindrome or not


def isPalindrome(string):
    Left_pos = 0
    Right_pos = len(string)-1

    while Right_pos >= Left_pos:
        if not string[Left_pos] == string[Right_pos]:
            return False
        Left_pos += 1
        Right_pos -= 1
    return True
print(isPalindrome('axa'))

print(" * " * 50)


#read random line from file


import random
def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)
print(random_line('text.txt'))


print(" * " * 50)


#convert degree to radian


pi =22/7

degree = float(input("enter the degrees : "))
radian = degree*(pi/180)
print(radian)

print(" * " * 50)


#area of trapezoid

height = float(input("height of trapezoid : "))
base_1 = float(input("enter the one base : "))
base_2 = float(input("enter the second base : "))

area = ((base_1 + base_2)/2) * height
print("area is : " , area)


print(" * " * 50)


#area of parallelogram

base = float(input("enter the length of base : "))
height = float(input("enter the height : "))
area = base * height
print("area is : " , area)

print(" * " * 50)

#surface volume and area of cylinder

pi =22/7
height = float(input("enter the height of cylinder : "))
radian = float(input("enter the radius of cylinder : "))
volume = pi * radian * radian * height
surface_area = ((2*pi*radian)*height) + ((pi*radian**2)*2)
print("volum of cylinder is : " , volume)
print("surface area of cylinder is : " ,surface_area)


print(" * " * 50)


#return sum of all divisors of a num

def sum_div(number):
    divisiors = [1]
    for i in range(2,number):
        if (number % i)==0:
            divisiors.append(i)
    return sum(divisiors)
print(sum_div(10))



print(" * " * 50)


#find the min and max num from decimal num


from decimal import*
data = list(map(Decimal, '2.45 4.76 1.7 5.76 3.6 2.00 0.04'.split()))
print("maximum : " , max(data))
print("minimum : " , min(data))

