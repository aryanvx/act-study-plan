from ics import Calendar, Event
from datetime import datetime, timedelta

def get_date_input(prompt):
    while True:
        try:
            date_str = input(prompt)
            return datetime.strptime(date_str, "%m/%d/%Y")
        except ValueError:
            print("Invalid date format. Please use the MM/DD/YYYY format.")

def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

print("=== ACT Study Plan Generator ===\n")

test_date = get_date_input("Enter your ACT test date (MM/DD/YYYY): ")

start_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

days_available = (test_date - start_date).days

if days_available <= 0:
    print("Error: Test date must be in the future!")
    exit()

print(f"\nYou have {days_available} days to study.\n")

num_subjects = get_int_input("How many subjects do you want to study? ")

subjects = []
total_chapters = 0

for i in range(num_subjects):
    subject_name = input(f"Enter name of subject {i+1}: ")
    num_chapters = get_int_input(f"How many chapters in {subject_name}? ")
    subjects.append({"name": subject_name, "chapters": num_chapters})
    total_chapters += num_chapters

print(f"\nTotal chapters to cover: {total_chapters}")

chapters_per_day = get_int_input("How many chapters do you want to study per day? ")

days_needed = total_chapters / chapters_per_day

if days_needed > days_available:
    print(f"\n⚠️  Warning: You need at least {int(days_needed)} days to complete all chapters at {chapters_per_day} chapters/day.")
    print(f"You only have {days_available} days available.")
    proceed = input("Do you want to continue anyway? (yes/no): ")
    if proceed.lower() != 'yes':
        exit()

print("\n📅 Generating study schedule...\n")

c = Calendar()
current_date = start_date
chapter_count = 0

all_chapters = []
for subject in subjects:
    for i in range(1, subject["chapters"] + 1):
        all_chapters.append(f"{subject['name']} Ch.{i}")

for i in range(0, len(all_chapters), chapters_per_day):
    if current_date >= test_date:
        break
    
    day_chapters = all_chapters[i:i+chapters_per_day]
    
    for chapter in day_chapters:
        e = Event()
        e.name = chapter
        e.begin = current_date
        e.make_all_day()
        c.events.add(e)
    
    print(f"{current_date.strftime('%m/%d/%Y')}: {', '.join(day_chapters)}")
    current_date += timedelta(days=1)

filename = "ACT_Study_Schedule.ics"
with open(filename, "w") as f:
    f.writelines(c)

print(f"\n✅ Calendar created: {filename}")
print("Import this file into your calendar app. Happy studying!")