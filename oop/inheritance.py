# class Person:
#     def __init__(self,f_name,l_name):
#         self.first_name = f_name
#         self.last_name = l_name
#
#     def print_name(self):
#         print(self.first_name, self.last_name)
#
# p1 = Person("David","Cohen")
# p1.print_name()
#
# class Student(Person):
#     def __init__(self,f_nam,l_name,inst):
#         # Person.__init__(self,f_nam,l_name)
#         super().__init__(f_nam,l_name)
#         self.institution = inst
#
# s1 = Student("Avi","Levi","Kod_code")
# s1.print_name()
# print(s1.institution)



# class Animal:
#     def __init__(self,age,height,weight):
#         self.age = age
#         self.height = height
#         self.weight = weight
#
#     def add_10_years(self):
#         self.age += 10
#
# class Cat(Animal):
#     def __init__(self,age,height,weight,mus_color):
#         super().__init__(age,height,weight)
#         self.mustache_color = mus_color
#
#     def get_mus_color(self):
#         return self.mustache_color


# a1 = Animal(10,0.75,35)
# c1 = Cat(8,25,0.5,"brown")
#
# c1.add_10_years()
# print(c1.age)
#
# color = c1.get_mus_color()
# print(color)

# class Building:
#     def __init__(self,address,length,width):
#         self.address = address
#         self.length = length
#         self.width = width
#
#
# class Mossad:
#     purpose = "Tora"
#     def __init__(self,name,n_people,n_staff):
#         self.name = name
#         self.n_people = n_people
#         self.n_staff = n_staff
#     def set_building(self,address,length,width):
#         self.building = Building(address,length,width)
#
# m1 = Mossad("Tora school",200,30)
# m1.set_building("union 10",50,20)
#
# print(m1.building.length)































