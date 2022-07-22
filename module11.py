n = int(input("enter your num : "))

for i in range(n+1):
    print(" *" * i)


print("*" * 50)

n = int(input("enter your num : "))

for i in range(n,0,-1):
    print(" *" * i)

print("*" * 50)


n = int(input("enter your num :"))

for i in range(n+1):
    for j in range(i):
        print(i , end=" ")
    print()

print("*" * 50)



n = int(input("enter your num : 6"))

for i in range(n+1):
    for j in range(i+1):
        print((i+1), end=" ")
    print()

print("*" * 50)

n = int(input("enter rows number you needed : \n"))
for i in range(n):
    for k in range (n-i-1):
        print(" " , end=" ")
    for j in range(i, -1 ,-1):
        print(n-j , end=" ")
    print()

print("*" * 50)




