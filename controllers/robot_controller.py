class RobotController:
    def __init__(self, manipulator, movement_strategy, indicator=None):
        self.manipulator = manipulator
        self.movement_strategy = movement_strategy
        self.indicator = indicator

    def initialize(self):
        self.manipulator.connect()
        self.manipulator.get_control()
        print("Управление захвачено. Подъём на безопасную высоту...")

        
        if self.indicator:
            self.indicator.off()


        self.manipulator.move_to(
            position=(0.0, 0.0, 0.45),
            orientation=(0, 0, 0, 1.0),
            velocity=0.3,
            acceleration=0.3
        )
        print("Робот поднят. Запуск динамического контроля скорости.")

    def start(self):
        if self.indicator:
            self.indicator.blink(2.0)   # режим "движение"
        self.movement_strategy.execute()
        if self.indicator:
            self.indicator.off()