def file_read():
    my_file = open("sheet.txt", "r")
    print(my_file.read())
    my_file.close()


def new_file():
    my_file = open("sheet.txt", "w")
    my_file.write("So it goes - Vonnegut\n")
    """my_file.seek(0)
    print(my_file.read())
    my_file.close()"""


def file_append():
    my_file = open("sheet.txt", "a")
    my_file.write("If you try you can fail.\n")
    """my_file.seek(0)
    print(my_file.read())
    my_file.close()"""


def letter_count(p):
    my_file = open("sheet.txt", "r")
    count = 0
    for e in my_file.read():
        if e.lower() == p:
            count += 1
    my_file.close()
    print(count)


def list_file():
    my_file = open("sheet.txt", "w")
    shoppings = ["braad\n", "orang\n", "melk\n", "cheez\n", "soap shoes\n"]
    my_file.writelines(shoppings)


new_file()
file_append()
letter_count("a")
list_file()
file_read()
