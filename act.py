from ics import Calendar, Event
from datetime import datetime, timedelta

c = Calendar()

schedule = {
    "2025-09-24": ["Math Ch.12", "English Ch.4"],
    "2025-09-25": ["Math Ch.13", "Reading Ch.6"],
    "2025-09-26": ["Math Ch.14", "English Ch.5"],
    "2025-09-27": ["Math Ch.15", "Math Ch.16", "Reading Ch.7"],
    "2025-09-28": ["Math Ch.17", "Math Ch.18", "English Ch.6", "Reading Ch.8"],
    "2025-09-29": ["Math Ch.19", "English Ch.7"],
    "2025-09-30": ["Math Ch.20", "Reading Ch.9"],
    "2025-10-01": ["Math Ch.21", "English Ch.8"],
    "2025-10-02": ["Math Ch.22", "Reading Ch.10"],
    "2025-10-03": ["Math Ch.23", "English Ch.9"],
    "2025-10-04": ["Math Ch.24", "Math Ch.25", "Reading Ch.11"],
    "2025-10-05": ["Math Ch.26", "Math Ch.27", "English Ch.10", "Reading Ch.12"],
    "2025-10-06": ["Math Ch.28", "English Ch.11"],
    "2025-10-07": ["Math Ch.29", "Reading Ch.13"],
    "2025-10-08": ["Math Ch.30", "English Ch.12"],
    "2025-10-09": ["Math Ch.31", "Science Ch.7"],
    "2025-10-10": ["Math Ch.32", "Science Ch.8"],
    "2025-10-11": ["Math Ch.33", "English Ch.13", "Science Ch.9"],
    "2025-10-12": ["Math Ch.34", "Reading Ch.14", "Science Ch.10", "Science Ch.11"],
    "2025-10-13": ["Math Ch.35", "Science Ch.12"],
    "2025-10-14": ["English Ch.14", "English Ch.15", "Science Ch.13"]
}

for date_str, chapters in schedule.items():
    date = datetime.strptime(date_str, "%Y-%m-%d")
    for chapter in chapters:
        e = Event()
        e.name = chapter
        e.begin = date
        e.make_all_day()
        c.events.add(e)

with open("ACT_Study_Schedule.ics", "w") as f:
    f.writelines(c)
