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
    def __init__(self) -> None:
        pass


class Task:
    def __init__(self) -> None:
        pass
