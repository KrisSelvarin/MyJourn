# main.py
from myjourn.journal import Journal
from myjourn.user import User
from myjourn.filename import Filename

def main():
    title = User.entry_title('Entry Title: ')
    message = User.entry_message('Entry Message: ')
    year, date, time = User.time()

    filename = Filename.filename(year)
    my = Journal(year, filename=filename)

    my.add_entry(date, title, message, time)

if __name__ == '__main__':
    main()