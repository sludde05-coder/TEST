# availability.py
# Task 3: Manage time slots
# This keeps track of which stations and which athletes are busy in each time slot.
#
# We use a dictionary with two dictionaries inside:
#   availability["stations"][time_slot] = list of stations that are busy in that slot
#   availability["athletes"][time_slot] = list of athlete ids that are busy in that slot
# A time slot is just a number 0, 1, 2, 3 ...


def create_availability():
    availability = {}
    availability["stations"] = {}
    availability["athletes"] = {}
    return availability


def is_station_free(availability, time_slot, station):
    # if nobody has used this time slot yet then the station is free
    if time_slot not in availability["stations"]:
        return True
    if station in availability["stations"][time_slot]:
        return False
    return True


def is_athlete_free(availability, time_slot, athlete_id):
    if time_slot not in availability["athletes"]:
        return True
    if athlete_id in availability["athletes"][time_slot]:
        return False
    return True


def book(availability, time_slot, station, athlete_id):
    # mark the station and the athlete as busy in this time slot
    if time_slot not in availability["stations"]:
        availability["stations"][time_slot] = []
    if time_slot not in availability["athletes"]:
        availability["athletes"][time_slot] = []

    availability["stations"][time_slot].append(station)
    availability["athletes"][time_slot].append(athlete_id)


def count_used_time_slots(availability):
    # returns how many time slots that are used (the last slot number + 1)
    biggest = -1
    for time_slot in availability["stations"]:
        if time_slot > biggest:
            biggest = time_slot
    return biggest + 1
