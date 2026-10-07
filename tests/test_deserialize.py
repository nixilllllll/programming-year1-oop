import os
import time
import unittest

from models import Cargo, DataPersistence, Robot, Zone


class TestLab19(unittest.TestCase):
    def setUp(self):
        if os.path.exists("transaction.txt"):
            os.remove("transaction.txt")
        Robot._id_counter = 0
        Cargo._id_counter = 0

    def test_transaction_history(self):
        cargo = Cargo(cargo_id="C-1", cargo_weight=10.0)
        cargo.set_weight(20.0)
        cargo.set_weight(30.0)

        self.assertEqual(len(cargo.transactions), 2)
        self.assertEqual(cargo.transactions[0].operation, "set_weight")
        self.assertEqual(cargo.transactions[0].old_value, "10.0")
        self.assertEqual(cargo.transactions[0].new_value, "20.0")

    def test_serialization(self):
        filename = "robot_test.pkl"
        original_robot = Robot(robot_id="R-TEST", robot_charge=75.0)

        DataPersistence.serialize(original_robot, filename)

        loaded_robot = DataPersistence.deserialize(filename)

        self.assertEqual(loaded_robot.get_id(), "R-TEST")
        self.assertEqual(loaded_robot.get_charge(), 75.0)

        if os.path.exists(filename):
            os.remove(filename)

    def test_destructor_file_output(self):
        cargo = Cargo(cargo_id="DEL-TEST")
        cargo.set_weight(50.0)

        del cargo

        time.sleep(0.1)

        self.assertTrue(os.path.exists("transaction.txt"))
        with open("transaction.txt", "r") as f:
            content = f.read()
            self.assertIn("DEL-TEST", content)
            self.assertIn("set_weight", content)
            self.assertIn("50.0", content)


if __name__ == "__main__":
    unittest.main()
