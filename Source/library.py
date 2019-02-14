class Public:
    def __init__(self):
        self.fullname = input("Enter your full Name:")
        self.email = input("Enter school email address:")
    def display(self):
        print("Name: ", self.fullname)
        print("Email: ", self.email)

#creating a class to display student details.
class Student(Public):
    StudentCount = 0
    def __init__(self):
        Public.__init__(self)
        self.student_id = input("Enter student ID:")
        Student.StudentCount +=1
    def displayCount(self):
        print("Total number of Students:", Student.StudentCount)
    def display(self):
        print( "Details of students are:")
        Public.display(self)
        print("Student Id: ",self.student_id)

#creating a class to display librarian details
class Librarian(Public):
    StudentCount = 0
    def __init__(self):
        super().__init__()
        self.employee_id = input("Enter your EmployeeID:")
    def display(self):
        print("Details of employee are:")
        Public.display(self)
        print("Employee Id: ",self.employee_id)

#creating a class to display the details of the book
class Book():
    def __init__(self):
        self.book_name = input("Enter Book name: ")
        self.author = input("Enter Author name: ")
        self.book_id = input("Enter Book ID: ")
    def display(self):
        print("Details of the book are")
        print("Book_Name: ", self.book_name)
        print("Author: ", self.author)
        print("Book_ID: ", self.book_id)

#creating a class to display the details of the book that is being borrowed
class Borrow_Book(Student,Book):
    def __init__(self):
        print("Enter details to borrow Book")
        Student.__init__(self)
        Book.__init__(self)
    def display(self):
        print("Borrowed Book Details:")
        Student.display(self)
        Book.display(self)

stu = Student()
stu.display()
lib = Librarian()
lib.display()
bk = Book()
bk.display()
bb = Borrow_Book()
bb.display()


