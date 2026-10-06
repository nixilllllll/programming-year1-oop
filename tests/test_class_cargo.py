import unittest

from models import Cargo, Zone


class TestCargo(unittest.TestCase):
    def setUp(self) -> None:
        Cargo._id_counter = 0
        self.zone = Zone(zone_id="ZONE-1")

    def test_constructor(self) -> None:
        cargo = Cargo(cargo_id="C-1", cargo_weight=10.5, cargo_location=self.zone)
        self.assertEqual(cargo.get_id(), "C-1")
        self.assertEqual(cargo.get_weight(), 10.5)
        self.assertEqual(cargo.get_location(), self.zone)

    def test_auto_id(self) -> None:
        cargo_1 = Cargo()
        cargo_2 = Cargo()
        self.assertEqual(cargo_1.get_id(), "CARGO-0")
        self.assertEqual(cargo_2.get_id(), "CARGO-1")

    def test_set_weight_valid(self) -> None:
        cargo = Cargo(cargo_id="C-1", cargo_weight=5.0)
        cargo.set_weight(10.0)
        self.assertEqual(cargo.get_weight(), 10.0)

    def test_set_weight_invalid(self) -> None:
        cargo = Cargo(cargo_id="C-1", cargo_weight=5.0)
        with self.assertRaises(ValueError):
            cargo.set_weight(-1.0)


if __name__ == "__main__":
    unittest.main()
