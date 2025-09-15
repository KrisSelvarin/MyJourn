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

    def rm_entry(self):
        """Remove user entry"""
        # Load existing file
        with open(self.filename, 'r') as file:
            data = json.load(file)

        pass

    def display_entry():
        """Displays all entries"""
        pass