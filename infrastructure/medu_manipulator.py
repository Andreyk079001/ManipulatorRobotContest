from sdk.manipulators.medu import MEdu
from sdk.commands.move_coordinates_command import MoveCoordinatesParamsPosition, MoveCoordinatesParamsOrientation, \
    PlannerType
from interfaces.manipulator_interface import IManipulator
import json
class MEduManipulator(IManipulator):
    def __init__(self, host, client_id, login, password):
        self._manipulator = MEdu(host, client_id, login, password)

    def connect(self):
        try:
            self._manipulator.connect()
        except Exception as e:
            print(f"[SDK ERROR] connect: {e}")

    def get_control(self):
        try:
            self._manipulator.get_control()
        except Exception as e:
            print(f"[SDK ERROR] get_control: {e}")

    def move_to(self, x, y, z):
        try:
            position = MoveCoordinatesParamsPosition(x, y, z)
            orientation = MoveCoordinatesParamsOrientation(0,0,0, 1.0)

            self.manipulator.move_to_coordinates(position, orientation, velocity_scaling_factor=0.5, acceleration_scaling_factor=0.5,
                                            planner_type=PlannerType.LIN, timeout_seconds=30.0, throw_error=True)
        except Exception as e:
            print(f"[SDK ERROR] move_to: {e}")
    def move_to_angle(self, x,z,y):
        try:
            self._manipulator.move_to_angles(x,y,z,
                                             velocity_factor=1.00,
                               acceleration_factor=1.00
            )
        except Exception as e:
            print(f"[SDK ERROR] move_to_angles: {e}")
    def get_coordinates(self):
        try:
            coordinates = self._manipulator.get_cartesian_coordinates()
            data = json.loads(coordinates)

            sx = data["tool1"]["position"]["x"]
            sy = data["tool1"]["position"]["y"]
            sz = data["tool1"]["position"]["z"]


            return sx, sy, sz
        except Exception as e:
            print(f"[SDK ERROR] get_coordinates: {e}")
            return 0, 0, 0

    def get_joint_angles(self):
        try:
            state = self._manipulator.get_joint_state()
            data = json.loads(state)

            sx = data["position"][0]
            sy = data["position"][1]
            sz = data["position"][2]


            return sx, sy, sz
        except Exception as e:
            print(f"[SDK ERROR] get_joint_angles: {e}")
            return 0, 0, 0

    def stream_velocity(self, linear_vel, angular_vel):
        try:
            self._manipulator.set_servo_twist_mode()
            self._manipulator.stream_cartesian_velocities(linear_vel, angular_vel)
        except Exception as e:
            print(f"[SDK ERROR] stream_velocity: {e}")

    def stop(self):
        try:
            self._manipulator.stop_movement(timeout_seconds=5.0)
        except Exception as e:
            print(f"[SDK ERROR] stop: {e}")
