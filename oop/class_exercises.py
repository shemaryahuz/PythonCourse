# def f():
#     print("hi")
#
# d = {"field":[1,2], "function":f}
#
# print(d["field"])
# d["function"]()



# class MyClass:
#     def __init__(self,x):
#         self.num = x
#
# o1 = MyClass(8)



#     number = 5
#
# object1 = MyClass()
#
# object2 = MyClass()
# object2.number = 10
# print(object2.number)
#
# print(object1.number)



# class BankAccount:
#     def __init__(self,x,y):
#         self.name = x
#         self.balance = y
#
#     def __str__(self):
#         return  f"My name is {self.name} and my balance is {self.balance}"
#
#     def __add__(self, other):
#         self.balance += other.balance
#
#     @staticmethod
#     def struction(a, b):
#         return a - b
#
#
# print(BankAccount.struction(5, 4))
#
# account1 = BankAccount("David",50)
#
# account2 = BankAccount("Adam",400)
#
# account1  + account2
#
# print(account1)
#
# print(account2)



# account1.balance += 100
#
# account3 = BankAccount("Ben",300)
#
# accounts = [account1,account2,account3]
#
# sum_all = 0
# for account in accounts:
#     sum_all += account.balance
#
# print(sum_all)

# class Person:
#     def __init__(self,height,weight):
#         self.height = height
#         self.weight = weight
#
# class BankAccount:
#     def __init__(self,x,y,p):
#         self.name = x
#         self.__balance = y
#         self.person = p
#
#     def add_15(self):
#         return self.__balance + 15
#
#     def set(self,z):
#         if z < 1000000:
#             self.__balance = z
#         else:
#             print("invalid operation")
#
#     def get_balance(self):
#         return self.__balance

# print(f"{account1.name}'s balance is {account1.add_15()}")
#

#
# x = account2.add_15()
# print(f"{account2.name}'s balance is {x}")



# person1 = Person(170,80)
# person2 = Person(180,70)
#
# account1 = BankAccount("David",15,person1)
# print(account1.person.height)
#
#
# account2 = BankAccount("Adam",400,person2)
# account2.set(2000000)
# print(account2.get_balance())


# class Quadrilateral:
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width
#
#
# class ColorQuadrilateral(Quadrilateral):
#     def __init__(self,length,width,color):
#         super().__init__(length,width)
#
#
#
# class Rectangle:
# class Square:

# class MyClass:
#     def __init__(self,x):
#         self.number = x
# object1 = MyClass(5)
#
# print(object1)
# print(type(object1))
# print(MyClass)
# print(type(MyClass))
#
# class Mossad:
#     purpose = "Tora"
#     def __init__(self,name,n_people,n_staff):
#         self.name = name
#         self.n_people = n_people
#         self.n_staff = n_staff
#
#     def set_building(self,address,length,width):
#         self.building = Building(address,length,width)
#
# class Building:
#     def __init__(self,address,length,width):
#         self.address = address
#         self.length = length
#         self.width = width
#
#     def get_area(self):
#         return self.length * self.width
#
# class Yeshiva(Mossad):
#     def super.__init__:


# class Person:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def __str__(self):
#         return f"Hi! my name is {self.first_name} {self.last_name}"
#
#     def __len__(self):
#         return len(self.first_name) + len(self.last_name)
#
#     def get_full_name(self):
#         return self.first_name + " " + self.last_name
#
#     def set_full_name(self, new_full_name):
#         self.first_name = new_full_name.split(" ")[0]
#         self.last_name = new_full_name.split(" ")[1]
# #
# person1 = Person("Eli","Gross")
# # person1.first_name = "Moshe"
# # print(person1.get_full_name())
# # person1.set_full_name("David Levi")
# # print(person1.get_full_name())
# print(person1)
# print(len(person1))