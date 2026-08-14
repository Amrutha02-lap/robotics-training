file = open("day14_note.txt", "w")
file.write("ROS2 bag practice completed")
file.close()

file = open("day14_note.txt", "r")
content = file.read()
file.close()

print(content)
