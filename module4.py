import re

pattern = r"^axay"
string = "axay"

x = re.match(pattern , string)
print(x)




import re
txt = "i am very happy "
x = re.search("\s" , txt)
print("the first white space :  " , x.start())


import re
txt = "today is firday"
x = re.search("monday" , txt)
print(x)

import re

str1 = "i am very happy today"
print("before replace : " , str1)

result = re.sub(r"very" , "not" , str1)
print("after replace : " , result)


import re

str1 = "Hello Good Morning Dosto"
print("before replace : " , str1)

result = re.sub(r"[a-z]" , "0" , str1)
print("after replace : " , result)




