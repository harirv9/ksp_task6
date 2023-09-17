# printing in python
print("hello all")
print(3+4)

# comments
# it is used to add comments in python

# variables
app1=10 # app is the variable and 10 is the value
app2="banana" #
app3=15.6
print(app1)
print(app2)
print(app3)

#data types
fruit= "apple" #string data type
ball=5 #integer data type
car=5.5 #float data type
bikes=True #boolean
print(bikes)
print(ball+car)
print(fruit)

#coverting data types
#converting int to float
print(float(app1))
#converting float to int
print(int(car))
#converting int to string
print(str(ball))
# checking data type
print(type(app1))
print(type(bikes))
print(type(fruit))

# strings
fruit1="guava"
print(fruit1)
name="Harika Ravula"
print(name)
print(name[2])

#string methods
#captialize
txt="hello world"
x=txt.capitalize()
print(x)
#casefold
txt1="Hello World, How are You"
x=txt1.casefold()
print(x)
#center
txt2="apple ball cat"
x=txt2.center(30)
print(x)
#lower
txt3="HELLO"
print(txt3.lower())
#upper
print(txt.upper())
#index
print(txt.index("world"))
#count
print(txt1.count("are"))
#isdecimal
txt5="12345"
print(txt5.isdecimal())
#isdigit
print(txt5.isdigit())
#replace
print(txt1.replace("World", "guys"))
#rsplit
txt6="apple, banana, guava"
print(txt6.rsplit(","))

#for loop
for x in "banana":
    print(x)
    for x in range(10):
        print(x)
        for x in txt6:
            print(x)


# if else loop
a=33
b=20
if a>b:
    print("a is greater than b")
elif a==b:
    print("a is equal to b")
else :
    print("a is less than b")

#functions

def  greeting() :
    print("hello world")

greeting()

#passing parameters and arguments
def greeting1(name):
    print("hi "  +name)
greeting1("harika") 

def add(num1,num2):
    print(num1+num2)
add(20,30)













      




