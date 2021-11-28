from datetime import date
import classes.Student as Stud
import classes.Employee as Emp
import classes.Book as Bk


class Order:
    employee: Emp.Employee
    student: Stud.Student
    books: Bk.Book
    order_date: date

    def __init__(self, employee: Emp.Employee, student: Stud.Student, books: Bk.Book, order_date: date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return f'Dt zam.:\nSTUD\n{self.student}\nBOOK\n{self.books}\nDt zam.: {self.order_date}\nEMP\n{self.employee}'
