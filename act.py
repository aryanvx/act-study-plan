from ics import Calendar, Event
from datetime import datetime, timedelta

c = Calendar()

def add_event(date_str, title):
    e = Event()
    e.name = title
    e.begin = date_str
    e.make_all_day()
    c.events.add(e)

start_date = datetime(2025, 9, 23)
end_date = datetime(2025, 10, 14)
total_days = (end_date - start_date).days + 1

subjects = {
    'Math': [
        (12, 7, 36), (13, 13, 47), (14, 3, 31), (15, 4, 25), (16, 7, 31),
        (17, 16, 51), (18, 3, 25), (19, 7, 26), (20, 4, 20), (21, 5, 35),
        (22, 7, 38), (23, 5, 32), (24, 4, 17), (25, 8, 30), (26, 1, 32),
        (27, 3, 24), (28, 6, 14), (29, 4, 25), (30, 1, 18), (31, 3, 18),
        (32, 4, 16), (33, 4, 14), (34, 7, 19), (35, 12, 37)
    ],
    'English': [
        (4, 6, 23), (5, 6, 23), (6, 4, 20), (7, 2, 18), (8, 6, 12),
        (9, 2, 40), (10, 3, 13), (11, 1, 10), (12, 2, 10), (13, 1, 20),
        (14, 4, 10), (15, 1, 8)
    ],
    'Reading': [
        (5, 4, 20), (6, 9, 25), (7, 3, 15), (8, 8, 10), (9, 1, 11),
        (10, 2, 12), (11, 9, 30), (12, 1, 10), (13, 9, 80)
    ],
    'Science': [
        (5, 4, 20), (6, 4, 20), (7, 2, 10), (8, 1, 8), (9, 2, 10),
        (10, 1, 6), (11, 1, 5), (12, 7, 30), (13, 2, 10)
    ]
}

def build_schedule(chapters, total_days):
    tasks = []
    for ch_num, lec, ques in chapters:
        for i in range(lec):
            tasks.append((ch_num, 1, 0))
        for j in range(ques):
            tasks.append((ch_num, 0, 1))
    per_day = len(tasks) / total_days
    schedule = [[] for _ in range(total_days)]
    day_idx = 0
    balance = 0
    for task in tasks:
        schedule[day_idx].append(task)
        balance += 1
        if balance >= per_day and day_idx < total_days - 1:
            day_idx += 1
            balance = 0
    return schedule

subject_daily = {sub: build_schedule(data, total_days) for sub, data in subjects.items()}

for day_offset in range(total_days):
    date_str = (start_date + timedelta(days=day_offset)).strftime('%Y-%m-%d')
    for sub in subjects.keys():
        entries = subject_daily[sub][day_offset]
        if entries:
            titles = []
            for ch, lec, ques in entries:
                if lec:
                    titles.append(f"{sub} Ch.{ch} ({lec} lecture)")
                if ques:
                    titles.append(f"{sub} Ch.{ch} ({ques} question)")
            add_event(date_str, "; ".join(titles))

with open('ACT_Study_Schedule_Final.ics', 'w') as f:
    f.writelines(c)

print("ACT study schedule .ics file generated: ACT_Study_Schedule_Final.ics")
