# מבחן תרגול בתכנות מונחה עצמים
# ===============================

"""
הוראות למבחן:
- השלימו את הקוד החסר במקומות המסומנים ב-pass
- שימו לב להערות המנחות בכל שאלה
- הקפידו על שימוש נכון במילות המפתח super(), self, cls
- כתבו קוד יעיל ונקי
"""


# שאלה 1
# ------
# השלימו את המתודה __init__ במחלקה Book
class Book:
    total_books = 0  # שדה של המחלקה

    def __init__(self, title, author):
        # צריך להוסיף את השדות title, author ולהגדיל את total_books ב-1
        self.title = title
        self.author = author
        Book.total_books += 1

book = Book("", "")
# print(Book.total_books)

# שאלה 2
# ------
# השלימו את המתודה __str__ שמחזירה מחרוזת בפורמט: "Title by Author"
class Magazine:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

magazine = Magazine("News Post","John Smith")
# print(magazine)

# שאלה 3
# ------
# השלימו את המתודה add_chapter שמוסיפה פרק חדש לספר
class Novel(Book):
    def __init__(self, title, author):
        super().__init__(title, author)
        self.chapters = []

    def add_chapter(self, chapter_name):
        # צריך להוסיף את הפרק לרשימת הפרקים
        self.chapters.append(chapter_name)

novel = Novel("", "")
novel.add_chapter("Chapter A")
novel.add_chapter("Chapter B")
novel.add_chapter("Chapter C")
# print(novel.chapters)


# שאלה 4
# ------
# השלימו את המתודה __init__ במחלקה Library שמקבלת שם ורשימת ספרים
class Library:
    def __init__(self, name, books=None):
        # צריך לאתחל את שם הספרייה ואת רשימת הספרים (אם לא התקבלה רשימה, צריך ליצור רשימה ריקה)
        self.name = name
        if books == None:
            self.books = []
        else:
            self.books = books

library = Library("Kod_code", ["Math", "English"])
# print(library.books)

# שאלה 5
# ------
# השלימו את המתודה הסטטית calculate_price שמחשבת מחיר ספר לפי מספר העמודים
class TextBook(Book):
    @staticmethod
    def calculate_price(pages):
        # צריך להחזיר מחיר לפי החישוב: מספר עמודים * 0.5 + 20
        return pages * 0.5 + 20

pages_number = 200
price = TextBook.calculate_price(pages_number)
# print(price)

# שאלה 6
# ------
# השלימו את המתודה __repr__ שמחזירה ייצוג מחרוזתי של האובייקט
class Author:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def __repr__(self):
        # צריך להחזיר: "Author(name='שם המחבר', birth_year=שנת לידה)"
        return f"Auther(name = '{self.name}', birth_year = '{self.birth_year}')"

auther = Author("David", 1970)
# print(auther)


# שאלה 7
# ------
# השלימו את המתודה add_book שמוסיפה ספר למחבר
class ModernAuthor(Author):
    def __init__(self, name, birth_year):
        super().__init__(name, birth_year)
        self.books = []

    def add_book(self, title):
        # צריך ליצור אובייקט Book חדש עם השם שהתקבל והמחבר הנוכחי, ולהוסיף אותו לרשימת הספרים
        book1 = Book(title, self.name)
        self.books.append(book1.title)

modern_auther = ModernAuthor("Moshe", 1990)
modern_auther.add_book("Philosophy")
modern_auther.add_book("History")
# print(modern_auther.books)


# שאלה 8
# ------
# השלימו את המתודה __init__ במחלקה שיורשת משתי מחלקות
class OnlineBook(Book, Magazine):
    def __init__(self, title, author, url):
        # צריך לקרוא ל-__init__ של שתי המחלקות ולהוסיף את השדה url
        Book.__init__(self, title, author)
        Magazine.__init__(self, title, author)
        self.url = url
o = OnlineBook("a","b","c")
# print(o.title, o.author, o.url)


# שאלה 9
# ------
# השלימו את המתודה add_review שמוסיפה ביקורת לספר
class ReviewedBook(Book):
    def __init__(self, title, author):
        super().__init__(title, author)
        self.reviews = []

    def add_review(self, reviewer_name, rating):
        # צריך ליצור מילון עם שם המבקר והדירוג ולהוסיף אותו לרשימת הביקורות
        review = {reviewer_name:rating}
        self.reviews.append(review)

reviewer_book = ReviewedBook("Science", "Einstein")
reviewer_book.add_review("David", 5)
reviewer_book.add_review("Avi", 3)
# print(reviewer_book.reviews)


# שאלה 10
# -------
# השלימו את המתודה get_average_rating שמחשבת ממוצע דירוגים
class RatedBook(ReviewedBook):
    @staticmethod
    def get_average_rating(reviews):
        # צריך לחשב את ממוצע הדירוגים מתוך רשימת הביקורות
        sum_rates = 0
        for review in reviews:
            for name in review:
                sum_rates += review[name]
        return sum_rates/len(reviews)

print(RatedBook.get_average_rating(reviewer_book.reviews))

# שאלה 11
# -------
# השלימו את המתודה __init__ במחלקה BookSeries שמכילה רשימת ספרים
class BookSeries:
    def __init__(self, series_name, first_book):
        # צריך לאתחל את שם הסדרה, ליצור רשימת ספרים ולהוסיף את הספר הראשון
        self.series_name = series_name
        self.first_book = first_book
        self.series = [first_book]

book_series = BookSeries("History", "Rome")
# print(book_series.series)

# שאלה 12
# -------
# השלימו את המתודה add_related_book שמוסיפה ספר קשור
class ReferenceBook(Book):
    def __init__(self, title, author):
        super().__init__(title, author)
        self.related_books = []

    def add_related_book(self, other_book):
        # צריך לבדוק שהספר שמתקבל הוא מסוג Book ולהוסיף אותו לרשימת הספרים הקשורים
        if type(other_book) == Book:
            self.related_books.append(other_book.title)
        else:
            print("This is not a Book!")

book2 = ReferenceBook("USA history", "King")
book3 = Book("NY history", "Smith")
book4 = Book("NJ history", "King")

book2.add_related_book(book3)
book2.add_related_book(book4)
print(book2.related_books)