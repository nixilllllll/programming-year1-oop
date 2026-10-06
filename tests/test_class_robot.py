import unittest

from models import Cargo, Robot, Zone


class TestRobot(unittest.TestCase):
    def setUp(self) -> None:
        Robot._id_counter = 0

        self.zone = Zone(zone_id="ZONE-1")
        self.cargo = Cargo(
            cargo_id="CARGO-1", cargo_weight=10.0, cargo_location=self.zone
        )

    def test_constructor(self) -> None:
        robot = Robot(
            robot_id="R-1",
            robot_charge=100.0,
            robot_max_load=10.0,
            robot_location=self.zone,
            robot_cargo=self.cargo,
            robot_status="idle",
        )
        self.assertEqual(robot.get_id(), "R-1")
        self.assertEqual(robot.get_charge(), 100.0)
        self.assertEqual(robot.get_max_load(), 10.0)
        self.assertEqual(robot.get_location(), self.zone)
        self.assertEqual(robot.get_cargo(), self.cargo)
        self.assertEqual(robot.get_status(), "idle")

    def test_auto_id(self) -> None:
        robot_1 = Robot()
        robot_2 = Robot()
        self.assertEqual(robot_1.get_id(), "ROBOT-0")
        self.assertEqual(robot_2.get_id(), "ROBOT-1")

    def test_setters_and_valiadation(self) -> None:
        robot = Robot(
            robot_id="R-1",
            robot_charge=50.0,
            robot_max_load=10.0,
            robot_location=self.zone,
        )
        new_zone = Zone(zone_id="ZONE-2")
        robot.set_charge(80.0)
        robot.set_max_load(20.0)
        robot.set_location(new_zone)
        robot.set_status("moving")

        self.assertEqual(robot.get_charge(), 80.0)
        self.assertEqual(robot.get_max_load(), 20.0)
        self.assertEqual(robot.get_location(), new_zone)
        self.assertEqual(robot.get_status(), "moving")

    def test_cargo_logic(self) -> None:
        robot = Robot(robot_max_load=10.0)
        robot.set_cargo(self.cargo)
        self.assertEqual(robot.get_cargo(), self.cargo)

        heavy_cargo = Cargo(cargo_id="HEAVY", cargo_weight=20.0)
        with self.assertRaises(ValueError):
            robot.set_cargo(heavy_cargo)

    def test_str_representation(self) -> None:
        robot = Robot(
            robot_id="R-1",
            robot_status="idle",
            robot_charge=100.0,
            robot_location=self.zone,
        )
        expected = "id: R-1, status: idle, location: ZONE-1, charge: 100.0, max_load: 10.0, cargo_id: None"
        self.assertEqual(str(robot), expected)


if __name__ == "__main__":
    unittest.main()
