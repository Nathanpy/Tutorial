from datetime import date
from typing import List

from person import Person
from enroll import Enroll

class Student(Person):
    def __init__(self, first: str, last: str, dob: date, phone: str, address: str, international: bool =False):
        super().__init__(first, last, dob, phone, address)
        self.international: bool = international
        self.enrolled: List[Enroll] = []

    def add_enrollment(self, enroll) -> None:
        if not isinstance(enroll, Enroll):
            raise ValueError("Enrollent must be of Enroll type")
        
        self.enrolled.append(enroll)

    def is_on_probation(self) -> bool:
        return False
    
    def is_part_time(self) -> bool:
        return len(self.enrolled) <= 3
    
    
            