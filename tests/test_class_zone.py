import unittest

from models import Zone


class TestZone(unittest.TestCase):
    def setUp(self) -> None:
        Zone._id_counter = 0

    def test_default_constructor_and_id_generation(self) -> None:
        """Test 1: autoID and constructor"""
        zone_0 = Zone()
        zone_1 = Zone()

        # Check ID generation
        self.assertEqual(zone_0.get_id(), "ZONE-0")
        self.assertEqual(zone_1.get_id(), "ZONE-1")

    def test_explicit_id_constructor(self) -> None:
        """Test 2: explicit ID"""
        custom_zone = Zone(zone_id="A-101")
        self.assertEqual(custom_zone.get_id(), "A-101")

    def test_str_representation(self) -> None:
        """Test 3: string representation"""
        zone = Zone(zone_id="ZONE-3")
        self.assertEqual(str(zone), "id: ZONE-3")


if __name__ == "__main__":
    unittest.main()
