"""
תרגילים בתכנות מונחה עצמים
===========================
לפניכם סדרת תרגילים בנושאים:
- כימוס (שדות פרטיים)
- מתודות קסם (__str__, __repr__, __add__)
- Getters & Setters
- מתודות סטטיות
- ארכיטקטורה של תכנות מונחה עצמים

השלימו את הקוד החסר במקומות המסומנים ב-pass
"""

# ==============================================
# תרגיל 1: כימוס - חשבון בנק
# ==============================================
"""
השלימו את המחלקה BankAccount כך שתממש חשבון בנק עם:
- שדה פרטי balance שמכיל את יתרת החשבון
- מתודות deposit ו-withdraw שמשנות את היתרה
- הקפידו על כימוס נכון כך שלא ניתן יהיה לשנות את היתרה ישירות
"""


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

bank_account = BankAccount(1000)
bank_account.deposit(2000)
# bank_account.withdraw(4000)
bank_account.withdraw(1500)
# print(bank_account.get_balance())

# ==============================================
# תרגיל 2: מתודות קסם - ספר
# ==============================================
"""
השלימו את המחלקה Book כך שתממש:
- מתודת __str__ שמחזירה מחרוזת בפורמט "הספר: [שם] מאת [מחבר]"
- מתודת __repr__ שמחזירה מחרוזת בפורמט "Book(title='[שם]', author='[מחבר]')"
- מתודת __add__ שמאפשרת לחבר שני ספרים לסדרה (מחזירה רשימה של שני הספרים)
"""


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        # צריך להחזיר מחרוזת בפורמט המבוקש
        return f"The book: {self.title} by {self.author}"

    def __repr__(self):
        # צריך להחזיר מחרוזת בפורמט המבוקש
        return f"Book(title = '{self.title}', author = '{self.author}')"

    def __add__(self, other):
        # צריך להחזיר רשימה של שני הספרים
        book_list = [self.__repr__(), other.__repr__()]
        return book_list



# ==============================================
# תרגיל 3: Getters & Setters - איש קשר
# ==============================================
"""
השלימו את המחלקה Contact כך שתממש:
- Property עבור full_name שמורכב משם פרטי ושם משפחה
- Setter ל-full_name שמעדכן את השם הפרטי ושם המשפחה בהתאם
"""


class Contact:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        # צריך להחזיר את השם המלא
        return self.first_name + " " + self.last_name

    @full_name.setter
    def full_name(self, full_name):
        # צריך לעדכן את השם הפרטי ושם המשפחה
        self.first_name = full_name.split(" ")[0]
        self.last_name = full_name.split(" ")[1]



# ==============================================
# תרגיל 4: מתודות סטטיות - מחשבון
# ==============================================
"""
השלימו את המחלקה Calculator כך שתממש:
- מתודות סטטיות לפעולות חשבון:
  * add: חיבור שני מספרים
  * multiply: כפל שני מספרים
  * power: העלאה בחזקה
  * is_even: בדיקה האם מספר זוגי
"""


class Calculator:
    @staticmethod
    def add(a, b):
        # צריך להחזיר את סכום המספרים
        return a + b

    @staticmethod
    def multiply(a, b):
        # צריך להחזיר את מכפלת המספרים
        return a * b

    @staticmethod
    def power(base, exponent):
        # צריך להחזיר את base בחזקת exponent
        return base ** exponent

    @staticmethod
    def is_even(number):
        # צריך להחזיר True אם המספר זוגי, אחרת False
        if number % 2 == 0:
            return True
        return False



# ==============================================
# תרגיל 5: מתודות מופע - ספריה
# ==============================================
class Library:

    def __init__(self):
        self.library_list = []

    def add_book(self,book):
        self.library_list.append(book.__repr__())

    def borrow_book(self, book, name):
        self.library_list.remove(book.__repr__())

    def return_book(self, book):
        self.library_list.append(book.__repr__())

    def is_book_available(self, book):
        if book.__repr__() in self.library_list:
            return True
        return False

# ==============================================
# קוד בדיקה
# ==============================================

def test_all():
    print("בדיקת תרגיל 1:")
    account = BankAccount(1000)
    account.deposit(500)
    account.withdraw(200)
    print(f"יתרה: {account.get_balance()}")  # אמור להדפיס 1300
    print("")

    print("בדיקת תרגיל 2:")
    book1 = Book("הארי פוטר", "ג'יי.קיי רולינג")
    book2 = Book("שר הטבעות", "ג'.ר.ר טולקין")
    print(book1)  # אמור להדפיס "הספר: הארי פוטר מאת ג'יי.קיי רולינג"
    print([book1, book2])  # אמור להדפיס ייצוג של שני הספרים
    combined = book1 + book2
    print(f"ספרים בסדרה: {len(combined)}")  # אמור להדפיס 2
    print("")

    print("בדיקת תרגיל 3:")
    contact = Contact("ישראל", "ישראלי")
    print(contact.full_name)  # אמור להדפיס "ישראל ישראלי"
    contact.full_name = "משה כהן"
    print(f"{contact.first_name} {contact.last_name}")  # אמור להדפיס "משה כהן"
    print("")

    print("בדיקת תרגיל 4:")
    print(f"2 + 3 = {Calculator.add(2, 3)}")  # אמור להדפיס 5
    print(f"4 * 5 = {Calculator.multiply(4, 5)}")  # אמור להדפיס 20
    print(f"2^3 = {Calculator.power(2, 3)}")  # אמור להדפיס 8
    print(f"7 זוגי? {Calculator.is_even(7)}")  # אמור להדפיס False
    print("")

    print("בדיקת תרגיל 5:")
    library = Library()
    book = Book("מלחמה ושלום", "לב טולסטוי")
    library.add_book(book)
    print(f"הספר זמין? {library.is_book_available(book)}")  # אמור להדפיס True
    library.borrow_book(book, "דן")
    print(f"הספר זמין? {library.is_book_available(book)}")  # אמור להדפיס False
    library.return_book(book)
    print(f"הספר זמין? {library.is_book_available(book)}")  # אמור להדפיס True
    print("")

if __name__ == "__main__":
    test_all()