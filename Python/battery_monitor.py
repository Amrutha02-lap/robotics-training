"""Simple battery monitoring program for robotics practice."""

battery_level = int(input("Enter battery percentage: "))

if battery_level >= 80:
    print("Battery Status: High")
elif battery_level >= 40:
    print("Battery Status: Medium")
elif battery_level >= 20:
    print("Battery Status: Low")
else:
    print("Warning! Charge the robot immediately.")