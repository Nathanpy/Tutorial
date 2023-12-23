from datetime import date
from typing import List, Union
from address import Address

class Person:
    def __init__(self, first: str, last: str, dob: date, phone: str, address: Union[Address, List[Address]]) -> None:
        self.first_name: str = first
        self.last_name: str = last
        self.date_of_birth: date = dob
        self.phone: str = phone
        self.addresses: List[Address] = []

        if isinstance(address, Address):
            self.addresses.append(address)
        elif isinstance(address, list):
            for entry in address:
                if not isinstance(entry, Address):
                    raise ValueError("Invalid Address...")
            self.addresses.extend(address)

        else:
            raise ValueError("Invalid Address...")

    def  add_address(self, address) -> None:
        if not isinstance(address, Address):
            raise ValueError("Invalid Address...")
        
        self.addresses.append(address)

    def got_raise(self) -> bool:
        return False