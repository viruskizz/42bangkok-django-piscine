import sys
# import antigravity
from antigravity import geohash

def geohashing(lat: str, long: str):
    datedow = b'2005-05-26-10458.68' ## convert string date of downjon stock start to byte
    return geohash(lat, long, datedow)

def is_float(num: str):
    try:
        float(num)
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('input only lat and long')
        sys.exit(1)
    if not is_float(sys.argv[1]) or not is_float(sys.argv[2]):
        print('Latitude or Longtitud is not float value')
        sys.exit(1)
    lat = float(sys.argv[1])
    long = float(sys.argv[2])
    if lat < -90.0 or lat > 90.0:
        print(f'Latitude {lat} is not in range -90.0 to 90.0')
    if long < -180.0 or lat > 180.0:
        print(f'Longitude {lat} is not in range -90.0 to 90.0')
    hash = geohashing(lat, long)
    print(f'Geohash: {hash}')
