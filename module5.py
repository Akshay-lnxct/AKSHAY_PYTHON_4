file = open("axay.txt" , "w")
file.write("this is a very beautyful garden")
file.close()
print("file succesfully save")

print("*" * 50)


file = open("axay.txt " , "r")
print(file.read())
file.close()
print("file read succesfully")


print("*" * 50)



file = open("axay.txt" , "a")
file.write("\n this is append file ")
file.close()
print("file append successfully")