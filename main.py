# main.py
# Track and field competition scheduler
# Run with:  python main.py
#
# It reads athletes.csv, makes a schedule and writes it to schedule.csv

from read_data import read_athletes
from stations import create_stations, get_station_names
from assign_events import create_events, count_events_per_discipline
from schedule import make_schedule
from availability import count_used_time_slots
from write_output import write_schedule
from check_schedule import check_schedule
from visual_schedule import show_schedule

INPUT_FILE = "athletes.csv"
OUTPUT_FILE = "schedule.csv"


def main():
    print("=== Track and Field Scheduler ===")
    print()

    # step 1: read the athletes
    athletes = read_athletes(INPUT_FILE)
    print("Read", len(athletes), "athletes from", INPUT_FILE)

    # step 2: make the stations
    stations = create_stations()
    station_names = get_station_names(stations)
    print("Stations:", station_names)

    # step 3: make one event for every discipline every athlete is in
    events = create_events(athletes)
    print("Number of events to schedule:", len(events))
    counts = count_events_per_discipline(events)
    for discipline in counts:
        print("   ", discipline, ":", counts[discipline])

    # step 4: find a time slot and station for every event
    schedule, availability = make_schedule(events, stations)
    print("Scheduled", len(schedule), "events")
    print("Time slots used:", count_used_time_slots(availability))

    # step 5: write it to the file
    rows = write_schedule(OUTPUT_FILE, schedule, station_names)
    print("Wrote", rows, "rows to", OUTPUT_FILE)

    # step 6: check that the schedule follows the rules
    print()
    print("Checking the schedule...")
    errors = check_schedule(OUTPUT_FILE, athletes, stations)
    if errors == 0:
        print("The schedule is OK, no errors found!")
    else:
        print("Found", errors, "errors in the schedule")

    # step 7: show the schedule in a window
    print()
    print("Opening the schedule window... (close the window to quit)")
    show_schedule(schedule, station_names)


main()
