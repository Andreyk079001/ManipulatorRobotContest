import time

class DynamicSpeedController:
    def __init__(self, manipulator, zone_manager):
        self.manipulator = manipulator
        self.zone_manager = zone_manager
        self.prev_zone = None

    def execute(self):
        try:
            self.manipulator._manipulator.set_servo_twist_mode()
            
            while True:
                x, y, z = self.manipulator.get_coordinates()
                zone = self.zone_manager.get_zone(x, y, z)
                speed = zone.speed if zone else 0.1

                if zone != self.prev_zone:
                    name = zone.name.upper() if zone else "OUT"
                    print(f"→ Зона: {name} | Скорость: {speed*100:.0f}%")
                    self.prev_zone = zone

                self.manipulator.stream_velocity(
                    {"x": 0.02 * speed, "y": 0, "z": 0},
                    {"rx": 0, "ry": 0, "rz": 0}
                )
                time.sleep(0.1)
        except KeyboardInterrupt:
            self.manipulator.stop()
            print("\nОстановка движения.")
