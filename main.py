import csv
from ics import Calendar, Event
from datetime import datetime
from pytz import timezone

event_timezone = timezone('Asia/Kolkata')


def create_event(cal, name, date_str, time_str):
    event_datetime_naive = datetime.strptime(f'{date_str} {time_str}',
                                             '%m/%d/%y %I:%M:%S %p')

    event_datetime = event_timezone.localize(event_datetime_naive)

    event = Event(name=name, begin=event_datetime)
    cal.events.add(event)


cal = Calendar()

with open('icsconvert.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        event_name = row['name']
        event_date = row['Assignment deadlines Diploma']
        event_time = row['time']
        create_event(cal, event_name, event_date, event_time)

with open('deadlines_dip.ics', 'w') as f:
    f.writelines(cal)

print("Calendar file created: deadlines_dip.ics")
