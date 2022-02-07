# def clock(hour, minutes):
#     #dictionary = {"hour":30, "minutes":6}
#     if hour == 12:
#         predicted_hour_angle = 0
#     else:
#         predicted_hour_angle = hour * 30
#     print(predicted_hour_angle)
#     if minutes == 60:
#         predicted_minute_angle = 0
#     else:
#         predicted_minute_angle = minutes * 6
#     print(predicted_minute_angle)

#     if predicted_hour_angle > predicted_minute_angle:
#         predicted_angle = predicted_hour_angle - predicted_minute_angle
#     else:
#         predicted_angle = predicted_minute_angle -  predicted_hour_angle
#     print(predicted_angle)

#     # 1 tik = 12 minutes
#     #1 tik = 6 degree
#     tik = minutes / 12
#     print(tik)
#     exceed_angle = int(tik * 6)
#     print(exceed_angle)

#     if  predicted_angle - exceed_angle >=180:
#         return 360 -  predicted_angle - exceed_angle
#     else:
#         predicted_angle - exceed_angle

# print(clock(11,10))

def anglesbetweenclock(hour, minutes):
    total_hour = hour + (minutes/60) # getting the exact hours by taking the minutes too.
    print(total_hour)
    Hour_angle =  total_hour * 30  #calculating the hour angle as 1 hour is 30 degree
    print(Hour_angle)
    Minute_angle = minutes * 6 #calculating the minutes angle as 1 minutes is 6 degree
    print(Minute_angle)
    difference = abs(Minute_angle-Hour_angle)

    print(True)
    print(difference)
    # print(difference) we are assuming that we are taking  the angle that is less than 180 degree because there will be two angles.
    if difference > 180:
        return 360-difference
    return difference
print(anglesbetweenclock(11,10))
