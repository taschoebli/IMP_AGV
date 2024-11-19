from robot import Robot
from mock_robot import MockRobot


class Agent:
    def __init__(self, id, is_coordinator, use_mock_robot, current_edge, robot_facing_direction):
        self.id = id
        self.is_coordinator = is_coordinator
        self.current_edge = current_edge
        self.robot_facing_direction = robot_facing_direction
        if use_mock_robot:
            self.robot = MockRobot(self.log, current_edge, robot_facing_direction)
        else:
            self.robot = Robot(self.log, current_edge, robot_facing_direction)

    def log(self, message):
        """
        Logs messages to the console with specifying the own local ip
        """
        print(f"Some message from the agent class")