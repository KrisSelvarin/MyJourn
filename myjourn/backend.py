# backend.py
# calls logic classes
from myjourn.journal import Journal
from myjourn.filename import Filename
from datetime import datetime
import re

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

    @staticmethod
    def search_entry():
        """Handles entry search"""

        # User input
        date = input('Date (MM-DD-YYYY): ')
        pattern = r'(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])-(\d{4})'
        reg = re.match(pattern, date)

        # default values
        new_date = None
        year = None

        if reg:
            try:
                # validate date
                datetime.strptime(date, '%m-%d-%Y')

                # capture month/day/year in regex
                month = reg.group(1)
                day = reg.group(2)
                year = reg.group(3)

                # create datetime object
                d = f'{month}-{day}-{year}'
                date_obj = datetime.strptime(d, '%m-%d-%Y')

                # format datetime object
                new_date = date_obj.strftime('%b-%d')

            except ValueError:
                print('Invalid Date!')
        else:
            print('Wrong Format!')
        
        if year and new_date:
            filename = Filename.filename(year)
            Journal.display_entry(year, filename, new_date)

    @staticmethod
    def close_program():
        """Just closes program"""
        exit()