# class Animal:
#     sound = ""
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def make_sound(self):
#         return self.sound
#
#     def describe(self):
#         return f"I am {self.name} and I am {self.age} years old"
#
# class Dog(Animal):
#     sound = "Woof!"
#     def __init__(self, name, age, breed):
#         super().__init__(name,age)
#         self.breed = breed
#
#     def fetch(self):
#         return f"{self.name} is fetching the ball"
#
# class Cat(Animal):
#     sound = "Meow!"
#     def __init__(self,name, age, mustache_color):
#         super().__init__(name,age)
#         self.mustache_color = mustache_color
#
#     def scratch(self):
#         return f"{self.name} is scratching"
#
#
# animal1 = Animal("Jim",8)
# dog1 = Dog("Jho",10,"bulldog")
# cat1 = Cat("Kity",5,"brown")
#
# print(animal1.describe())
# print("")
# print(dog1.describe())
# print(dog1.make_sound())
# print(dog1.fetch())
# print("")
# print(cat1.describe())
# print(cat1.mustache_color)
# print(cat1.make_sound())
# print(cat1.scratch())



# class Person:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def __str__(self):
#         return f"Hello my name is {self.first_name} {self.last_name}!"
#
#     def __repr__(self):
#         return {"first_name": self.first_name, "last_name": self.last_name}
#
# class Student(Person):
#     def __init__(self, first_name, last_name, institution):
#         super().__init__(first_name, last_name)
#         self.institution = institution
#         self.__grades = {}
#
#     def set_grade(self,subject, grade):
#         self.__grades[subject] = grade
#
#     def get_grades(self):
#         return self.__grades
#
#     def get_average(self):
#         counter = 0
#         is_sum = 0
#         for subject in self.__grades:
#             counter += 1
#             is_sum += self.__grades[subject]
#         return is_sum/counter
#
#
# student1 = Student("David","Friedman","Kod_code")
# student1.set_grade("English", 100)
# student1.set_grade("Math", 110)
# student1.set_grade("Python", 120)
#
# print(student1.get_grades())
# print(student1.get_average())
# print(student1)
# print(student1.__repr__())



class BankAccount:
    def __init__(self, initial_balance):
        # צריך להגדיר שדה פרטי balance
        self.__balance = initial_balance

    def deposit(self, amount):
        # צריך להוסיף את amount ליתרה
        self.__balance += amount

    def withdraw(self, amount):
        # צריך להוריד את amount מהיתרה אם יש מספיק כסף
        if self.__balance > amount:
            self.__balance -= amount
        else:
            print("The amount is greater than the balance!")

    def get_balance(self):
        # צריך להחזיר את היתרה הנוכחית
        return self.__balance

# bank_account = BankAccount(1000)
# bank_account.__balance = 500
# print(bank_account.__balance)
# bank_account.deposit(2000)
# bank_account.withdraw(4000)
# bank_account.withdraw(1500)
# print(bank_account.get_balance())


# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#
#     def __str__(self):
#         # צריך להחזיר מחרוזת בפורמט המבוקש
#         return f"The book: {self.title} by {self.author}"
#
#     def __repr__(self):
#         # צריך להחזיר מחרוזת בפורמט המבוקש
#         return f"Book(title = '{self.title}', author = '{self.author}')"
#
#     def __add__(self, other):
#         # צריך להחזיר רשימה של שני הספרים
#         book_list = [self.__repr__(), other.__repr__()]
#         return book_list
#
# book5 = Book("History", "Smith")
# book6 = Book("History2", "Smith")
#
# print(book5)
# print(book5.__repr__())
# print(book6)
# print(book6.__repr__())
#
# print(book5 + book6)


# class Contact:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     @property
#     def full_name(self):
#         # צריך להחזיר את השם המלא
#         return self.first_name + " " + self.last_name
#
#     @full_name.setter
#     def full_name(self, full_name):
#         # צריך לעדכן את השם הפרטי ושם המשפחה
#         name_list = full_name.split(" ")
#         self.first_name = name_list[0]
#         self.last_name = name_list[1]
#
# contact = Contact("Ben", "Gold")
# print(contact.full_name)
# contact.full_name = "Benjamin Goldman"
# print(contact.full_name)




# def myfunc1():
#   x = "Jane"
#   def myfunc2():
#     nonlocal x
#     x = "hello"
#   myfunc2()
#   return x
#
# print(myfunc1())


























