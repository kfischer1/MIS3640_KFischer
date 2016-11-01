# file one.py
def func():
    print("func() in one.py")


def main():
    print("Main function in one.py")

if __name__ == "__main__":              #underscores allows anything above to be run in other code, not below this point
    main()
    print("one.py is being run directly")
else:
    print("one.py is being imported into another module")
