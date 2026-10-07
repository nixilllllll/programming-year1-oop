import pickle
from datetime import datetime


class DataPersistence:
    @staticmethod
    def serialize(obj, filename: str) -> None:
        with open(filename, "wb") as f:
            pickle.dump(obj, f)

    @staticmethod
    def deserialize(filename: str):
        with open(filename, "rb") as f:
            return pickle.load(f)


class Transaction:
    def __init__(self, operation: str, old_value: str, new_value: str):
        self.when = datetime.now()
        self.operation = operation
        self.old_value = old_value
        self.new_value = new_value

    def __str__(self):
        return "{0}: Operation '{1}' changed {2} -> {3}".format(
            self.when.strftime("%Y-%m-%d %H:%M:%S"),
            self.operation,
            self.old_value,
            self.new_value,
        )


class Zone:
    id: str

    _id_counter: int = 0

    def __init__(self, zone_id: str | None = None) -> None:
        if zone_id is None:
            self.id = f"ZONE-{Zone._id_counter}"
            Zone._id_counter += 1
        else:
            self.id = zone_id

    def get_id(self) -> str:
        return self.id

    def get_info(self) -> str:
        return f"Zone ID: {self.id}"

    def __str__(self) -> str:
        return "id: {0}".format(self.id)


class Cargo:
    id: str
    weight: float
    location: Zone
    transactions: list[Transaction]

    _id_counter: int = 0

    def __init__(
        self,
        cargo_id: str | None = None,
        cargo_weight: float = 1.0,
        cargo_location: Zone | None = None,
    ) -> None:
        if cargo_id is None:
            self.id = f"CARGO-{Cargo._id_counter}"
            Cargo._id_counter += 1
        else:
            self.id = cargo_id
        self.weight = cargo_weight
        self.location = cargo_location
        self.transactions = []

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
        self.transactions.append(
            Transaction("set_weight", str(self.weight), str(new_weight))
        )
        self.weight = new_weight

    def set_location(self, new_location: Zone) -> None:
        old_loc = self.location.get_id() if self.location else "None"
        self.transactions.append(
            Transaction("set_location", str(self.location.id), str(new_location.id))
        )
        self.location = new_location

    def __str__(self) -> str:
        return "id: {0}, weight: {1}".format(self.id, self.weight)

    def __del__(self):
        try:
            with open("transaction.txt", "a") as f:
                for t in self.transactions:
                    f.write("Cargo {0} - {1}\n".format(self.id, str(t)))
        except Exception:
            pass


class Robot:
    id: str
    charge: float
    max_load: float
    location: Zone
    cargo: Cargo | None = None
    status: str
    transactions: list[Transaction]

    _id_counter: int = 0

    def __init__(
        self,
        robot_id: str | None = None,
        robot_charge: float = 100.0,
        robot_max_load: float = 10.0,
        robot_location: Zone | None = None,
        robot_cargo: Cargo | None = None,
        robot_status: str = "idle",
    ) -> None:
        if robot_id is None:
            self.id = f"ROBOT-{Robot._id_counter}"
            Robot._id_counter += 1
        else:
            self.id = robot_id

        if not (0.0 <= robot_charge <= 100.0):
            raise ValueError("Charge must be between 0 and 100!")
        if robot_max_load <= 0:
            raise ValueError("Max Load must be more than zero!")

        self.charge = robot_charge
        self.max_load = robot_max_load
        self.location = robot_location
        self.cargo = robot_cargo
        self.status = robot_status
        self.transactions = []

    def get_id(self) -> str:
        return self.id

    def get_charge(self) -> float:
        return self.charge

    def set_charge(self, new_charge: float) -> None:
        if not (0.0 <= new_charge <= 100.0):
            raise ValueError("Charge must be between 0 and 100!")
        self.transactions.append(
            Transaction("set_charge", str(self.charge), str(new_charge))
        )
        self.charge = new_charge

    def get_max_load(self) -> float:
        return self.max_load

    def set_max_load(self, new_max_load: float) -> None:
        if new_max_load <= 0:
            raise ValueError("Max Load must be more then zero!")
        self.transactions.append(
            Transaction("set_max_load", str(self.max_load), str(new_max_load))
        )
        self.max_load = new_max_load

    def get_location(self) -> Zone:
        return self.location

    def set_location(self, new_location: Zone) -> None:
        old_loc = self.location.get_id() if self.location else "None"
        self.transactions.append(
            Transaction("set_location", old_loc, new_location.get_id())
        )
        self.location = new_location

    def get_cargo(self) -> Cargo | None:
        return self.cargo

    def set_cargo(self, new_cargo: Cargo | None) -> None:
        if new_cargo is not None and new_cargo.get_weight() > self.max_load:
            raise ValueError("Cargo is too heavy for this robot!")
        old_cargo = self.cargo.get_id() if self.cargo else "None"
        new_val = new_cargo.get_id() if new_cargo else "None"
        self.transactions.append(Transaction("set_cargo", old_cargo, new_val))
        self.cargo = new_cargo

    def get_status(self) -> str:
        return self.status

    def set_status(self, new_status: str) -> None:
        self.transactions.append(Transaction("set_status", self.status, new_status))
        self.status = new_status

    def get_info(self) -> str:
        cargo = self.get_cargo()
        cargo_id = cargo.get_id() if cargo is not None else "None"
        return (
            f"Robot ID: {self.get_id()}\n"
            f"Robot Status: {self.get_status()}\n"
            f"Robot Location: {self.location.get_id()}\n"
            f"Robot Charge: {self.get_charge()}\n"
            f"Robot Max Load: {self.get_max_load()} kg\n"
            f"Cargo ID: {cargo_id}\n"
        )

    def __str__(self) -> str:
        loc_id = self.location.get_id() if self.location else "None"
        cargo_id = self.cargo.id if self.cargo else "None"

        return "id: {0}, status: {1}, location: {2}, charge: {3}, max_load: {4}, cargo_id: {5}".format(
            self.id,
            self.status,
            loc_id,
            self.charge,
            self.max_load,
            cargo_id,
        )

    def __del__(self):
        try:
            with open("transaction.txt", "a") as f:
                for t in self.transactions:
                    f.write("Robot {0} - {1}\n".format(self.id, str(t)))
        except Exception:
            pass


class Task:
    id: str
    status: str
    performer: Robot | None
    cargo: Cargo
    from_zone: Zone
    to_zone: Zone
    transactions: list[Transaction]

    _id_counter: int = 0

    def __init__(
        self,
        from_zone: Zone,
        to_zone: Zone,
        task_cargo: Cargo,
        task_id: str | None = None,
        task_status: str = "created",
        task_performer: Robot | None = None,
    ) -> None:
        if from_zone.get_id() == to_zone.get_id():
            raise ValueError("Source and destination zones must be different!")

        if task_id is None:
            self.id = f"TASK-{Task._id_counter}"
            Task._id_counter += 1
        else:
            self.id = task_id

        self.status = task_status
        self.performer = task_performer
        self.cargo = task_cargo
        self.from_zone = from_zone
        self.to_zone = to_zone
        self.transactions = []

    def get_id(self) -> str:
        return self.id

    def get_status(self) -> str:
        return self.status

    def set_status(self, new_status: str) -> None:
        self.transactions.append(Transaction("set_status", self.status, new_status))
        self.status = new_status

    def get_performer(self) -> Robot | None:
        return self.performer

    def set_performer(self, new_performer: Robot | None) -> None:
        old_perf = self.performer.get_id() if self.performer else "None"
        new_perf = new_performer.get_id() if new_performer else "None"
        self.transactions.append(Transaction("set_performer", old_perf, new_perf))
        self.performer = new_performer

    def get_cargo(self) -> Cargo:
        return self.cargo

    def get_from_zone(self) -> Zone:
        return self.from_zone

    def get_to_zone(self) -> Zone:
        return self.to_zone

    def get_info(self) -> str:
        performer = self.get_performer()
        performer_id = performer.get_id() if performer is not None else "None"
        return (
            f"Task ID: {self.get_id()}\n"
            f"Task Status: {self.get_status()}\n"
            f"Task Performer: {performer_id}\n"
            f"Cargo: {self.get_cargo().get_id()}\n"
            f"From Zone: {self.get_from_zone().get_id()}\n"
            f"To Zone: {self.get_to_zone().get_id()}\n"
        )

    def __str__(self) -> str:
        performer_id = self.performer.get_id() if self.performer else "None"
        return "id: {0}, status: {1}, performer: {2}, cargo: {3}, from: {4}, to: {5}".format(
            self.id,
            self.status,
            performer_id,
            self.cargo.get_id(),
            self.from_zone.get_id(),
            self.to_zone.get_id(),
        )

    def __del__(self):
        try:
            with open("transaction.txt", "a") as f:
                for t in self.transactions:
                    f.write("Task {0} - {1}\n".format(self.id, str(t)))
        except Exception:
            pass
