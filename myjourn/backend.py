# backend.py
# calls logic classes
from myjourn.journal import Journal
from myjourn.filename import Filename
from myjourn.home import Home
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
        time = datetime.now().strftime('%H%M') + 'H'    # 24H format (e.g. 1830H)

        self.journal.add_entry(date, title, message, time)

    @staticmethod
    def rm_entry():
        """Handles removing entry"""

        # gets filename, year and if theres an entry
        filename, year, n_entry = Backend.search_entry()

        # if theres an available entry to be removed
        if n_entry:
            rm_id = int(input('Entry ID to remove: '))
            journal = Journal(year, filename=filename)
            journal.rm_entry(rm_id)
        
    @staticmethod
    def search_entry():
        """Handles entry search"""

        # User input
        date = input('Date (MM-DD-YYYY): ')
        pattern = r'(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])-(\d{4})'

        # default values
        new_date = None
        year = None

        if not re.match(pattern, date):
            print('Wrong Format!')
            return None

        try:
            # validate date
            date_obj = datetime.strptime(date, '%m-%d-%Y')

        except ValueError:
                print('Invalid Date!')
                return None
        
        # format datetimeobj
        year = date_obj.strftime('%Y')
        new_date = date_obj.strftime('%b-%d')
        filename = Filename.filename(year)
        
        n_entry = Journal.display_entry(year, filename, new_date)
        return filename, year, n_entry
    
    @staticmethod
    def close_program():
        """Just closes the program"""
        Home.goodbye()
        exit()
    
    @staticmethod
    def menu():
        """CLI Menu"""
        print('=== Main Menu ===')
        menu_list = ['Add Entry', 'Remove Entry', 'Search', 'Exit']

        for i, option in enumerate(menu_list, start=1):
            print(f'[{i}] {option}')

        while True:
            try:
                select = int(input('Selection: ').strip())
                if 1 <= select <= len(menu_list):
                    return select
                else:
                    print(f'Enter number between 1-{len(menu_list)}.')
            except ValueError:
                print('Enter valid number.')

    def run(self):
        """Main Loop"""
        
        # Actions dictionary
        actions = {
            1: self.add_entry,
            2: self.rm_entry,
            3: self.search_entry,
            4: self.close_program,

        }

        while True:
            select = self.menu()
            action = actions.get(select)
            if action:
                action()