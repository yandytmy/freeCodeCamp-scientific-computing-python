def add_time(start, duration, date=None):
    date_set = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    temp_time = start.split(" ")
    temp_hm = temp_time[0].split(":")
    hour, minute, ampm = int(temp_hm[0]), int(temp_hm[1]), temp_time[1]
    temp_duration = duration.split(":")
    hour_add, minute_add = int(temp_duration[0]), int(temp_duration[1])

    day_result = 0
    minute_result = (minute + minute_add) % 60
    hour_result = (hour + hour_add + (minute + minute_add) // 60) % 24
    if hour_result >= 12 and hour_result <= 24 and ampm == "PM":
        ampm = "AM"
        day_result += 1
    elif hour_result >= 12 and hour_result <= 24 and ampm == "AM":
        ampm = "PM"
    hour_result -= 12 if hour_result > 12 else 0
    day_result += (hour + hour_add + (minute + minute_add) // 60) // 24
    
    if not(date == None):
        date_now = date_set.index(date.lower())
        date_add = (date_now + day_result) % 7
        date_result = date_set[date_add]
    
    new_time = str(hour_result) + ":"
    new_time += "0" + str(minute_result) if minute_result < 10 else str(minute_result)
    new_time += " " + ampm
    if not(date == None):
        new_time += ", " + date_result.capitalize()
    if day_result == 1:
        new_time += " (next day)"
    elif day_result > 1:
        new_time += " (" + str(day_result) + " days later)"

    return new_time
