def time_converter(hour, minute, period):
    # check if hour is not equal to 12 
    if hour != 12 and (period == "pm" or period == "PM"):
        hour +=12
    # check if hour is equal to 12 and update hour to 0 if true otherwise hour remains the same
    elif hour == 12 and (period == "am" or period == "AM"):
         hour = 0
       
    # update hour and minute with 2 digits
    hour = str(hour).rjust(2, '0')
    minute = str(minute).rjust(2, '0')
    # return time in 24 hour format
    return f"{hour}{minute}" 


print(time_converter(8, 30, "AM")) #0830
print(time_converter(8, 30, "PM")) #2030
print(time_converter(12, 00, "AM")) #0000
print(time_converter(12, 00, "PM")) #1200



