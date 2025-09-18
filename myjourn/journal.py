# journal.py
import json, os

class Journal:
    def __init__(self, year, *, filename=None):
        self.year = str(year)
        self.filename = filename

        # check if file do exists
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as file:
                json.dump({self.year: []}, file, indent=2)

    def add_entry(self, date, title, message, time):
        """Adding entry to journal"""
        # Load existing data
        with open(self.filename, 'r') as file:
            data = json.load(file)

        # Find next ID
        existing_ids = [entry.get('id') for entry in data[self.year]]
        next_id = max(existing_ids, default=0) + 1

        # Create new entry
        new_entry = {
            'id': next_id,
            'date': date,
            'title': title,
            'message': message,
            'time': time
        }

        # Append entry
        data[self.year].append(new_entry)
                
        # Save to file
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=2)

    def rm_entry(self, rm_id):
        """Remove user entry"""
        # Load existing file
        with open(self.filename, 'r') as file:
            data = json.load(file)

        # Filter id's
        original_count = len(data[self.year])
        data[self.year] = [entry for entry in data[self.year] if entry.get('id') != rm_id]

        # if no match id / nothing to remove
        if len(data[self.year]) == original_count:
            print('No id matched.')
            return
        
        # update file
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=2)

        print(f'Removed entry (ID: {rm_id})')

    @staticmethod
    def display_entry(year, filename, date):
        """Search entries"""
        # Load file
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            print(f'No file exists for year {year}.')
            return

        # initial state
        found = False

        for entry in data[year]:
            
            # display details
            if entry.get('date') == date:
                if found:
                    print('-------------------------')

                print(f'ID: {entry.get('id')}')
                print(f'Title: {entry.get('title')}')
                print(f'Message: {entry.get('message')}')

                found = True

        if not found:
            print('No entries found on this date')
        return found