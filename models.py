class Zone:
    id: str

    def __init__(self, zone_id: str) -> None:
        self.id = zone_id

    def get_id(self) -> str:
        return self.id

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

    def get_id(self) -> str:
        return self.id

    def get_weight(self) -> float:
        return self.weight

    def get_location(self) -> Zone:
        return self.location

    def get_info(self) -> str:
        return (
            f"Cargo ID: {self.get_id()}\n"
            f"Cargo Weight: {self.get_weight()}\n"
            f"Current Location: {self.location.get_id()}"
        )

    def set_weight(self, new_weight: float) -> None:
        if new_weight <= 0:
            raise ValueError("Weight value must be more than zero!")
        self.weight = new_weight

    def set_location(self, new_location: Zone) -> None:
        self.location = new_location


class Robot:
    id: str
    charge: float
    max_load: float
    location: Zone
    cargo: Cargo | None = None
    status: str

    def __init__(
        self,
        robot_id: str,
        robot_charge: float,
        robot_max_load: float,
        robot_location: Zone,
        robot_cargo: Cargo | None = None,
        robot_status: str = "idle",
    ) -> None:
        if not (0.0 <= robot_charge <= 100.0):
            raise ValueError("Charge must be between 0 and 100!")
        if robot_max_load <= 0:
            raise ValueError("Max Load must be more then zero!")

        self.id = robot_id
        self.charge = robot_charge
        self.max_load = robot_max_load
        self.location = robot_location
        self.cargo = robot_cargo
        self.status = robot_status

    def get_id(self) -> str:
        return self.id

    def get_charge(self) -> float:
        return self.charge

    def set_charge(self, new_charge: float) -> None:
        if not (0.0 <= new_charge <= 100.0):
            raise ValueError("Charge must be between 0 and 100!")
        self.charge = new_charge

    def get_max_load(self) -> float:
        return self.max_load

    def set_max_load(self, new_max_load: float) -> None:
        if new_max_load <= 0:
            raise ValueError("Max Load must be more then zero!")
        self.max_load = new_max_load

    def get_location(self) -> Zone:
        return self.location

    def set_location(self, new_location: Zone) -> None:
        self.location = new_location

    def get_cargo(self) -> Cargo | None:
        return self.cargo

    def set_cargo(self, new_cargo: Cargo | None) -> None:
        if new_cargo is not None and new_cargo.get_weight() > self.max_load:
            raise ValueError("Cargo is too heavy for this robot!")
        self.cargo = new_cargo

    def get_status(self) -> str:
        return self.status

    def set_status(self, new_status: str) -> None:
        self.status = new_status

    def get_info(self) -> str:
        return (
            f"Robot ID: {self.get_id()}\n"
            f"Robot Charge: {self.get_charge()}\n"
            f"Robot Max Load: {self.get_max_load()}\n"
            f"Robot Location: {self.location.get_id()}\n"
            f"Robot Cargo: {self.get_cargo()}\n"
            f"Robot Status: {self.get_status()}\n"
        )


class Task:
    def __init__(self) -> None:
        pass
