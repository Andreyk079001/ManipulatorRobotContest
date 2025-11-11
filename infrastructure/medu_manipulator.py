from sdk.manipulators.medu import MEdu
from sdk.commands.move_coordinates_command import MoveCoordinatesParamsPosition, MoveCoordinatesParamsOrientation
from sdk.utils.enums import PlannerType
from interfaces.i_manipulator import IManipulator

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

    def move_to(self, position, orientation, velocity, acceleration):
        try:
            self._manipulator.move_to_coordinates(
                MoveCoordinatesParamsPosition(*position),
                MoveCoordinatesParamsOrientation(*orientation),
                velocity_scaling_factor=velocity,
                acceleration_scaling_factor=acceleration,
                planner_type=PlannerType.LIN,
                timeout_seconds=20.0,
                throw_error=True
            )
        except Exception as e:
            print(f"[SDK ERROR] move_to: {e}")

    def get_coordinates(self):
        try:
            coords = self._manipulator.get_cartesian_coordinates()
            return coords["x"], coords["y"], coords["z"]
        except Exception as e:
            print(f"[SDK ERROR] get_coordinates: {e}")
            return 0, 0, 0

    def get_joint_angles(self):
        try:
            state = self._manipulator.get_joint_state()
            return (
                state["povorot_osnovaniya"],
                state["privod_plecha"],
                state["privod_strely"]
            )
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
