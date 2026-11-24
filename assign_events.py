# assign_events.py
# Task 4: Assign athletes to events
# Goes through all athletes and all their disciplines and makes one "event"
# for every discipline the athlete wants to compete in.
# An event is a dictionary with the athlete and the discipline.

from read_data import DISCIPLINES


def create_events(athletes):
    events = []

    for athlete in athletes:
        # go through the disciplines in the same order as in the csv file
        for discipline in DISCIPLINES:
            if discipline in athlete["prs"]:
                event = {}
                event["athlete_id"] = athlete["id"]
                event["name"] = athlete["name"]
                event["country"] = athlete["country"]
                event["discipline"] = discipline
                event["pr"] = athlete["prs"][discipline]
                events.append(event)

    return events


def count_events_per_discipline(events):
    # counts how many athletes there are in each discipline, used for printing info
    counts = {}
    for discipline in DISCIPLINES:
        counts[discipline] = 0
    for event in events:
        counts[event["discipline"]] = counts[event["discipline"]] + 1
    return counts
