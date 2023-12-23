from datetime import date
from typing import List

from person import Person
from course import Course

class Professor(Person):
    get_raise: bool

    def __init__(self, first: str, last: str, dob: date, phone: str, address: str, salary):
        super().__init__(first, last, dob, phone, address)
        self.salary: float = salary
        self.courses: List[Course] = []
        self.get_raise: bool = False

    def check_for_raise(self) -> None:
        if len(self.courses) >= 4 and not self.got_raise:
            self.salary += 20000
            self.got_raise = True

    def add_course(self, course: Course) -> None:
        if not isinstance(course, Course):
            raise ValueError("Invalid Course...")
        
        self.courses.append(course)
        