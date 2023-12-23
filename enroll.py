from course import Course
from student import Student
from datetime import datetime
from typing import Optional

class Enroll:
    def __init__(self, student: Student, course: Course) -> None:
        if not isinstance(student, Student):
            raise ValueError("Invalid student...")
        
        if not isinstance(course, Course):
            raise ValueError("Invalid course...")
        
        self.student = student
        self.course = course
        self.grade: Optional[float] = None
        self.date: datetime = datetime.now()

    def set_grade(self, grade: float) -> None:
        self.grade = grade