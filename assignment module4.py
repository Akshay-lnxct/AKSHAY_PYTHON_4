
# read an entire text file

def file_read(fname):
    txt = open(fname)
    print(txt.read())

file_read('test.txt')

#append text to a file & display the text

def file_read(fname):
    from itertools import islice
    with open (fname,"w") as myfile:
        myfile.write("python exercises\n")
        myfile.write("java exercises")
    txt = open(fname)
    print(txt.read())

file_read('ab.txt')

#read first n line

n = input("enter the lines")
f = open("file.txt","r")
for i in range(n):
    print(f.readline())

#read last n line

def read_lastnlines(fname,n):
    with open('file1.txt')as f:
        for line in (f.readlines()[-n:]):
            print(line)

read_lastnlines('file1.txt',3)


#read a file line by line and store in into list

with open("data_file.txt") as f:
    content_list = f.readlines()

ab = [x.strip() for x in content_list]
print(ab)


#read a file line by line and store in into variable

f = open("file.txt","r")
str = ""
for i  in range(0,100):
    str = str+f.read(i)
print(str)

#longest word

def longest_word(filename):
    with open(filename,'r') as infile:
        words = infile.read().split()
    max_len = len(max(words,key=len))
    return [word for word in words if len(word)==max_len]

print(longest_words('about.txt'))


#count the number flines in text file

with open(r"myfile.txt","r") as f:
    lines = len(f.readlines())
    print("total number of lines : " ,lines)


#count the frequence of word in file

from collection import counter

def world_count(fname):
    with open(fname) as f:
        return counter(f.read().split())
print("number of words in the file : ",world_count("text.txt"))

#write a list to a file


color = ['red', 'green', 'white', 'black']
with open('abc.txt',"w") as myfile:
    for c in color:
        myfile.write("%\n" %c)

content = open('abc.txt')
print(content.read())

#copy the contents of file to another file

with open("test.txt") as f:
    with open("out.txt") as f1:
        for line in f:
            f1.write(line)

#try & except & finally

try:
    a = int(input("please enter the firdt number : "))
    b = int(input("please enter the second number :"))
    c = a/b
    print("{} / {} = {}".formate(a,b,c))
except ZeroDivisionError:
    print("division by zero is not possible")
finally:
    print("end of the program")



#enter only odd num else raise exception

try:

    n = int(input("enter the number :"))
    if n%2!=0:
        print(n)
except Exception as e:
    print("Exception Caughtc: ",e)

#rectangle area

class Rectangular():
    def __init__(self,l,w):
        self.length = l
        self.width = w

    def rectanular_area(self):
        return self.length*self.width

newrectangular = Rectangular(12,10)
print(newrectangular.rectanular_area())



#circle area & perimeter

class Circle():
    def __init__(self,r):
        self.radius = r
    def area(self):
        return self.radius**2*3.14
    def perimeter(self):
        return 2*self.radius*3.14

newcircle = Circle(5)
print(newcircle.area())
print(newcircle.perimeter())


#inharitance example

class RBI:
    def Interest(self):
        pass

class SBI(RBI):
    def Interest(self):
        print("SBI Interest is 5%")

class HDFC(RBI):
    def Interest(self):
        print("HDFC Interest is 2%")

s = SBI()
s.Interest()


b = HDFC()
b.Interest()


class Animal:
    def move(self):
        pass

class Dog(Animal):
    def move(self):
        print("I CAN BARK")

class Snake(Animal):
    def move(self):
        print("I CAN HISSS")

A = Dog()
A.move()


B = Snake()
B.move()