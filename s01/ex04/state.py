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

def getKeyFromVal(input, obj):
    for key, val in obj.items():
        if val == input:
            return key

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(0)
    input = sys.argv[1]
    st = getKeyFromVal(input, capital_cities)
    if not st:
        print("Unknown capital city")
        exit(0)
    state = getKeyFromVal(st, states)
    print(state)