# main.py
from module.journal import Journal
from module.user import User
from module.filename import Filename

def main():
    title = User.entry_title('Entry Title: ')
    message = User.entry_message('Entry Message: ')
    year, date, time = User.time()

    filename = Filename.test_file(year)
    my = Journal(year, filename=filename)

    my.add_entry(date, title, message, time)

if __name__ == '__main__':
    main()