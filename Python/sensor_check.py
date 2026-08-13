def check_distance(distance):
    if distance < 1.0:
        return "Object is very close"
    elif distance < 3.0:
        return "Object detected nearby"
    else:
        return "Path is clear"


distance = float(input("Enter sensor distance in meters: "))

result = check_distance(distance)

print(result)
