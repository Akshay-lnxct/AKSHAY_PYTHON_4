from numpy import*

arr = array([1,2,3,4,5],int)

print(arr.dtype)
print(arr)


print(" * " * 114)


arr = array([1,2,3,4,5.0])

print(arr.dtype)
print(arr)


print(" * " * 114)


arr = array([1,2,3,4,5],float)

print(arr.dtype)
print(arr)


print(" * " * 114)


arr = linspace(0,15,20)

print(arr)


print(" * " * 114)


arr = linspace(0,15)

print(arr)


print(" * " * 114)


arr = arange(1,15,2)

print(arr)

print(" * " * 114)


arr = logspace(1,40,5)

print(arr)
print('%.2f' %arr[0])


print(" * " * 114)


arr = zeros(5)

print(arr)


print(" * " * 114)


arr = ones(5)

print(arr)


print(" * " * 114)


arr = ones(5,int)

print(arr)


