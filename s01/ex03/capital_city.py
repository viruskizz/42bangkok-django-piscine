import sys

states = {
    "Oregon" : "OR",
    "Alabama" : "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO"
}

capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
}

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(0)
    input = sys.argv[1]
    if input not in states:
        print("Unknown state")
        exit(0)
    key = states[input]
    print(capital_cities[key])
