# def time_converter(hour, minute, period):
    
#     if hour != 12 and (period == "pm" or period == "PM"):
#         hour +=12

#     elif hour == 12 and (period == "am" or period == "AM"):
#          hour = 0
       
    
#     hour = str(hour).rjust(2, '0')
#     return f"{hour}{minute}"


# print(time_converter(12, 12, "PM"))


def convert_to_24(hour, minutes, period):
    
    time = f"00{minutes}"

    return time if hour == 12 and (period == "AM" or period =="am") else f"{hour+12}{minutes}"

print(convert_to_24(1, 44, "AM"))

