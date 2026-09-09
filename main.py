from models import Cargo, Zone

zone_a = Zone("ALPHA")
zone_b = Zone("BETA")

cargo_a = Cargo("banana", 1.1, zone_a)

print(zone_a.get_info())
print(zone_b.get_info())
print()
print(cargo_a.get_info())
cargo_a.set_location(zone_b)
print(f"Cargo '{cargo_a.get_id()}' was moved!")
print(cargo_a.get_info())
