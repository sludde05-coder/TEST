# schedule.py
# Task 5: Find available placements
# For every event we look for a time slot and a station where both the
# station and the athlete are free. We use the functions from stations.py
# and availability.py.
#
# The algorithm is simple:
#   start at time slot 0
#   try every station that supports the discipline
#   if no station works (or the athlete is busy) go to the next time slot

from stations import get_stations_for_discipline
from availability import create_availability, is_station_free, is_athlete_free, book


def find_place(event, stations, availability):
    possible_stations = get_stations_for_discipline(stations, event["discipline"])

    # if there is no station for this discipline we can not schedule it
    if len(possible_stations) == 0:
        print("Error: no station for discipline", event["discipline"])
        return -1, ""

    time_slot = 0
    found = False
    found_station = ""

    while found == False:
        # first check if the athlete is free, otherwise there is no point checking the stations
        if is_athlete_free(availability, time_slot, event["athlete_id"]):
            for station in possible_stations:
                if found == False and is_station_free(availability, time_slot, station):
                    found = True
                    found_station = station

        if found == False:
            time_slot = time_slot + 1

    return time_slot, found_station


def make_schedule(events, stations):
    availability = create_availability()
    schedule = []

    for event in events:
        time_slot, station = find_place(event, stations, availability)

        if time_slot == -1:
            print("Could not schedule", event["name"], "in", event["discipline"])
        else:
            book(availability, time_slot, station, event["athlete_id"])

            # save the assignment
            assignment = {}
            assignment["time_slot"] = time_slot
            assignment["station"] = station
            assignment["discipline"] = event["discipline"]
            assignment["athlete_id"] = event["athlete_id"]
            assignment["name"] = event["name"]
            assignment["country"] = event["country"]
            assignment["pr"] = event["pr"]
            schedule.append(assignment)

    return schedule, availability
