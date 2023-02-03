'''#calculating product price for 5 units
old={'rice':60,'dhal':120,'oil':150}
new={product:price*5 for (product,price) in old.items()}
print(new)


#with checks
real={'sam':24,'angel':18,'kumar':35}
now={name:age for (name,age) in real.items() if age>20}
print(now)


#create a list with  8 customer names display a dictinoary which has customer names along with discounts with them from a particular shop
import random
cust=["sathwik","sudharma","pranay"]
cust_dict={names:random.randint(1,100) for names in cust}
print(cust_dict)


#percetage of student in school
a=list(map(str,input("enter the names of the student").split()))
b=list(map(int,input("enter the marks").split()))
cent=[]
for i in range(len(b)):
    n=round((b[i]/500)*100,2)
    cent.append(n)
cent_dict={a:cent for (a,cent) in zip(a,cent)}
print(cent_dict)

#get one string as input along with a character find out and display whether that particular string is present in it or not
s=input("enter the string:")
c=input("enter the char:")
if c in s:
    print(c,"present")
else:
    print(s,"not present")

#check given string is palindrome or not
s=input("enter the string:")
s=s.lower()
if(s==s[::-1]):
    print("the string is palindrome")
else:
    print("the string is not palindrome")

#check one string as input check your contaisn space or not if yes count number of spaces and print 
s=input("enter the string:")
if " " in s:
    print("yes")
else:
    print("no")
a=s.replace(" ","A")
print(s.count(" "))


#neon number
num = int(input("Enter a number \n"))
sqr = num*num
sumOfDigit = 0
while sqr>0:
    sumOfDigit =sumOfDigit + sqr%10
    sqr = sqr//10
if (num == sumOfDigit):
    print("Neon Number")
else:
    print("Not a Neon Number")'''

    
#create a list with vowels get one string as input count vowels from the string and display the result 
str=input("Enter string:")
vowels=0
for i in str:
      if(i=='a'or i=='e'or i=='i'or i=='o'or i=='u'or i=='A'or i=='E'or i=='I'or i=='O' or i=='U'):
            vowels=vowels+1
print("Number of vowels are:")
print(vowels)


