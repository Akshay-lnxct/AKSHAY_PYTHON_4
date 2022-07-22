
#num positive negative or zero

n = int(input("enter the number : "))

if n ==0 :
    print("your num is 0")
elif n>0 :
    print("your num is positive")
elif n<0 :
    print("your num is negative")


print(" * " * 50)


#factorial

n = int(input("enter the number : "))

factorial = 1

if n < 0 :
    print("sorry, factorial does not exist for negative numbers")
elif n==0 :
    print("the factorial of o is 1")
else:
    for i in range(1,n+1):
        factorial = factorial*i
    print("the factorial of " , n , "is" , factorial)

print(" * " * 50)


#fibonacci series


n = int(input("enter the number : "))

a = 0
b = 1

print(a, end=" ")

while b<n:
    print(b,end=" ")
    a,b=b,a+b



print(" * " * 50)



#swaping with variabal

a = 5
b = 6

tem = a
a = b
b = tem

print(a)
print(b)



print(" * " * 50)



#swaping without variable


a = 5
b = 6

a,b = b,a

print(a)
print(b)


print(" * " * 50)


#even odd


n = int(input("enter the number : " ))

if n%2==0:
    print("your number is even")
else:
    print("your number is odd")


print(" * " * 50)



#vowel or not

n = input("enter any latter : ")

if n in ('a','e','i','o','u'):
    print("your latter is vowel")
else:
    print("your latter is consonant")


print(" * " * 50)


#sum of three num

n1 = int(input("enter your 1st number : "))
n2 = int(input("enter your 2nd number : "))
n3 = int(input("enter your 3rd number : "))

n = n1+n2+n3

if (n1==n2 or n1==n3 or n2==n3):
    print("your sum is : 0")
else:
    print("your sum is : " , n )


print(" * " * 50)



#given integervalue difference is 5 and both are same so output is true otherwise false


def test_number(n1,n2):

    if n1==n2 or (n1-n2)==5 or (n1+n2)==5:
        return True
    else:
        return False
n1 = int(input("enter the 1st number : "))
n2 = int(input("enter the 2nd number : "))

print(test_number(n1,n2))


print(" * " * 50)



#sum of first n positive interger

n = int(input("enter the number : "))
sum = (n*(n+1))/2
print("sum of first n num is : " , sum)


print(" * " * 50)



#lenth of sting

n = input("enter anything : ")
print(len(n))

#count a character

print(len(n) - n.count(" "))

#count occurrence of substring

substg = 'axay'

a = n.count(substg)

print("number of occurrence of substring : " ,a)


print(" * " * 50)

#count occurrence of each word

def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word]+=1
        else:
            counts[word]=1

    return counts

n = input(" enter anything : ")

print(word_count(n))



print(" * " * 50)

#separated by space and change first 2 character

n1 = input("enter anything : ")
n2 = input("enter anything : ")

new_n1 = n2[:2] + n1[2:]
new_n2 = n1[:2] + n2[2:]

print(new_n1 + ' ' + new_n2)

print(new_n1)
print(new_n2)


print(" * " * 50)



def add_ly(n):
    length = len(n)

    if length > 2:
        if n[-3:] == 'ing':
            n += 'ly'
        else:
            n += 'ing'
    return n


n = input("enter anything : ")

print(add_ly(n))



print(" * " * 50)

"""

#poor and good



def not_poor(n):

    snot = n.find('not')
    spoor = n.find('poor')

    if spoor > snot and snot > 0 and spoor > 0 :
        n = n.replace(n[snot:(spoor+4)], 'good')
        return n
    else:
        return n

n = input("enter anything : ")

print(not_poor(n))


"""0


print(" * " * 50)

#get first two or last two char sum


n = input("enter anything : ")

a = len(n)

if a < 2 :
    print(n)
else:
    print(n[:2] + n[-2:])"""






