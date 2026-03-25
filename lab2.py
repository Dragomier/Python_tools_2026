# Data structures
from typing import Dict, List
from collections import defaultdict
class PhoneBook:
    def __init__(self):
        self.phonebook: Dict[str, List[str]] = defaultdict(list)
        print("I created new Phonebook")

    def add_phone(self, user, phone):
        self.phonebook[user].append(phone)

    def give_numbers(self, user):
        print(self.phonebook[user] if user in self.phonebook else [])

    def remove_numbers(self, user, number):
        self.phonebook[user].remove(number)

    def print_phonebook(self):
        print(self.phonebook)

new_book = PhoneBook()
new_book.add_phone("", "test")
new_book.give_numbers("test")
new_book.give_numbers("")
new_book.print_phonebook()

