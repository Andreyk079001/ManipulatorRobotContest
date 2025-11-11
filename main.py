from infrastructure.medu_manipulator import MEduManipulator
from domain.zones import Zone, ZoneManager
from domain.movement_strategy import DynamicSpeedController
from controllers.robot_controller import RobotController
from domain.movement_strategy_maze import MazePathController
from domain.led_indicator import UARTLedIndicator
from domain.joint_zones import JointZone, JointZoneManager, VerticalZone, VerticalZoneManager
from domain.movement_dynamic_joint import DynamicJointSpeedController


def task1(manip):
    zones = [
        VerticalZone("green", (0.35, 0.45), 0.8),  # верхняя безопасная зона
        VerticalZone("yellow", (0.25, 0.35), 0.5), # средняя
        VerticalZone("red", (0.15, 0.25), 0.2),    # нижняя — медленно
    ]
    zm = VerticalZoneManager(zones)
    strategy = DynamicJointSpeedController(manip, zm)
    ctrl = RobotController(manip, strategy)
    ctrl.initialize()
    ctrl.start()

def task2(manipulator):
    # светодиодная индикация движения
    zones = [
        Zone("green", (-0.20, 0.20), (-0.20, 0.20), (0.25, 0.45), 0.8)
    ]
    zone_manager = ZoneManager(zones)
    strategy = DynamicSpeedController(manipulator, zone_manager)
    indicator = UARTLedIndicator("/dev/ttyUSB0")
    controller = RobotController(manipulator, strategy, indicator)
    controller.initialize()
    controller.start()

def task3(manipulator):
    # траектория лабиринта
    trajectory = [
        (0.1, 0.0, 0.3, (0,0,0,1)),
        (0.2, 0.1, 0.3, (0,0,0,1)),
        (0.3, 0.2, 0.3, (0,0,0,1)),
    ]
    strategy = MazePathController(manipulator, trajectory, safe_radius=0.05)
    controller = RobotController(manipulator, strategy)
    controller.initialize()
    controller.start()


if __name__ == "__main__":
    # запуск основной программы
    manipulator = MEduManipulator("192.168.88.182", "122", "13", "14")
    choice = input("Выбери задачу (1 - зоны, 2 - светодиод, 3 - лабиринт): ")
    if choice == "1":
        task1(manipulator)
    elif choice == "2":
        task2(manipulator)
    elif choice == "3":
        task3(manipulator)