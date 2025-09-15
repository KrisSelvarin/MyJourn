# main.py
from myjourn.home import Home

def main():
    # CLI startup
    Home.greet()
    Home.menu()

if __name__ == '__main__':
    main()