from datetime import date
from typing import List

from person import Person
from course import Course

class Professor(Person):
    def __init__(self, first: str, last: str, dob: date, phone: str, address: str, salary):
        super().__init__(first, last, dob, phone, address)
        self.salary = salary
        self.courses: List[Course] = []

    def check_for_raise(self):
        if len(self.courses) >= 4 and not self.got_raise:
            self.salary += 20000
            self.got_raise = True

    def add_course(self, course):
        if not isinstance(self, Course):
            raise ValueError("Invalid Course...")
        
        self.courses.append(course)
        