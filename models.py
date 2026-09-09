class Robot:
    def __init__(self) -> None:
        pass


class Zone:
    id: str

    def __init__(self, zone_id: str) -> None:
        self.id = zone_id

    def get_info(self) -> str:
        return f"Zone ID: {self.id}"


class Cargo:
    id: str
    weight: float
    location: Zone

    def __init__(
        self, cargo_id: str, cargo_weight: float, cargo_location: Zone
    ) -> None:
        self.id = cargo_id
        self.weight = cargo_weight
        self.location = cargo_location

    def get_info(self) -> str:
        return f"Cargo ID: {self.id}\nCargo Weight: {self.weight}\nCurrent Location: {self.location.id}"

    def get_id(self) -> str:
        return self.id

    def get_weight(self) -> float:
        return self.weight

    def get_location(self) -> Zone:
        return self.location

    def set_location(self, new_location: Zone) -> None:
        self.location = new_location


class Task:
    def __init__(self) -> None:
        pass
