def openprint():
    """
    docstring
    """
    f = open('test.txt')
    print(f.read())
    f.close()
def withprint():
    filename='test.py'
    with open(filename) as file_obj:
        content = file_obj.read()
        print(content)

def main():
    openprint()
    withprint()

if __name__ == "__main__":
    main()
