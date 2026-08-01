"""Sensor-status monitor for robotics practice."""

sensor_readings = {
    "camera": True,
    "lidar": True,
    "motor_temperature": 44,
    "battery": 80
}

for sensor, value in sensor_readings.items():
    print(f"{sensor}: {value}")

if sensor_readings["battery"] < 20:
    print("Warning: Battery is low")
else:
    print("Battery level is sufficient")

if sensor_readings["motor_temperature"] > 70:
    print("Warning: Motor temperature is high")
else:
    print("Motor temperature is normal")