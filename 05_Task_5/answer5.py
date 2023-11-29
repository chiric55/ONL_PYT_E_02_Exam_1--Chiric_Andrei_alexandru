from exam_lib import Book
import re

class EBook(Book):
    def __init__(self, title, author, page_count, size, registration_code):
        super().__init__(title, author, page_count)
        self.__size = size
        self.registration_code = registration_code

    @property
    def registration_code(self):
        return self.__registration_code

    @registration_code.setter
    def registration_code(self, registration_code):
        if self.check_code(registration_code):
            self.__registration_code = registration_code
        else:
            self.__registration_code = None

    @staticmethod
    def check_code(registration_code):
        if isinstance(registration_code, str) and re.match(r'\d{16}', registration_code):
            return True
        else:
            return False