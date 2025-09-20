# main.py
from myjourn.home import Home
from myjourn.backend import Backend

def main():
    # CLI startup
    Home.greet()

    backend = Backend()
    backend.run()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('=== Program Interrupted ===')
    finally:
        Home.goodbye()