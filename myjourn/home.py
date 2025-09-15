# home.py
# for CLI

class Home:
    
    @staticmethod
    def greet():
        """CLI Greeting"""
        print('=== MyJournal ===')
        print('(Personal Project by KrisSelvarin)')

    @staticmethod
    def menu():
        """CLI Menu"""
        menu_list = ['Add Entry', 'Remove Entry', 'Search', 'Exit']

        for i, option in enumerate(menu_list, start=1):
            print(f'[{i}] {option}')

    @staticmethod
    def run():
        """Run backend"""
        pass