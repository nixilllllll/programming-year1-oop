import unittest

from models import Cargo, Robot, Task, Zone


class TestTask(unittest.TestCase):
    def setUp(self) -> None:
        Task._id_counter = 0
        self.zone_from = Zone(zone_id="ZONE-1")
        self.zone_to = Zone(zone_id="ZONE-2")
        self.cargo = Cargo(cargo_id="C-1")

    def test_auto_id_and_defaults(self) -> None:
        task = Task(
            from_zone=self.zone_from, to_zone=self.zone_to, task_cargo=self.cargo
        )
        self.assertEqual(task.get_id(), "TASK-0")
        self.assertEqual(task.get_status(), "created")
        self.assertIsNone(task.get_performer())

    def test_same_zone_error(self) -> None:
        with self.assertRaises(ValueError):
            Task(
                from_zone=self.zone_from, to_zone=self.zone_from, task_cargo=self.cargo
            )

    def test_str_representation(self) -> None:
        task = Task(
            task_id="T-100",
            from_zone=self.zone_from,
            to_zone=self.zone_to,
            task_cargo=self.cargo,
        )
        expected = "id: T-100, status: created, performer: None, cargo: C-1, from: ZONE-1, to: ZONE-2"
        self.assertEqual(str(task), expected)


if __name__ == "__main__":
    unittest.main()
