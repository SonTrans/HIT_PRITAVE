def create_event(name, day, time):
    event = {"name" : name,"day":day,"time":time}
    return event
def add_event(schedule, event):
    schedule.append(event)
def find_by_day(schedule, day):
    return [event for event in schedule if day == event["day"]]
def remove_event(schedule, name):
    schedule[:] = [event for event in schedule if name != event["name"]]
def export_schedule(schedule):
    lich = ''
    for event in schedule:
        lich += f"\n{event['name']} {event['day']} - {event['time']}"
    return lich
schedule = []
schedule.append(create_event("van","Thur","5 a.m"))
print(export_schedule(schedule))
event1 = create_event("toan", "Mon", "7 a.m")
event2 = create_event("ly", "Tue", "8 a.m")
event3 =  create_event("hoa", "Wed", "9 a.m")
add_event(schedule,event1)
add_event(schedule,event2)
add_event(schedule,event3)
print(export_schedule(schedule))
Mon = find_by_day(schedule,"Mon")
print(Mon)
remove_event(schedule,"toan")
print(schedule)
print(export_schedule(schedule))