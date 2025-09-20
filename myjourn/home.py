# home.py
class Home:
    
    @staticmethod
    def greet():
        """CLI Greeting"""
        print('=== MyJournal ===')
        print('(Personal Project by KrisSelvarin)')
        print('----------------------------------')
        print('Simple CLI journal app for practice.')
        print('Data is stored in JSON files per year.')
        print('Note: This is a learning project, not for production use.')
        print('----------------------------------\n')

    @staticmethod
    def goodbye():
        """Program Exit Message"""
        print('\n=== Program Closed ===')
        print('Thanks for using MyJournal!')
        print('Keep coding, keep learning')
