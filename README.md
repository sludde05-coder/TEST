# Track and Field Scheduler

Course project: a Python program that makes a schedule for a track and field competition.
It reads `athletes.csv` and writes `schedule.csv`.

## Tasks

1	Read athlete data	Read athletes.csv, extract athlete information and PRs, store athletes in lists/dictionaries.	read_data.py


2	Create station system	Define stations (LJ1, LJ2, HJ1, HJ2, PV1, TRACK) and which disciplines they support.	stations.py


3	Manage time slots	Create the system that tracks available stations and whether athletes are already occupied in a time slot.	availability.py


4	Assign athletes to events	Develop the logic that goes through athletes and their disciplines and creates event assignments.	assign_events.py


5	Find available placements	Develop the logic that finds a suitable station and time slot for each event, using Member 2 and 3's systems.	schedule.py


6	Generate output	Collect all assignments and write the finished schedule into schedule.csv.	write_output.py


## How to run

You need Python 3. Go to the project folder and run:

```
python main.py
```

The program prints some info about the athletes and events, writes `schedule.csv`
and then checks the schedule with our checker.

## Input format

The input file is `athletes.csv` (the name is written in `main.py`).
The first line is the header:

```
Name,Sex,Age,Country,LJ,TJ,HJ,PV,100m,200m,400m,800m,1600m
```

Every line after that is one athlete. If the athlete competes in a discipline the field has
their PR (metres for jumps, seconds for runs). If the field is empty they do not compete in it.
Empty lines are skipped. Lines with the wrong number of columns, and PRs that are not numbers,
are skipped with a warning.

## Output format

The output file is `schedule.csv`. Example:

```
TimeSlot,Station,Discipline,AthleteID,Athlete,Country,PR
0,LJ1,LJ,2,Maria Karlsson,UK,5.9
0,LJ2,TJ,3,Amelia Brown,Germany,15.74
0,HJ1,HJ,1,Elijah Smith,Spain,1.49
```

- **TimeSlot** - the time slot number (0, 1, 2, ...)
- **Station** - LJ1, LJ2, HJ1, HJ2, PV1 or TRACK
- **Discipline** - the discipline code from the input file
- **AthleteID** - the athlete's number (the order in the input file). We added this because some athletes have the same name (for example there are two Maria Karlsson from the UK)
- **Athlete**, **Country**, **PR** - copied from the input file

The rows are sorted by time slot and then by station.

## Program structure

| File | What it does |
|------|--------------|
| `main.py` | Starts the program and calls all the other parts in order |
| `read_data.py` | `read_athletes()` reads the csv file into a list of dictionaries |
| `stations.py` | `create_stations()` makes the stations and which disciplines they support |
| `availability.py` | Keeps track of which stations and athletes are busy in each time slot |
| `assign_events.py` | `create_events()` makes one event for every discipline of every athlete |
| `schedule.py` | `make_schedule()` finds a free time slot and station for every event |
| `write_output.py` | `write_schedule()` writes the schedule to `schedule.csv` |
| `check_schedule.py` | Our checker, reads `schedule.csv` back and checks all the rules |

### The algorithm

We go through the athletes in the order of the file. For every discipline an athlete has, we
start at time slot 0 and try every station that supports the discipline. If the athlete is
busy or all the stations are busy we try the next time slot, until we find a slot that works.

### Results

With `athletes.csv` there are 100 athletes and 304 events. The schedule uses 175 time slots.
There are 175 running events and only one TRACK, so 175 is the shortest possible schedule.

### Checker

`check_schedule.py` checks that:

1. an athlete is only in one event per time slot
2. a station only has one athlete per time slot
3. every discipline is on a station that supports it
4. every athlete got all of their disciplines

It runs automatically at the end of `main.py`.
