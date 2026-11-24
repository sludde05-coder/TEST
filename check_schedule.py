# check_schedule.py
# Our own checker. It reads schedule.csv back in and checks that the rules are followed:
#   1. an athlete is only in one event per time slot
#   2. a station only has one athlete per time slot
#   3. every discipline is on a station that supports it
#   4. every athlete got all of their disciplines scheduled

from stations import station_supports


def check_schedule(filename, athletes, stations):
    infile = open(filename, "r")
    lines = infile.readlines()
    infile.close()

    errors = 0
    used_athletes = []      # list of (time slot, athlete id)
    used_stations = []      # list of (time slot, station)
    scheduled = []          # list of (athlete id, discipline)

    # skip the header line
    for i in range(1, len(lines)):
        parts = lines[i].strip().split(",")
        time_slot = int(parts[0])
        station = parts[1]
        discipline = parts[2]
        athlete_id = int(parts[3])

        # rule 1
        if (time_slot, athlete_id) in used_athletes:
            print("ERROR: athlete", athlete_id, "has two events in time slot", time_slot)
            errors = errors + 1
        used_athletes.append((time_slot, athlete_id))

        # rule 2
        if (time_slot, station) in used_stations:
            print("ERROR: station", station, "is used two times in time slot", time_slot)
            errors = errors + 1
        used_stations.append((time_slot, station))

        # rule 3
        if station_supports(stations, station, discipline) == False:
            print("ERROR:", discipline, "can not be done at", station)
            errors = errors + 1

        scheduled.append((athlete_id, discipline))

    # rule 4
    for athlete in athletes:
        for discipline in athlete["prs"]:
            if (athlete["id"], discipline) not in scheduled:
                print("ERROR:", athlete["name"], "is missing", discipline)
                errors = errors + 1

    return errors
