# read_data.py
# Task 1: Read athlete data
# This file reads athletes.csv and puts every athlete in a dictionary.
# All the athletes are then stored in a list.

# these are all the disciplines in the competition (same names as in the csv file)
DISCIPLINES = ["LJ", "TJ", "HJ", "PV", "100m", "200m", "400m", "800m", "1600m"]


def read_athletes(filename):
    # open the file and read all lines
    infile = open(filename, "r")
    lines = infile.readlines()
    infile.close()

    athletes = []

    # the first line is the header, we use it to know which column is which discipline
    header = lines[0].strip().split(",")

    # start from 1 because line 0 is the header
    for i in range(1, len(lines)):
        line = lines[i].strip()

        # skip empty lines
        if line == "":
            continue

        parts = line.split(",")

        # check that the line has the right number of columns
        if len(parts) != len(header):
            print("Warning: line", i + 1, "has the wrong number of columns, skipping it")
            continue

        athlete = {}
        athlete["id"] = len(athletes) + 1   # some athletes have the same name so we give them a number
        athlete["name"] = parts[0].strip()
        athlete["sex"] = parts[1].strip()
        athlete["country"] = parts[3].strip()

        try:
            athlete["age"] = int(parts[2])
        except ValueError:
            print("Warning: bad age for", athlete["name"], "on line", i + 1)
            athlete["age"] = 0

        # the PRs are in column 4 and forward
        # we only save the disciplines that the athlete takes part in (the field is not empty)
        prs = {}
        for j in range(4, len(header)):
            discipline = header[j].strip()
            value = parts[j].strip()
            if value != "":
                try:
                    prs[discipline] = float(value)
                except ValueError:
                    print("Warning:", athlete["name"], "has a bad PR in", discipline, ":", value)
        athlete["prs"] = prs

        # print(athlete)
        athletes.append(athlete)

    return athletes
