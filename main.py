import sys
from cw import MyApp

def main():
    a = MyApp()
    sys.exit(a.exec())

if __name__ == "__main__":
    main()