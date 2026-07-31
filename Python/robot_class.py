class Robot:

    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def move(self):
        print(f"{self.name} is moving at {self.speed} m/s")

robot = Robot("Robo1", 2)

robot.move()