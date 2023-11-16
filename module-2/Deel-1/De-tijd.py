for hour in range(24):
    suffix = "AM" if hour < 12 else "PM"
    display_hour = hour if hour <= 12 else hour - 12
    display_hour = 12 if display_hour == 0 else display_hour

    print(f"{display_hour:02d}:00 {suffix}")


