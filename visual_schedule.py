# visual_schedule.py
# Optional feature: shows the schedule in a window with Tkinter.
# Every row is a time slot and every column is a station.
# The boxes get a color depending on the discipline so it is easy to see
# what is happening where. You can scroll down with the mouse wheel or the scrollbar.

from tkinter import *

# one color for every discipline
COLORS = {}
COLORS["LJ"] = "salmon"
COLORS["TJ"] = "orange"
COLORS["HJ"] = "yellow"
COLORS["PV"] = "violet"
COLORS["100m"] = "light blue"
COLORS["200m"] = "turquoise"
COLORS["400m"] = "light green"
COLORS["800m"] = "khaki"
COLORS["1600m"] = "pink"

BOX_WIDTH = 165       # width of one station column
BOX_HEIGHT = 24       # height of one time slot row
SLOT_WIDTH = 60       # width of the column with the time slot numbers
HEADER_HEIGHT = 30    # height of the row with the station names


def get_color(discipline):
    if discipline in COLORS:
        return COLORS[discipline]
    else:
        return "gray"


def show_schedule(schedule, station_names):
    # find out how many time slots there are
    last_slot = 0
    for assignment in schedule:
        if assignment["time_slot"] > last_slot:
            last_slot = assignment["time_slot"]
    number_of_slots = last_slot + 1

    total_width = SLOT_WIDTH + BOX_WIDTH * len(station_names)
    total_height = BOX_HEIGHT * number_of_slots

    window = Tk()
    window.title("Track and Field Schedule")

    # title at the top
    title_text = "Track and Field Schedule  -  " + str(len(schedule)) + " events in " + str(number_of_slots) + " time slots"
    title = Label(window, text=title_text, font=("Arial", 14, "bold"))
    title.pack(pady=5)

    # the legend that shows which color is which discipline
    legend = Frame(window)
    legend.pack(pady=5)
    for discipline in COLORS:
        label = Label(legend, text=discipline, bg=COLORS[discipline], width=6, relief=RIDGE)
        label.pack(side=LEFT, padx=2)

    # the station names at the top, this one does not scroll so you always see the names
    header = Canvas(window, width=total_width, height=HEADER_HEIGHT, bg="dark gray", highlightthickness=0)
    header.pack(anchor=W)
    header.create_text(SLOT_WIDTH / 2, HEADER_HEIGHT / 2, text="Slot", font=("Arial", 10, "bold"))
    for i in range(len(station_names)):
        x = SLOT_WIDTH + i * BOX_WIDTH
        header.create_text(x + BOX_WIDTH / 2, HEADER_HEIGHT / 2, text=station_names[i], font=("Arial", 10, "bold"))

    # the canvas with the schedule and a scrollbar
    frame = Frame(window)
    frame.pack(fill=BOTH, expand=True)

    canvas = Canvas(frame, width=total_width, height=550, bg="white", highlightthickness=0,
                    scrollregion=(0, 0, total_width, total_height), yscrollincrement=BOX_HEIGHT)
    scrollbar = Scrollbar(frame, orient=VERTICAL, command=canvas.yview)
    canvas.config(yscrollcommand=scrollbar.set)
    scrollbar.pack(side=RIGHT, fill=Y)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)

    # draw the rows, every other row is a bit gray so it is easier to read
    for time_slot in range(number_of_slots):
        y = time_slot * BOX_HEIGHT
        if time_slot % 2 == 0:
            row_color = "white"
        else:
            row_color = "#eeeeee"
        canvas.create_rectangle(0, y, total_width, y + BOX_HEIGHT, fill=row_color, outline="")
        canvas.create_text(SLOT_WIDTH / 2, y + BOX_HEIGHT / 2, text=str(time_slot), font=("Arial", 9))

    # lines between the stations
    for i in range(len(station_names) + 1):
        x = SLOT_WIDTH + i * BOX_WIDTH
        canvas.create_line(x, 0, x, total_height, fill="gray")

    # draw one box for every event in the schedule
    for assignment in schedule:
        column = station_names.index(assignment["station"])
        x = SLOT_WIDTH + column * BOX_WIDTH
        y = assignment["time_slot"] * BOX_HEIGHT
        color = get_color(assignment["discipline"])

        canvas.create_rectangle(x + 2, y + 2, x + BOX_WIDTH - 2, y + BOX_HEIGHT - 2, fill=color, outline="black")
        text = assignment["name"] + " (" + assignment["discipline"] + ")"
        canvas.create_text(x + BOX_WIDTH / 2, y + BOX_HEIGHT / 2, text=text, font=("Arial", 8))

    # so you can scroll with the mouse wheel
    def scroll(event):
        if event.num == 4 or event.delta > 0:
            canvas.yview_scroll(-3, "units")
        else:
            canvas.yview_scroll(3, "units")

    canvas.bind_all("<MouseWheel>", scroll)   # windows and mac
    canvas.bind_all("<Button-4>", scroll)     # linux scroll up
    canvas.bind_all("<Button-5>", scroll)     # linux scroll down

    window.mainloop()
