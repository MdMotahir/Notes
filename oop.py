# class Students:
#     count=0
#     def __init__(self,roll_no,std,marks):
#         self.roll_no=roll_no   # this is the variable of a object which is under the class Students
#         self.std=std          # this is the variable of a object which is under the class Students
#         self.marks=marks          # this is the variable of a object which is under the class Students
#         Students.count+=1         # this is the variable of a object which is under the class Students
#     def percentage(self):
#         self.per=(sum(self.marks.values())/500)*100
#         if self.per < 40:
#             self.results="Pass"
#         else:
#             self.results="Fail"
#         return f"{self.per},{self.results}"
    
#     def get_details(self):
#         return f"{self.roll_no},{self.percentage()}"

# stud1 = Students(1,5,{"eng":75,"phy":50,"chem":60,"maths":80,"bio":40})
# stud2 = Students(2,5,{"eng":70,"phy":71,"chem":55,"maths":80,"bio":80})
# stud3 = Students(3,5,{"eng":70,"phy":71,"chem":55,"maths":80,"bio":80})
# stud4 = Students(4,5,{"eng":30,"phy":30,"chem":30,"maths":30,"bio":30})

# students=[stud1,stud2,stud3,stud4]
# for i in students:
#     i.percentage()  #for any object we must have pass the percentage() because we did not return any things in def percentage(self): so we do this
                    # here i for all objects
# stud1.percentage()
# print(stud1.get_details())
# for i in students:
#     if i.results=='Fail':
#         print(i.get_details())

# print(Students.count)
# print(stud1.get_details())






# class Course:  
#     courses = []
#     @classmethod
#     def check_course(cls,c_id):
#         for course in cls.courses:
#             if course.c_id == c_id:
#                 return course
#         else:
#             return "Course Id did not match"
        
#     @classmethod
#     def add_course(cls,obj):
#         cls.courses.append(obj)
                
#     def __init__(self,c_id,c_name,c_desc,author):
#         self.c_id= c_id
#         self.c_name = c_name
#         self.c_desc = c_desc
#         self.author = author
#         Course.add_course(self)

# class Tutorial:
#     tutorials = []
#     @classmethod
#     def add_tutorials(cls,obj):
#         cls.tutorials.append(obj)
#     def __init__(self,t_id,t_name,t_content,course):
#         self.t_id = t_id
#         self.t_name = t_name
#         self.t_content = t_content
#         self.course = course        
#         Tutorial.add_tutorials(self)
#     def get_details(self):
#         return self.t_id,self.t_name,self.t_content
        

# class Author:
#     def __init__(self,name,prof,exp,tech):
#         self.name = name
#         self.prof = prof
#         self.exp = exp
#         self.tech = tech

# auth1 = Author("ABC","xyz",5,['c','c++','python'])
# auth2 = Author("ABD","xya",7,['c','python'])
# auth3 = Author("ABE","xyb",5,['python'])
# auth4 = Author("ABF","xyc",10,['python'])

# # print(auth1.__dict__)

# course1 = Course(101,"Python","Python Beg. to Advanced",auth1)
# course2 = Course(102,"Django","Django Beg. to Advanced",auth4)

# # print(course1.__dict__)

# tut1 = Tutorial(1,"Python basics","Operators,Conditional Statements",course1)
# tut2 = Tutorial(2,"Python loops","For,While Loops",course1)
# tut3 = Tutorial(3,"Python lists","Append,Extend,Insert",course1)

# tut4 = Tutorial(4,"Django Models","Models,Migrations,Model fields",course2)
# tut5 = Tutorial(5,"Django Views","Class Based and Function based views",course2)

# # for i in Tutorial.tutorials:#here tutorials is a class variable.
# #     # if i.course.author.name=="ABC":
# #     #     print(i.get_details())
# #     print(i.course.c_name)

# # for i in Tutorial.tutorials:#here tutorials is a class variable.
# #     if i.course.c_id==102:
# #         print(i.get_details())
# #     else:
# #         print("NO object is there")

# # for i in Tutorial.tutorials:
# #     print(i)

# # print(Course.check_course(105))









# class Offer:
#     def __init__(self,offer_id,min_qty,offer_price):
#         self.offer_id=offer_id
#         self.min_qty=min_qty
#         self.offer_price=offer_price

# class Products:
#     products=[]
#     @classmethod
#     def add_obj(cls,obj):
#         cls.products.append(obj)

#     def __init__(self,product_id,product_name,unite_price,stock,offer=None):
#         self.product_id=product_id
#         self.product_name=product_name
#         self.unite_price=unite_price
#         self.stock=stock
#         self.offer=offer
#         Products.add_obj(self)

# class Admin:
#     def __init__(self,name,username,email):
#         self.name=name
#         self.username=username
#         self.email=email
    
#     def add_products(self,product_id,product_name,unite_price,stock,offer=None):
#         product=Products(product_id,product_name,unite_price,stock,offer)
#         return product
#     def add_offer(self,offer_id,min_qty,offer_price):
#         offer=Offer(offer_id,min_qty,offer_price)
#         return offer

# class System:
#     @classmethod
#     def calculate(cls,cart):
#         total=0
#         for key,value in cart.items():
#             if key.offer:
#                 if value% key.offer.min_qty ==0:
#                     total+=key.offer.offer_price*(value//key.offer.min_qty)
#                 else:
#                     total+=key.offer.offer_price*(value//key.offer.min_qty)+ value%key.offer.min_qty*key.unite_price
#             else:
#                 total+=key.unite_price*value
#         return total


# class Customer:
#     def __init__(self,name,contact):
#         self.name=name
#         self.contact=contact
#         self.cart={}

#     def add_cart(self,product_name,quantity):
#         if product_name not in self.cart:
#             self.cart.setdefault(product_name,quantity)
#         else:
#             self.cart[product_name]+=quantity
    
#     def view_cart(self):
#         return {key.product_name:value for key,value in self.cart.items()}
    
#     def checkout(self):
#         return System.calculate(self.cart)



# admin=Admin("ABC","abc","abc@gmail.com")


# off1=Offer(101,3,120)
# off2=Offer(102,2,45)

# # print(admin.__dict__)
# p1=admin.add_products(1,"A",50,100,off1)
# p2=admin.add_products(1,"B",30,100,off2)
# p3=admin.add_products(1,"C",20,100)

# # for i in Products.products:
# #     print(i)

# cust1=Customer("BBB",'7787030497')
# print(cust1.view_cart())

# cust1.add_cart(p1,15)
# cust1.add_cart(p3,10)
# cust1.add_cart(p1,3)
# print(p1.offer.__dict__)

# print(cust1.view_cart())
# print(cust1.checkout())

# print("------------------------------")
# cust2=Customer("AAA",'778655647030497')
# cust2.add_cart(p1,3)
# cust2.add_cart(p2,5)
# cust2.add_cart(p1,3)

# print(cust2.view_cart())
# print(cust2.checkout())



# new class \
# def hello():
#     print('hello')
# print(type(hello))

# class Dog:
#     pass

# class Students:
#     def __init__(self,name,age,grade):
#         self.name=name
#         self.age=age
#         self.grade=grade
    
#     def get_grade(self):
#         return self.grade
    

# class Course:
#     def __init__(self,name,max_students):
#         self.name=name
#         self.max_students=max_students
#         self.student=[]

#     def add_students(self,students):
#         if len(self.student)<self.max_students:
#             self.student.append(students)
#             return True
#         return False

#     def get_avg_grade(self):
#         return sum(Students.get_grade())/len(Students)


# s1=Students('raji',19,75)
# s2=Students('mot',20,62)
# s3=Students('kab',18,83)
# s4=Students('kau',20,95)
# s5=Students('tab',18,85)
# s6=Students('mah',19,65)

# course1=Course('Math',3)
# course2=Course('Science',2)
    

# course1.add_students(s3)
# course1.add_students(s5)
# course2.add_students(s4)
# course1.add_students(s1)
# course1.add_students(s6)


# # print(course1.student[0].age)
# # print(course2.student)
# print(course1.get_avg_grade)

# l1=[{'name':'raj'},{'age':'24'}]
# keys=[]
# for i in l1:
#     keys.append(i.keys())

# print(keys)



# class Computer:
#     pass




# c1=Computer()
# c2=Computer()

# print(id(c1)) #the size of the objec is depend upon the no. of variable so if the no. of variable of a object is increse then the size is increases.
# print(id(c2))         #every  time it creat a new address in ram

# variable has 2 types 
        # 1st one is instance variable ----------besically whic is called in __init__ they are instance
        #class veriable and statics variables ------------ generally which is called in class and that is constant for every object

# types of methods
        #instance methods ---------- which methods work with object is known as instance methods like if we want to fined the avg of students then we use this methods
        #class methods ----------- if we work in a methods by useing class then we use (cls) in behalf of (self) before his we use @classmethods mainly it work only for class variable
        #static methods ---------- before this we use @staticmethod and generally it is not link with class or instance variable.

