def ft_water_reminder():
    day = input("Days since last watering: ")
    if int(day) > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
