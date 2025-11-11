class MazePathController:
    def __init__(self, manipulator, trajectory_points, safe_radius):
        self.manipulator = manipulator
        self.points = trajectory_points
        self.safe_radius = safe_radius

    def execute(self):
        print("Начало прохождения лабиринта...")
        for point in self.points:
            x, y, z, orientation = point
            # учёт безопасного радиуса и плавность
            self.manipulator.move_to(
                (x, y, z + self.safe_radius),
                orientation,
                velocity=0.2,
                acceleration=0.2
            )
        print("Траектория лабиринта пройдена.")