import time

class DynamicJointSpeedController:
    def __init__(self, manipulator, zone_manager):
        self.manipulator = manipulator
        self.zone_manager = zone_manager
        self.prev_zone = None

    def execute(self):
        print("Динамическое ограничение скорости по вертикальной оси Z...")
        try:
            self.manipulator._manipulator.set_servo_twist_mode()

            x, y, z, orientation = (1, 0.0, 1, (0,0,0,1))


            start_time = time.time()  # запоминаем время начала

            while time.time() - start_time < 4:  # пока не прошло 5 секунд
                print("Цикл выполняется...")
                # time.sleep(0.5)  # пауза 0.5 секунды между итерациями (для примера)
                self.manipulator.stream_velocity(
                    {"x": 0, "y": 10, "z": 0},
                    {"rx": 0, "ry": 0, "rz": 0}
                )
            time.sleep(3)
            print("==================================================================================")
            

            while True:
                _x, _y, z = self.manipulator.get_coordinates()
                print(_x, _y, z)
                zone = self.zone_manager.get_zone(_y)
                speed = zone.speed if zone else 0.1

                if zone != self.prev_zone:
                    name = zone.name.upper() if zone else "OUT"
                    self.prev_zone = zone
                
                print(f"→ Зона: {name} | Скорость: {speed*100:.0f}%")
                
                self.manipulator.stream_velocity(
                    {"x": 0, "y": -1.5* speed, "z": 0},
                    {"rx": 0, "ry": 0, "rz": 0}
                )

                time.sleep(0.1)
        except KeyboardInterrupt:
            self.manipulator.stop()
            print("\nОстановка движения.")