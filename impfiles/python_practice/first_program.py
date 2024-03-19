'''
print("python")
a="infy"
b=20.127
c=10
print(a,b,c)
print(a,b,c,sep=":")
print(a,b,c,end=" ")
print(a,b,c)
print("b=%0.2f" %b)
print("c=%8d" %c)
print("c=%-8d" %c)
#find leap year
i=int(input("enter year to check leap year or not\n"))
if(i%4==0 and i%400==0):
    print("its a leap year")
else:
    print("it's not a leap year")
#find greatest of three numbers
x=10
y,z=20,30
if(x>y and y>z):
    print("x is greater")
elif(y>z and y>x):
    print("y is grater")
else:
    print("z is greater")
#find number is prime or not
n=int(input())
c=0
if(n>2 and n%2==0):
    print("its not prime number")
else:
    
    for i in range(1,n+1):
        if(n%i==0):
            if(c>2):
                break
            else:
                c+=1
    if(c>2):
        print("its a  not prime number")
    else:
        print("its a prime number")   
#fibinoci series
a,b=0,1
c=b
count=2
print("0 1")
n=int(input())
while(c<=n):
    print(c,sep=",")
    #count+=1 if want the no of elements use count<n
    a,b=b,c
    c=a+b

#sum of digits of number
n=int(input())
sum1=0
while(n>0):
    print(n%10,n//10)
    sum1=sum1+(n%10)
    n=n//10
print(sum1)
#reverse of a number
n=int(input())
rev=0
x=n
while(x>0):
    print(x%10,x//10,rev)
    rev=rev*10+(x%10)
    x=x//10
if(rev==n):
    print("number is panlindrome")
else:
    print("number is not a palindrome") 

#functions
def find_square(x):
    return x*x
n=int(input())
print(find_square(n))

def find_sum(x):
    sum=0
    for i in range(x):
        sum+=i
    return sum
print(find_sum(n))

x=formal argument and n= actual agrument
pass by value : n=10 
pass by reference : n=[20] passing addres with it it will
                    be refelect after the funtional call also.
                    

def change_number(num):
    num+=10
def change_list(num_list):
    num_list.append(20)
num_val=10
print("*********effect of pass by value*********")
print("num_val before function call:", num_val)
change_number(num_val)
print("num_val after function call:", num_val)
print("-----------------------------------------------")
val_list=[5,10,15]
print("*********effect of pass by reference*********")
print("val_list before function call:", val_list)
change_list(val_list)
print("val_list after function call:", val_list)

#factorial;
def factorail(a):
    if(a==1 or a==2):
        return a
    else:
        return a*factorail(a-1)
n=int(input())
print(factorail(n))

#palindrome or not
def is_palindrome(num):
    sum1=0
    while(num>0):
        sum1=sum1*10+(num%10)
        num=num//10
    return sum1
n=int(input())
if(n==is_palindrome(n)):
    print("it is a palindrome")
else:
    print("it is not a palindrome")
 
#amicable_numbers(sum of proper divisors)
def check_amicable_numbers(num1, num2):
    sum1,sum2=0,0
    for i in range(1,num1):
        if(num1%i==0):
            sum1=sum1+i
    for i in range(1,num2):
        if(num2%i==0):
            sum2=sum2+i
    if(sum2==num1 and sum1==num2):
        print("nums are amicable number")
    else:
        print("nums are not amicable number")


n1=int(input())
n2=int(input())
check_amicable_numbers(n1,n2)

right shit operator for moving byes to right
print(60>>2)

#strong number :A number is said to be strong number, 
def check_strong_number(num):
    def factorial(x):
        if(x==1 or x==0):
            return 1
        else:
            return x*factorial(x-1)
    sum1=0
    while(num>0):
        sum1=sum1+factorial(num%10)
        num=num//10
    return sum1
n=int(input())
print(check_strong_number(n))

#List
sample_list1=["Mark",5,"Jack",9, "Chan",5]
s=[]
s1=list()
x=[None]*5
print(s,s1,len(s),len(x),x)

Random access of elements:
print(sample_list[2])

Random write
sample_list[2]=“James”

Other operations:
Adding an element to the end of the list
sample_list.append("James")


Concatenating two lists
new_list=["Henry","Tim"] 
sample_list+=new_list
sample_list=sample_list+new_list

sample_list+=new_list, concatenates new_list to sample_list

sample_list=sample_list+new_list, creates a new list named sample_list
containing the concatenated elements from the original s
ample_list and new_list


#Given a list of integer values, write a Python program to check whether
#the list contains the same number in adjacent positions.
#Display the count of such adjacent occurrences.
l1=[1,1,5,100,-20,-20,6,0,0]
l2=[10,20,30,40,30,20]
l=[1,2,2,3,4,4,4,10]
count=0
for i in range(len(l)-1):
    if(l[i]==l[i+1]):
        count+=1
print(count)


#Write a Python program to generate the ticket numbers for specified number of passengers traveling in a flight as per the details mentioned below:
The ticket number should be generated as airline:src:dest:number where,

Consider AL1 as the value for airline

src and dest should be the first three characters of the source and destination cities.

number should be auto-generated starting from 101

The program should return the list of ticket numbers of last five passengers.
Note: If passenger count is less than 5, then return the list
of all generated ticket
numbers.

def generate_ticket_number(passenger_count,airline="AL1",source="src",
                           destination="dest"):
    ticket_generate=[]
    for i in range(1,passenger_count+1):
        number=100+i
        t=f"{airline}:{destination[:3]}:{source[:3]}:{number}"
        ticket_generate.append(t)
    return ticket_generate[-5:] if passenger_count>5 else ticket_generate
        
passenger_count=int(input())
print(generate_ticket_number(passenger_count))

#Dictionary
crew_details={ "Pilot":"Kumar",
"Co-pilot":"Raghav",
"Head-Strewardess":"Malini",
"Stewardess":"Mala" }
print(crew_details["Pilot"])
for key,value in crew_details.items():
     print(key,":",value)
print(crew_details.keys())
print(crew_details.values())


#proper divisior using list
def proper_divisiors(x):
    l=[]
    for i in range(1,x):
        if x%i==0:
            l.append(i)
    return l
n=int(input())
print(proper_divisiors(n))


#FIBINOCI SERIES USING LIST
def generate_fibseries(x):
    l=[0,1]
    count=0
    for i in range(0,n):
        if(count==n):
            break
        else:
            count+=1
            l.append(l[i]+l[i+1])
    return l

n=int(input())
print(generate_fibseries(n))

#next 15 leap years from a given year
def next_15_leapyears(x):
    l=[]
    if(x%400==0 and x%4==0):
        l.append(x)
        for i in range(0,14):
            l.append(l[i]+4)
        return l
    else:
        for i in range(1,4):
            x=x+1
            print(x)
            if(x%4==0):
                print(x)
                l.append(x)
                for i in range(0,14):
                    l.append(l[i]+4)
        return l
                
n=int(input())
print(next_15_leapyears(n))

#run length encode
#ex: message=AAAABBBBCCCCCCCC  output: 4A4B8C
def encode(mes):
    t=mes[0]
    count=1
    res=""
    for i in range(1,len(mes)):
        if(mes[i]==t):
            count+=1
        else:
            res=res+str(count)+t
            count=1
            t=mes[i]
    return res+str(count)+t
        
m=input()
print(m.count('a'))
print(encode(m))
d ={"merry":"god","christmas":"jul", "and":"och",
 "happy":"gott", "new":"nytt", "year":"ar"}
l=[]
for i in d.keys():
    l.append(i)
print(l)

#next palindrome
def getNextPalindrome(N):
    return N
    
def isPalindrome(N):
    x=N
    rev=0
    while(x>0):
        rev=rev*10+(x%10)
        x=x//10
    if(N==rev):
        return True
    else:
        return False
  
        


N = int(input())
while(True):
    if(isPalindrome(N)):
        result = getNextPalindrome(N)
        break
    N=N+1
print(result)
    
#wordcount, words,no of characters
s="i love my country india"
x=s.split()

print(type(x),x,len(x),len(s))

 #lines count

with open(r"first_program.py", 'r') as fp:
    l=fp.readlines()
    #print(l)
    lines = len(l)
    for i in l:
        if(i.__contains__('a')):
            print(i)
    print('Total Number of lines:', lines)

fhr=open("first_program.py","rb+")
print("file name:",fhr.name)
print("access mode:",fhr.mode)
print("closed?",fhr.closed)
fhr.close()
print("after closing the file closed?",fhr.closed)

fhr=open("data.txt","r")
data =fhr.read()
print("Before writing:")
print(data)
fhr.close()
fhw=open("data.txt","w")
num=fhw.write("this new first line written\n")
num1=fhw.write("this new second line written\n")
print("num:",num)
print("num1:",num1)
fhw.close()
fhr=open("data.txt","r")
data =fhr.read()
print("After writing:")
print(data)
fhr.close()


fhr=open("data.txt","r")
data =fhr.read()
print("Before writing:")
print(data)
fhr.close()
fhw=open("data.txt","a")
num=fhw.write("this new first line written\n")
num1=fhw.write("this new second line written\n")
print("num:",num)
print("num1:",num1)
fhw.close()
fhr=open("data.txt","r")
data =fhr.read()
print("After writing:")
print(data)
fhr.close()
#current position cursor tell()
fhr=open("data.txt","r")
cur_pos=fhr.tell()
print(cur_pos)
data =fhr.readline()
print(data)
cur_pos=fhr.tell()
print(cur_pos)
data =fhr.readline()
print(data)
fhr.close()

#seek

Python provides seek() function to navigate the file object pointer to the required position specified.

Syntax:

file_object.seek(offset,[whence])

where,

file_object indicates the file object pointer to be navigated

offset indicates which position the file object pointer is to be navigated

if offset is,

positive navigation is done in forward direction
negative navigation is done in backward direction
whence represent reference point for navigating the file object pointer. whence is optional, if not specified default value is 0.

If whence value is

0, navigation will take the reference of beginning of file (absolute positioning)
1, navigation will take the reference of current position (relative positioning) of the file object pointer
2, navigation will take the reference of end of file (relative positioning)
Note:  If you are working with is a text file, then the access mode
        of the should be ‘rb+’ (which opens a file for reading and
writing in binary format) otherwise relative positioning will misbehave.

fhr=open("data.txt","rb+")
print(fhr.tell())
fhr.seek(12) #navigates to 12th position from beginning of the file
print(fhr.tell())
fhr.seek(3,1) #navigates to 3rd position from current position of the file object position
print(fhr.tell())
fhr.seek(-3,2)#navigates to 3rd position from end of the file in backward direction
print(fhr.tell())
fhr.close()


class Mobile:
    def __init__(self, brand, price):
        print("Inside constructor")
        self.brand = brand
        self.price = price

##mob1=Mobile("Apple", 20000)
##print("Mobile 1 has brand", mob1.brand, "and price", mob1.price)
del p1
##mob2=Mobile("Samsung",3000)
##print("Mobile 2 has brand", mob2.brand, "and price", mob2.price)

class Mobile:
    def __init__(self,price,brand):
        print("Price:",price)
        print("Brand:",brand)
#Uncomment each line below. Try it out and observe the output.
#mob1=Mobile()
#mob1=Mobile(10000,'Samsung','Android')
#mob1=Mobile(10000,'Samsung')

class Mobile:
    def __init__(self):
        print("Inside constructor")
    def purchase (self):
        print("Purchasing a mobile")
mob1=Mobile()
mob1.purchase() #Inbound method invocation, We need not pass the value for self.
Mobile.purchase(mob1) #Outbound method invocation, We have to pass the object as the value of self.

class Customer:
    def __init__(self, cust_id, name, age, wallet_balance):
        self.cust_id = cust_id
        self.name = name
        self.age = age
        self.__wallet_balance = wallet_balance
    def update_balance(self,amount):
        if amount < 1000 and amount > 0:
            self.__wallet_balance += amount
    def show_balance(self):
        print("The balance is ",self.__wallet_balance)
c1=Customer(100, "Gopal", 24, 1000)
c1.__wallet_balance = 10000000000
c1.show_balance()

class Mobile:
    __discount = 50
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand
    def purchase(self):
        total = self.price - self.price * Mobile.__discount / 100
        print (self.brand, "mobile with price", self.price, "is available after discount at", total)
    @classmethod
    def enable_discount(cls):
        cls.set_discount(50)
    @classmethod
    def disable_discount(cls):
        cls.set_discount(0)
    @classmethod
    def get_discount(cls):
        return cls.__discount
    @classmethod
    def set_discount(cls, discount):
        cls.__discount = discount
    @staticmethod
    def calculate_tax(cust_type):
        if(cust_type=='member'):
            return 10
        else:
            return 20
        
print('Tax percent to be paid by members:',Mobile.calculate_tax('member'))
print('Tax percent to be paid by non-members:',Mobile.calculate_tax('non-member'))
mob1=Mobile(20000, "Apple")
mob2=Mobile(30000, "Apple")
mob3=Mobile(5000, "Samsung")
Mobile.disable_discount()
mob1.purchase()
Mobile.enable_discount()
mob2.purchase()
Mobile.disable_discount()
mob3.purchase()

#aggregation
class Customer:
    def __init__(self, name, age, phone_no, address):
        self.name = name
        self.age = age
        self.phone_no = phone_no
        self.address = address
    def view_details(self):
        print (self.name, self.age, self.phone_no)
        print (self.address.get_door_no(), self.address.get_street(), self.address.get_pincode())
class Address:
    def __init__(self, door_no, street, pincode):
        self.__door_no = door_no
        self.__street = street
        self.__pincode = pincode
    def get_door_no(self):
        return self.__door_no
    def get_street(self):
        return self.__street
    def get_pincode(self):
        return self.__pincode
    def set_door_no(self, value):
        self.__door_no = value
    def set_street(self, value):
        self.__street = value
    def set_pincode(self, value):
        self.__pincode = value
    def update_address(self):
        pass
add1=Address(123, "5th Lane", 56001)
cus1=Customer("Jack", 24, 1234, add1)
cus1.view_details()

class Phone:
    def __init__(self, price, brand, camera):
        self.price = price
        self.brand = brand
        self.camera = camera
    def buy(self):
        print ("Buying a phone")
    def return_phone(self):
        print ("Returning a phone")
class FeaturePhone(Phone):
    pass
class SmartPhone(Phone):
    pass
FeaturePhone(10000,"Apple","13px").buy()

#constructor inheritance
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera
    def buy(self):
        print ("Buying a phone")
    def return_phone(self):
        print ("Returning a phone")
class FeaturePhone(Phone):
    pass
class SmartPhone(Phone):
    pass
s=SmartPhone(20000, "Apple", 13)
s.buy()
s.return_phone()

#Accessing private attributes of parent class
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera
    def buy(self):
        print ("Buying a phone")
    def return_phone(self):
        print ("Returning a phone")
    def get_price(self):
        return self.__price
    def set_price(self,price):
        self.__price=price
class FeaturePhone(Phone):
    pass
class SmartPhone(Phone):
    def check(self):
        print(self.get_price())
s=SmartPhone(20000, "Apple", 13)
s.check()

#Invoking methods of the parent class
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera
    def buy(self):
        print ("Buying a phone")
    def return_phone(self):
        print ("Returning a phone")
class FeaturePhone(Phone):
    pass
class SmartPhone(Phone):
    pass
s=SmartPhone(20000, "Apple", 13)
s.buy()

#Method Overriding
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera
    def buy(self):
        print ("Buying a phone")
    def return_phone(self):
        print ("Returning a phone")
class FeaturePhone(Phone):
    pass
class SmartPhone(Phone):
    def buy(self):
        print ("Buying a smartphone")
s=SmartPhone(20000, "Apple", 13)
s.buy()

#Using the super() function
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera
    def buy(self):
        print ("Buying a phone")
    def return_phone(self):
        print ("Returning a phone")
class FeaturePhone(Phone):
    pass
class SmartPhone(Phone):
    def buy(self):
        print ("Buying a smartphone")
        super().buy()
s=SmartPhone(20000, "Apple", 13)
s.buy()

#Constructor overriding
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera
    def buy(self):
        print ("Buying a phone")
    def return_phone(self):
        print ("Returning a phone")
class FeaturePhone(Phone):
    pass
class SmartPhone(Phone):
    def __init__(self, os, ram):
        self.os = os
        self.ram = ram
        print ("Inside SmartPhone constructor")
    def buy(self):
        print("Buying a SmartPhone")
s=SmartPhone("Android", 2)
print(s.os)
print(s.brand)

#Using super to access parent class constructor
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera
    def buy(self):
        print ("Buying a phone")
    def return_phone(self):
        print ("Returning a phone")
class FeaturePhone(Phone):
    pass
class SmartPhone(Phone):
    def __init__(self, price, brand, camera, os, ram):
        super().__init__(price, brand, camera)
        self.os = os
        self.ram = ram
        print ("Inside smartphone constructor")
    def buy(self):
        print ("Buying a smartphone")
s=SmartPhone(20000, "Samsung", 12, "Android", 2)
print(s.os)
print(s.brand)

class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera
    def buy(self):
        print ("Buying a phone")
    def return_phone(self):
        print ("Returning a phone")
class SmartPhone(Phone):
    pass
SmartPhone(1000,"Apple","13px").buy()

class Product:
    def review(self):
        print ("Product customer review")
class Phone(Product):
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera
    def buy(self):
        print ("Buying a phone")
    def return_phone(self):
        print ("Returning a phone")
class SmartPhone(Phone):
    pass
s=SmartPhone(20000, "Apple", 12)
s.buy()
s.review()

class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera
    def buy(self):
        print ("Buying a phone")
    def return_phone(self):
        print ("Returning a phone")
class SmartPhone(Phone):
    pass
class FeaturePhone(Phone):
    pass
SmartPhone(1000,"Apple","13px").buy()


class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera
    def buy(self):
        print ("Buying a phone")
    def return_phone(self):
        print ("Returning a phone")
class Product:
    def review(self):
        print ("Customer review")
class SmartPhone(Phone, Product):
    pass
s=SmartPhone(20000, "Apple", 12)
s.buy()
s.review()

#raise exception
class CreditCard:
    def __init__(self, card_no, balance):
        self.card_no = card_no
        self.balance = balance
class Customer:
    def __init__(self,cards):
        self.cards=cards
    def purchase_item(self, price, card_no):
        if price < 0:
            raise Exception()
        if card_no not in self.cards:
            raise Exception()
        if price>self.cards[card_no].balance:
            raise Exception()
card1=CreditCard(101,800)
card2=CreditCard(102,2000)
cards={card1.card_no:card1,card2.card_no:card2}
c=Customer(cards)
while(True):
    card_no=int(input("Please enter a card number"))
    try:
        c.purchase_item(1200,card_no)
        break
    except Exception as e:
        print("Something went wrong. "+str(e))


#custom exception
class InvalidPrice(Exception):
    pass
class WrongCard(Exception):
    pass
class CreditCard:
    def __init__(self, card_no, balance):
        self.card_no=card_no
        self.balance=balance
class Customer:
    def __init__(self,cards):
        self.cards=cards
    def purchase_item(self,price,card_no):
        if price < 0:
            raise InvalidPrice("The price is wrong")
        if card_no not in self.cards:
            raise WrongCard("Card is invalid")
        if price>self.cards[card_no].balance:
            raise WrongCard("Card has insufficient balance")
card1=CreditCard(101,800)
card2=CreditCard(102,2000)
cards={card1.card_no:card1,card2.card_no:card2}
c=Customer(cards)
while(True):
    card_no=int(input("Please enter a card number"))
    try:
        c.purchase_item(1200,card_no)
        break
    except InvalidPrice as e:
        print(str(e))
        break
    except WrongCard as e:
        print(str(e))
        continue
    except Exception as e:
        print("Something went wrong. "+str(e))
#Custom exceptions with constructor overriding
class InvalidUsername(Exception):
    def __init__(self,username):
        msg='The given username '+username+' is invalid'
        super().__init__(msg)
try:
    username='1abc'
    if not username[0].isalpha():
        raise InvalidUsername(username)
except InvalidUsername as e:
    print(e)
-----------------------
    CREATE TABLE Computer (
    id int,
    LastName varchar(255),
    FirstName varchar(255),
    year varchar(4)
);
username=root
password=Lalluk@19

import mysql.connector
#Replace the connection string of your MySQL server
con = mysql.connector.connect(host="localhost",
                              user="root", password="Lalluk@19",
                              database="mydb")
cur = con.cursor()
cur.execute("INSERT INTO Computer VALUES (1005,'Toshiba','Tecra',2013)")
print(cur.rowcount)
cur.close()
#Committing the changes
con.commit()
con.close()

import mysql.connector
#Assume the MySQL server is running on 'localhost', database name is 'mydb' and user is 'root'
con = mysql.connector.connect(host="localhost", user="root", password="Lalluk@19"
                              , database="mydb")
cur = con.cursor()
param = "1005"
cur.execute("DELETE FROM Computer WHERE CompId="+param)
print(cur.rowcount)
cur.close()
con.commit()
con.close()

import mysql.connector 
#Assume the MySQL server is running on 'localhost', database name is 'mydb' and user is 'root'
con = mysql.connector.connect(host="localhost",
                              user="root", password="Lalluk@19",
                              database="mydb")
try:
    cur = con.cursor()
    cur.execute("INSERT INTO Computer_1 VALUES (1006)")
    con.commit()
except mysql.connector.ProgrammingError as e:
    print(e)
finally:
    cur.close()
    con.close()

import mysql.connector 
#Assume the MySQL server is running on 'localhost', database name is 'mydb' and user is 'root'
con = mysql.connector.connect(host="localhost", user="root",
                              password="Lalluk@19", database="mydb")
cur = con.cursor()
cur.execute("SELECT * FROM Computer")
#print(cur.fetchone())
#print(cur.fetchmany())
#print(cur.fetchmany(2))
#print(cur.fetchall())
#for row in cur:
#    print(row)
cur.close()
con.close()

#Fetching individual columns

import mysql.connector 
#Assume the MySQL server is running on 'localhost', database name is 'mydb' and user is 'root'
con = mysql.connector.connect(host="localhost",
                              user="root", password="Lalluk@19",
                              database="mydb")
cur = con.cursor()
cur.execute("SELECT * FROM Computer")
###Fetching the records by iterating through the cursor object
##for row in cur:
##    print(row[0], row[1], row[2], row[3])
#Fetching the records by iterating the cursor object
for column1,column2,column3,column4 in cur:
    print(column1, column2, column3, column4)
cur.close()
con.close()

import mysql.connector 
#Assume the MySQL server is running on 'localhost', database name is 'mydb' and user is 'root'
con = mysql.connector.connect(host="localhost", user="root",
                    password="Lalluk@19", database="mydb")
cur = con.cursor()
cur.execute("SELECT count(id) AS total FROM Computer")
for row in cur:
    print(row[0])
cur.close()
con.close()

#binding parmeters
import mysql.connector
#Assume the MySQL server is running on 'localhost', database name is 'mydb' and user is 'root'
con = mysql.connector.connect(host="localhost", user="root", password="", database="mydb")
cur = con.cursor()
id = 1002
query = "SELECT * FROM Computer WHERE CompId=" + str(id)
cur.execute(query)
print(cur.fetchone())
cur.close()
con.commit()
con.close()


import mysql.connector 
#Replace the connection string of your MySQL server
con = mysql.connector.connect(host="host", user="username", password="password", database="database_name")
cur = con.cursor()
list_of_ids = [1001,1002,1003,1004]
for id in list_of_ids:
    cur.execute("SELECT * FROM Computer WHERE CompId=%(c_id)s", {"c_id":id} )
    for CompId,Make,Model,MYear in cur:
        print(Make,CompId)
cur.close()
con.close()

#Binding parameters in quires
import mysql.connector
#Assume the MySQL server is running on 'localhost', database name is 'mydb' and user is 'root'
con = mysql.connector.connect(host="localhost", user="root", password="", database="mydb")
cur = con.cursor()
list_of_ids = [1001,1002,1003,1004]
for id in list_of_ids:
    cur.execute("SELECT * FROM Computer WHERE CompId=%(c_id)s",{"c_id":id})
    for CompId,Make,Model,MYear in cur:
        print(Make,CompId)
cur.close()
con.close()


#invoke store functions

DELIMITER //
CREATE FUNCTION increase_by_100 (number INT) RETURNS INT
BEGIN
    RETURN number+100;
END;
//


import mysql.connector 
#Assume the MySQL server is running on 'localhost', database name is 'mydb' and user is 'root'
con = mysql.connector.connect(host="localhost", user="root", password="", database="mydb")
cur = con.cursor()
cur.execute('SELECT increase_by_100(%s)', [10])
print(cur.fetchone())
cur.close()
con.close()

#invoke stored procedures
DELIMITER //
CREATE PROCEDURE promotion_discount(IN discount INT, INOUT price INT)
BEGIN
SET price=price*(1-discount/100);
END;
//
import mysql.connector 
#Assume the MySQL server is running on 'localhost', database name is 'mydb' and user is 'root'
con = mysql.connector.connect(host="localhost", user="root", password="", database="mydb")
cur = con.cursor()
args = [10,1000]
res = cur.callproc('promotion_discount', args)
print(res)
cur.close()
con.close()

----------------
#Mongodb with python

from pymongo import MongoClient
#Establishing MongoDB connection
conn_obj = MongoClient('mongodb://localhost:27017/')
print(type(conn_obj))
database_obj = conn_obj['database_name']
#or
database_obj = conn_obj.database_name

collection_obj = database_obj['collection_name']
#or
collection_obj = database_obj.collection_name

from pymongo import MongoClient
#Establishing MongoDB connection
conn_obj = MongoClient('mongodb://localhost:27017/')
#Creating database object
database_obj = conn_obj ['ETA']
#Creating collection object
collection_obj = database_obj['student']

from pymongo import MongoClient
conn_obj = MongoClient('mongodb://localhost:27017/')
#Fetches the list of databases
db_list = conn_obj.list_database_names()
print(db_list)
database_obj = conn_obj['ETA']
#Fetches the list of collections under 'ETA' database
col_list = database_obj.list_collection_names()
print(col_list)

from pymongo import MongoClient
conn_obj = MongoClient('mongodb://localhost:27017/')
database_obj = conn_obj['ETA']
collection_obj = database_obj['student']
document = {'Name':'John','Regd_id':'1','Age':20,'Sex':'M'}
returnval = collection_obj.insert_one(document)
print(returnval.inserted_id)

from pymongo import MongoClient
conn_obj = MongoClient('mongodb://localhost:27017/')
database_obj = conn_obj['ETA']
collection_obj = database_obj['student']
document_list = [
    {'Name':'Kelley','Regd_id':'2','Age':21,'Sex':'M'},
    {'Name':'Hannah','Regd_id':'3','Age':18,'Sex':'F'},
    {'Name':'Ravi','Regd_id':'4','Age':22,'Sex':'M'},
    {'Name':'Rachel','Regd_id':'5','Age':26,'Sex':'F'},
    {'Name':'Esther','Regd_id':'6','Age':19,'Sex':'F'}
]
returnval = collection_obj.insert_many(document_list)
print(returnval.inserted_ids)


from pymongo import MongoClient
conn_obj = MongoClient('mongodb://localhost:27017/')
database_obj = conn_obj['ETA']
collection_obj = database_obj['student']
#Fetching the first document
print('Find One Document:')
doc = collection_obj.find_one()
print(doc)
#Fetching all the documents
print('Find All Documents:')
docs = collection_obj.find()
for doc in docs:
    print(doc)

from pymongo import MongoClient
conn_obj = MongoClient('mongodb://localhost:27017/')
database_obj = conn_obj['ETA']
collection_obj = database_obj['student']
docs = collection_obj.find({'Sex':'F'})
for doc in docs:
    print(doc)

from pymongo import MongoClient
conn_obj = MongoClient('mongodb://localhost:27017/')
database_obj = conn_obj['ETA']
collection_obj = database_obj['student']
docs = collection_obj.find({'Age':{'$gt':21}})
for doc in docs:
    print(doc)

from pymongo import MongoClient
conn_obj = MongoClient('mongodb://localhost:27017/')
database_obj = conn_obj['ETA']
collection_obj = database_obj['student']
docs = collection_obj.find({},{'_id':0,'Name':1,'Age':1})
for doc in docs:
    print(doc)

from pymongo import MongoClient
conn_obj = MongoClient('mongodb://localhost:27017/')
database_obj = conn_obj['ETA']
collection_obj = database_obj['student']
docs = collection_obj.find({}).sort('Age',1)
for doc in docs:
    print(doc)

from pymongo import MongoClient
conn_obj = MongoClient('mongodb://localhost:27017/')
database_obj = conn_obj['ETA']
collection_obj = database_obj['student']
docs = collection_obj.find({}).limit(2)
for doc in docs:
    print(doc)

from pymongo import MongoClient
conn_obj = MongoClient('mongodb://localhost:27017/')
database_obj = conn_obj['ETA']
collection_obj = database_obj['student']
#Update one record
collection_obj.update_one({'Regd_id':'3'},{'$set':{'Age':25}})
#Update many records
collection_obj.update_many({'Regd_id':{'$gt':'4'}},{'$set':{'Age':24}})
docs = collection_obj.find({},{'_id':0,'Regd_id':1,'Age':1})
for doc in docs:
    print(doc)

from pymongo import MongoClient
conn_obj = MongoClient('mongodb://localhost:27017/')
database_obj = conn_obj['ETA']
collection_obj = database_obj['student']
#Delete one record
collection_obj.delete_one({'Regd_id':'1'})
#Delete many records
collection_obj.delete_many({'Regd_id':{'$gt':'4'}})
docs = collection_obj.find({})
for doc in docs:
    print(doc)

from pymongo import MongoClient
conn_obj = MongoClient('mongodb://localhost:27017/')
database_obj = conn_obj['ETA']
collection_obj = database_obj['student']
print('Before Dropping the collection:')
for doc in collection_obj.find():
    print(doc)
#Dropping the collection
collection_obj.drop()
print('After Dropping the collection:')
for doc in collection_obj.find():
    print(doc)


#python programmer question
def abberivation(s):
    words=s.split()
    a=''
    for w in words:
        if(len(w)>2):
            a+=w[0].upper()
        elif(len(w)==2):
            a+=w[0].lower()
    return a
s=input()
print(abberivation(s))
'''
 
import numpy as np
int_array=np.array([1,2,3,4])
float_array=np.array([1.0,2,3,4])
string_array=np.array(["orange,mango,apple"])
string_array=np.array(["orange","mango","apple"])
string_array
type(int_array)
type(float_array)
type(string_array)
#same output for above
int_array.dtype
float_array.dtype
string_array.dtype
x=np.array([1.0,1.2,3,4], dtype=np.int32)
x.dtype
b=np.arange(1,10)
b
b[0:3]
b[:8:2]
b[5:]
b[-1]

#boolean indexing
s=[1,2,3,4,5,6,7]
boolean_list=[]
for i in s:
    if i>3:
        boolean_list.append(True)
    else:
        boolean_list.append(False)

boolean_list
b>3
b[b>3]
#numpy matrix and multi-dimensions
m=np.matrix([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
m.shape
m.ndim
m[1]
m[1,1]
x=np.array([
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ],
])
x.shape
x.size
x.ndim
#numpy methods and operations
a=np.linspace(1,10,2)
a
a=np.arange(1,10,2)
a
np.zeros((2,3))
np.ones((3,3))
x=np.eye(3)
np.diag(x)
#Arthametic operations
A=np.array([[1,2],[3,4]])

B=np.array([[1,2],[3,4]])
np.add(A,B)
#np.subtract(a,b)
#np.multipy(a,b)
#np.divide(a,b)
A+B
A-B
A*B
A/B
x=np.dot(A,B)
xx=np.dot(A,B)
x
#determinant of matrix
np.linalg.det(x)#determinant of matrix
np.linalg.det(x)

#eigen values
np.linalg.eig(x)
#eigen values
np.linalg.eigvals(x)#eigen values
np.linalg.eigvals(x)
#inverse of mat
np.linalg.inv(x)#inverse of mat
np.linalg.inv(x)
#random method
np.random.randint(4)
np.random.randint(0,2,10)
#last 10 indiactes no of elements#random method
np.random.randint(4)
np.random.randint(0,2,10)
#last 10 indiactes no of elements
np.random.randint(-4,4)np.random.randint(-4,4)
np.random.randint(-10,10,(3,3))np.random.randint(-10,10,(3,3))
np.random.randint(-10,10,(3,3,3))np.random.randint(-10,10,(3,3,3))
np.random.rand(3)np.random.rand(3)
np.random.rand(3,3)np.random.rand(3,3)
np.random.rand(3,3,3)np.random.rand(3,3,3)
np.random.randn(3)np.random.randn(3)
np.random.randn(2,2)np.random.randn(2,2)

#import pandas as pd


    

