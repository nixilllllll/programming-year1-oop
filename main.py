from models import Cargo, Robot, Zone

zone_a = Zone("ALPHA")
zone_b = Zone("BETA")

cargo_a = Cargo("banana", 1.1, zone_a)

robot_a = Robot("Victor", 100.0, 80.0, zone_a, None, "idle")


print(zone_a.get_info())
print(zone_b.get_info())
print()
print(cargo_a.get_info())
print()
print(robot_a.get_info())
