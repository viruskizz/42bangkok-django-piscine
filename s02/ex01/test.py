from intern import Intern

if __name__ == '__main__':
    noname = Intern()
    mark = Intern("Mark")
    print(noname)
    print(mark)
    try:
        result = mark.make_coffee()
        print(result)
        noname.work()
    except Exception as e:
        print("Error:", e)
