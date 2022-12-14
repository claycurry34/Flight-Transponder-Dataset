from math import ceil, floor, pi, cos
from typing import List
from logging import DEBUG, debug


class Airspace():
    def __init__(self, tiles):
        self.lat1 = 0
        self.lon1 = 0
        self.lat2 = 0
        self.lon2 = 0
        self.tiles: List[int] = tiles
    

# number of lat, long divisions per tile
globeIndexGrid = 3
globeIndexSpecialTiles = {}
globeIndexCached = {}


def globe_indexes(region) -> List[str]:
    """ accepts a Region, returns indexes of all "grid tiles" covering this region."""
    # Distances are measured in miles.
    # Longitudes and latitudes are measured in degrees.
    # Earth is assumed to be perfectly spherical.

    x1 = floor(region.lon1)
    x2 = ceil(region.lon2)
    y1 = floor(region.lat1)
    y2 = ceil(region.lat2)

    x2 = x2 if x2 < 179 else 179
    x1 = x1 if x1 > -179 else -179
    y2 = y2 if y2 < 90 else 90
    y1 = y1 if y1 > -90 else -90

    indexes = []
    grid = globeIndexGrid
    x3 = x2 if x1 < x2 else 199
    count = 0

    for lon in range(x1, x3, grid):
        if x1 > x2 and lon > 180:
            lon -= 360
            x3 = x2

        if lon > x3:
            lon = x3 + 0.01
        count += 1
        if count > 360 / grid:
            print(f"globeIndexes fail, lon: {lon}")

        count2 = 0
        for lat in range(y1, y2, grid):
            count2 += 1
            if (count2 > 180 / grid):
                print("globeIndexes fail, lon: " + lon + ", lat: " + lat)
                break
            if (lat > y2):
                lat = y2 + 0.01
            if (lat > 90):
                break
            index = globe_index(lat, lon)
            debug(f'{lat} {lon} {index}')
            if index not in indexes:
                indexes.append(index)

    return indexes


def globe_index(lat, lon) -> int:
    grid = globeIndexGrid

    lat = grid * floor((lat + 90) / grid) - 90
    lon = grid * floor((lon + 180) / grid) - 180

    i = floor((lat + 90) / grid)
    j = floor((lon + 180) / grid)

    lat_multiplier = floor(360 / grid + 1)
    defaultIndex = i * lat_multiplier + j + 1000
    index = -1
    try:
        index = globeIndexCached[f"{defaultIndex}"]
        return index

    except KeyError:
        # not yet in lookup, check special tiles
        for i in range(len(globeIndexSpecialTiles)):
            tile = globeIndexSpecialTiles[i]
            if (lat >= tile[0] and lat < tile[2]) and ((tile[1] < tile[3] and lon >= tile[1] and lon < tile[3]) or tile[1] > tile[3] and (lon >= tile[1] or lon < tile[3])):
                globeIndexCached[f"{defaultIndex}"] = index = i
        if index == -1:
            globeIndexCached[f"{defaultIndex}"] = index = defaultIndex
    debug(
        f'lat: ({lat}, {lat + grid}) lon: ({lon}, {lon + grid}) index: {index}')
    return index


if __name__ == "__main__":
    air_sp = Airspace(35.222569, -97.439476, 200)
    print(air_sp.tiles)
