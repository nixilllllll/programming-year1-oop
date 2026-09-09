from models import Cargo, Zone

zone_a = Zone("ALPHA")
zone_b = Zone("BETA")

cargo_a = Cargo("banana", 1.1, zone_a)
cargo_b = Cargo("apple", 1.2, zone_b)

print(zone_a.get_info())
print(zone_b.get_info())

print(cargo_a.get_info())
print(cargo_b.get_info())
