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

def getCityFromState(capital_map, find):
    for state, city in capital_map.items():
        if state.lower() == find.lower():
            return city

def getStateFromCity(capital_map, find):
    for state, city in capital_map.items():
        if city.lower() == find.lower():
            return state

def map_states_cities():
    map = {}
    for state, short in states.items():
        city = capital_cities[short]
        map[state] = city
    return map

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(0)
    input = sys.argv[1]
    inputs = [s.strip() for s in input.split(",")]
    capital_map = map_states_cities()
    for s in inputs:
        if not s:
            continue
        state = getStateFromCity(capital_map, s)
        city = getCityFromState(capital_map, s)
        if state:
            print(f'{s.capitalize()} is the capital of {state}')
        elif city:
            print(f'{city} is a capital of {s}')
        else:
            print(f'{s} is neither a capital city nor a state')