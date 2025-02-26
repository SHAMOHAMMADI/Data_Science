# #comment
# """comment"""
# '''comment'''


# firstName = "max"
# lastName = "ramini"

# year , first_name , last_name , birth_date = (1985 , "mustafa", "shamohammadi" , "1985/5/30")
# fullName = firstName + " " + lastName
# print(first_name , last_name , year , birth_date)
# print(fullName)

# car = ["mclaren" ,"benz" , "aston martin"]
# print(type(car))
# is_done = False # False with capital 

# for car in car:
#     print(car)

# # input1 = input("please enter your number: ")
# # print(input1)
# mybirthday = 2025
# # myage = mybirthday - int(input1) # int() float() bool() str()

# # print(myage)

# age2 = 44 
# print(age2>40 and age2<50)
# print(age2>50 or age2>45)


# first_name = "mustafa"
# score = 20 
# print("hello" + first_name + "your score is "+ str(score))
# print("hello {first_name} your score is {score}".format(first_name = first_name , score = str(score)))
# print(f"hello{first_name} your score is {str(score)}") # concatenation

# course = "python crash course!"
# print(course.upper()) 
# print(course.replace("crash" , "beginner"))

# course = course.replace("crash" , "beginner")

# print(course)

# print(course.count("o"))

# print(course.startswith("python"))
# print(course.endswith("course"))
# print(course.endswith("!"))
# print(course.split(","))
# print(course.isalpha())#for alphabetic 
# print(course.isnumeric())# for number


# # list 
# student_name = ["sarvin" , "sam" , "sara ", "mina"]
# # student_name = list(("sarvin" , "sam" , "sara" , "mina"))

# print(student_name ,  type(student_name))

# print(student_name[0])

# student_name[1] = "samsum"
# print(student_name)

# print(student_name[1:3])
# print(student_name[1:])#1 til last item
# print(student_name[:3])

# nums = [1 , 2 , 3 , 4 , 5]
# nums.append(7)
# print(nums)
# nums.insert(3 , 25)
# nums.remove(1)# remove amount 1
# nums.pop(0) # remove index 0
# nums.reverse()
# nums.sort()
# print(nums)

# print(7 in nums)
# nums.clear()
# print(len(nums))
# #/////////////////////////////////////////
# #Tuple = a list you can change the list

# course2 = ('html' , 'css' , 'java')
# # course2 = ('html',)
# # course[1] = 'c++' # you can change item
# del course2


# # print(course2 , type(course2))

# # print(course2[2])


# #/////////////////////////////////////////////////////////////////////////////
# # set : no index , dont repeat item
# course3 = {'html','css','java'}
# print(course3 , type(course3))
# course3.add('html')# it can't possible to add
# course3.remove('css')
# course3.clear()
# print(course3)

 
# #/////////////////////////////////////////////////////////////////////////////
# #dictionary
# # first way
# student = { 
#     'first_name' : 'John',
#     'last_name' : 'Doe',
#     'age' : 30,
#     'isDone' : True
# }
# # second way
# # student = dict(first_name = 'sarvin' , last_name = 'tabatabaei' , age = 42)


# print(student ,  type(student))

# print(student['age'])
# print(student.get("age"))

# student["phone"] = '99-9999-99999'

# print(student)

# person = student.copy()
# person["city"] = "tehran"
# print(f"person : {person}")

# del(person["city"])
# print(f"person : {person}")
# person.pop("age")
# print(f"person : {person}")

# print(len(student))
# student.clear()
# print(student)

# print(student.keys())
# print(student.items()) 


# #dictionary
# people = [
#     { "name" : "sarvin" , "class" : "html"},
#     {"name" : "sam" , "class" : "css"}
# ]

# print(people[0]["name"])


# # function

# def sayHello (name = "ali"):
#     print("hello")
#     x = name 
#     print("hello " + x)

# def getSum(x , y):
#     total = x + y
#     return total

# result = getSum(10 , 5)
# print(result)

# sayHello()

# # lambda function
# getSum = lambda p1 , p2 : p1 + p2 

# # equal to up
# # def getSum(p1 , p2):
# #     return p1 + p2 

# print(getSum(1 , 2))


# #condition 
# # if condition :
# x = 25 
# y = 25
# if x>y:
#     print("x is greater than y")
#     print("condition")
# elif x==y:
#     print(f"{x} is equal to {y}")
# else:
#     print(f"{x} is not greater than y")

# print("done")

# #nested if 
# if x>y:
#     if x==40:
#         print("x>y and x=40")

# if x>30 and y==30:
#     print("x>30 and y = 30")

# if not(x>30):
#     print("x is not greater than 30")


# #membership(in , not in)
# num = [1 , 2 , 3 , 4 , 5]
# x=8
# if x in num:
#     print("x is in num")

# if x not in num:
#     print("x is not in num")

# #identify operator ( is , not is)
# x2 = 3
# y2 = 3
# if x2 is y2:
#     print("x is y")
# if x2 is not y2: 
#     print("x2 is not y2")


# #loop
# student = ["sara" , "sarvin" , "dara" , "john"]

# for item in student:
#     if item == "dara":
#         break
#        # continue
#     print(f"student is {item}")

# #range 
# # for i in range(10):
# # # for i in range(5 , 10): 5 til 10
# #     print(i)

# for i in range(len(student)):
#     print(i)

# #while
# count = 0
# while count<10:
#     print(f"count is {count}")
#     count+=2 


# #module

# #core modules

# import datetime
# # from datetime import datetime # when we want to import one item from datetime

# # today = datetime.today()
# today = datetime.datetime.today()
# print(today)

# #external module  
# #in command line    pip3 install camelcase
# #if you write         pip3 freeze          which what package install in your system
# from camelcase import CamelCase

# c=CamelCase()
# print(c.hump("sarvin style codding"))

# #import validate
# # from validate import validate_email
# email = "sarvin@sarvinstyle.com" 

# # print(validate_email(email))


# #create class

# class User:
#     def __init__(self , name ,email ,  birth_year): #  constructor , self like this in other language 
#         self.name = name
#         self.email = email
#         self.birth_year = birth_year
#     def greeting(self):
#         return f"your name is {self.name}"
    
#     def get_age(self):
#         return 2022 - self.birth_year
    

# newUser = User("sarvin" , "sarvin@sarvinstyle.com" , 1979)
# print(type(newUser))
# print(newUser.greeting())
# print(newUser.get_age())

# class Student (User):
#     def __init__(self, name,email,birth_year):
#         self.name=name 
#         self.email = email
#         self.birth_year = birth_year
#         self.score = 0
    
#     def set_score(self , score):
#         self.score = score
    
#     def get_score(self):
#         return self.score

# sara = Student("sara" , "sarvin@sarvinstyle.com" , 1989)
# sara.set_score(10)
# print(sara.get_score()) 


# #file
# newfile = open("new.txt", "w") # name of file and type "w" refer to write
 
# print(f"name : {newfile.name} is colsed : {newfile.closed},mode : {newfile.mode}")
# newfile.write("first msg ")
# newfile.write("second msg")
# newfile.close()

# #append
# newfile = open("new.txt" , "a") # append
# newfile.write("first msg2")
# newfile.write("second msg2")
# newfile.close()

# #read
# newfile = open("new.txt", "r")
# text = newfile.read(5)#5 words
# print(text) 

# # json
# import json
# sampleJson= '{"name":"sarvin" , "last_name " : "taba" , "course" : "python" }'
# user = json.loads(sampleJson)

# print(user)
# print(user["name"])

# user2 = { 'name' : 'sara' , 'last_name' : 'due' , 'course' : 'css'}
# user2tojson = json.dumps(user2)
# print(user2tojson)

















# #comment
# """comment"""
# '''comment'''

# #Variables
# nameOfSystem = "mark"
# nameOfCategory = "employee"
# name , family , age , bornDate = ("mark" , "zackerberg" , "35" , "1989-01-01")
# print(name , family , age , bornDate)

# #list 
# listSample = [5 , 5 , 6 , 8]
# listSample2 = list((4 , 2 , 6 , 7 , 9))

# print(listSample , listSample2 )

# #tuple no change 
# tupleTest = ('ali' , 'rezaei' , 36)
# print(tupleTest)


# #set no index - no repeat
# setSample = {'rust' , 'golang' , 'programmin' , 'rust'}


# #dictionary 
# dicSample = {
#     "id" : "1",
#     "description" : "the item which is existed in the store",
#     "title":"cat1"
# }

# dicSample2 = dict( id = "3", description = "the item which is existed in the item Box")
# print(dicSample2)

# dicSample3 = [
#     {
#         "id" : "8",
#         "description" : "the item which is existed in the item box"
#     },
#     {
#         "id" : "9",
#         "description": "the item which is not equal to "
#     }
# ]

# print(dicSample3[0]['id'])

# print(dicSample["description"])








# def functionSample (a , b):
#     return a ** b
# print(functionSample(6 , 2))

# functionSample2 = lambda amount1 , amount2: amount1 ** amount2

# print(functionSample2(3 , 3))


# class classSample :
#     def __init__ (self , familyName , Company , age , bornDate):
#         self.name = familyName , 
#         self.Company = Company , 
#         self.age = age ,
#         self.bornDate = bornDate

#     def getName (self):
#         return f"the employee is {self.name}"
    
#     def getFullData (self):
#         return f"all info of employee is {self.name , self.Company , self.age , self.bornDate}"


# employee1 = classSample("aliMohammadi" , "alphapars", "36","1985-01-01")
# employee2 = classSample("rezaAhmadi" , "ioetech", "32" , "1983-01-01")
# print(f"the first employee is {employee1.getFullData()} and the second employee is {employee2.getFullData()}")

# #newfile 

# newfile = open('new.txt','w')
# print(f"name:{newfile.name} is closed :{newfile.closed} > mode : {newfile.mode}")

# newfile.write("firstMessage")
# newfile.write("secondMessage")
# # newfile.closed()

# newfile.write("thirdMessage ")
# newfile.write("fourMessage ")


# newfile = open("new.txt","a")
# newfile.write("fivthMessage")

# newfile = open("new.txt" , "r")
# text = newfile.read(6)
# print(text)
# # newfile.closed()


# # import json
# # sampleJson = '{
# # "name":"sarvin","lastname": "taba", "course" : "python"
# # }'
# # user = json.loads(sampleJson)
# # print(user)





























# import mysql.connector

# mydb = mysql.connector.connect(
#     host = "localhost",
#     username="admin",
#     password = "foo"
# )

# mycursor = mydb.mycursor()

# mycursor.execute("CREATE DATABASE python")

from zeep import Client

wsdl_url = "http://www.dneonline.com/calculator.asmx?WSDL"

client = Client(wsdl_url)
print(client)