# backend.py
# calls logic classes
from journal import Journal
from filename import Filename
from datetime import datetime

class Backend:
    def __init__(self):
        year = datetime.now().strftime('%Y')
        filename = Filename.filename(year)
        self.journal = Journal(year, filename=filename)

    def add_entry(self):
        """Handles adding entries"""
        # User input
        title = input('Entry Title: ')
        message = input('Entry Message: ')

        # Time stamps
        date = datetime.now().strftime('%b-%d')         # format to Sep-14
        time = datetime.now().strftime('%H%MH')         # 24H format (e.g. 1830H)

        self.journal.add_entry(date, title, message, time)

    def rm_entry(self):
        """Handles removing entry"""
        # TODO: implement remove logic using IDs
        pass

    def search_entry(self):
        """Handles entry search"""
        # TODO: implement search logic with filters (by date on what year)
        pass

    @staticmethod
    def close_program():
        """Just closes program"""
        exit()