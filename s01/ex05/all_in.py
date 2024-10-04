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
        if val.lower() == input.lower():
            return key

def getStateFromCity(city):
    st = getKeyFromVal(city, capital_cities)
    if not st:
        return
    state = getKeyFromVal(st, states)
    return state

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(0)
    input = sys.argv[1]
    inputs = [s.strip() for s in input.split(",")]
    # inputs.reverse()
    for str in inputs:
        if not str:
            continue
        state = getStateFromCity(str)
        if state:
            print(f'{str.capitalize()} is the capital of {state}')
        elif str.title() not in states:
            print(f'{str} is neither a capital city nor a state')