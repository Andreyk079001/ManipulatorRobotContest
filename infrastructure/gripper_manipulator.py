from sdk.attachments.gripper_attachment import GripperAttachment

class MEduGripper:
    def __init__(self, manipulator):
        self._gripper = GripperAttachment(manipulator)
        manipulator.nozzle_power(True)

    def close(self, rotation=20, grip=10):
        self._gripper.activate(rotation=rotation, gripper=grip)

    def open(self):
        self._gripper.deactivate()