# stations.py
# Task 2: Create station system
# Here we define all the stations in the stadium and which disciplines
# can be done on each station.


def create_stations():
    # the key is the station name and the value is a list of disciplines
    stations = {}
    stations["LJ1"] = ["LJ", "TJ"]      # long jump and triple jump share the runways
    stations["LJ2"] = ["LJ", "TJ"]
    stations["HJ1"] = ["HJ"]
    stations["HJ2"] = ["HJ"]
    stations["PV1"] = ["PV"]            # only one pole vault
    stations["TRACK"] = ["100m", "200m", "400m", "800m", "1600m"]   # all running events
    return stations


def get_station_names(stations):
    # returns a list with the names of all stations
    names = []
    for name in stations:
        names.append(name)
    return names


def get_stations_for_discipline(stations, discipline):
    # returns a list of the stations that can be used for a discipline
    # for example "TJ" gives ["LJ1", "LJ2"]
    result = []
    for name in stations:
        if discipline in stations[name]:
            result.append(name)
    return result


def station_supports(stations, station, discipline):
    # returns True if the discipline can be done on the station
    if station not in stations:
        return False
    if discipline in stations[station]:
        return True
    else:
        return False
