# write_output.py
# Task 6: Generate output
# Writes the finished schedule to a csv file.
# The rows are sorted by time slot and then by station.


def write_schedule(filename, schedule, station_names):
    outfile = open(filename, "w")

    # header line
    print("TimeSlot,Station,Discipline,AthleteID,Athlete,Country,PR", file=outfile)

    # find the last time slot
    last_slot = 0
    for assignment in schedule:
        if assignment["time_slot"] > last_slot:
            last_slot = assignment["time_slot"]

    # go through every time slot and every station so the file comes out sorted
    rows = 0
    for time_slot in range(last_slot + 1):
        for station in station_names:
            for assignment in schedule:
                if assignment["time_slot"] == time_slot and assignment["station"] == station:
                    line = str(time_slot) + "," + station + "," + assignment["discipline"] + ","
                    line = line + str(assignment["athlete_id"]) + "," + assignment["name"] + ","
                    line = line + assignment["country"] + "," + str(assignment["pr"])
                    print(line, file=outfile)
                    rows = rows + 1

    outfile.close()
    return rows
