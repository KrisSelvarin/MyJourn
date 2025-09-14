# user.py
from datetime import datetime

class User:
    
    @staticmethod
    def entry_message(prompt):
        """Gets user entry message"""
        return input(prompt)
    
    @staticmethod
    def entry_title(prompt):
        """Gets user entry title"""
        return input(prompt).title()
    
    @staticmethod
    def time():
        now = datetime.now()
        year = now.strftime("%Y")
        date = now.strftime("%b-%d")
        time = now.strftime("%H%MH")

        return year, date, time