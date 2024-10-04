if __name__ == '__main__':
    filename = "numbers.txt"
    f = open(filename, "r")
    lines = f.readlines()
    f.close()
    numbers = lines[0].strip().split(",")
    for x in numbers:
        print(x)