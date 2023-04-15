import math

def add_time(start, duration, day = None):
    time, amOrPm = start.split()
    thours, tminutes = map(int, time.split(":"))
    dhours, dminutes = map(int, duration.split(":"))
    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    #we add minutes
    nminutes = tminutes + dminutes
    nhours = thours
    if nminutes > 59:
        nminutes = nminutes % 60
        dhours += 1

    clockCycle = 0;
    while dhours:
        newT = nhours + 1
        if nhours == 11:
            clockCycle += 1
        if nhours == 12:
            nhours = 1
            dhours -= 1
            continue
        dhours -= 1
        nhours = newT

    dayPassed = 0
    if amOrPm == "AM":
        dayPassed += math.floor(clockCycle / 2)
        if clockCycle % 2 != 0:
            amOrPm = "PM"
        elif clockCycle == 1:
            amOrPm = "PM"
    else:
        if clockCycle % 2 == 0:
            dayPassed = clockCycle / 2
        else:
            dayPassed = math.ceil(clockCycle / 2)
            amOrPm = "AM"

    if nminutes < 10:
        new_time = str(nhours) + ":0" + str(nminutes) + " " + amOrPm
    else: 
        new_time = str(nhours) + ":" + str(nminutes) + " " + amOrPm
    if day:
        day = day.lower()
        day = day[0].upper() + day[1:]
        i = dayPassed
        while i:
            i -=1
            index = week.index(day)
            if day == "Sunday":
                day = "Monday"
                continue
            day = week[index + 1]
        new_time += ", " + day
    if dayPassed:
        if dayPassed == 1:
            new_time += " (next day)"
        else:
            new_time += " (" + str(dayPassed) + " days later)" 
    #if over 59 we add an hour and add the rest of the minutes
    #we add hours
    #if over 11 we change currentAMorPM
    #if we go over from PM to AM we're next day, store the amount of next day

    return new_time