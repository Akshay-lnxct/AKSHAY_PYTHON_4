from array import*

vals = array('i' , [1,5,4,5,56,78,34])

vals.reverse()
print(vals)

print(" * " *114)

print(vals.buffer_info())

print(vals.typecode)

print(" * " *114)

for i in range(5):
    print(vals[i])

for e in vals:
    print(e)

print(" * " *114)


vals = array('u' ,['a' , 'b' ,'c'])

for e in vals:
    print(e)

print(" * " *114)


vals = array('i' , [1,5,4,5,56,78,34])

newArr = array(vals.typecode, (a*a for a in vals))

for e in newArr:
    print(e)

print(" * " * 114)

arr = array('i' , [])

n = int(input("enter the length of array :"))

for i in range(n):
    x = int(input("enter the next value"))
    arr.append(x)

print(arr)

val = int(input("enter the value for search :"))

k = 0

for e in arr:
    if e==val:
        print(k)
        break
    k+=1

print(arr.index(val))

