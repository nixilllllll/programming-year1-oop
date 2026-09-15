from models import Cargo, Robot, Task, Zone


def main() -> None:
    print("=== 1. Basic Objects Creation ===")
    zone_a = Zone("Zone-A")
    zone_b = Zone("Zone-B")

    cargo = Cargo("Cargo-101", 25.0, zone_a)
    robot = Robot("Robot-X", 100.0, 50.0, zone_a)
    task = Task("Task-55", "pending", None, cargo, zone_a, zone_b)

    print("--- Task Info Before Assignment ---")
    print(task.get_info())

    print("\n=== 2. Task Execution Simulation ===")
    task.set_performer(robot)
    task.set_status("in_progress")
    robot.set_status("busy")
    robot.set_cargo(cargo)

    print("--- Robot Info ---")
    print(robot.get_info())
    print("\n---  ---")
    print(task.get_info())

    print("\n=== 3. Validation Testing ===")
    try:
        print("Try to load overweight cargo...")
        heavy_cargo = Cargo("Cargo-Heavy", 100.0, zone_a)
        robot.set_cargo(heavy_cargo)
    except ValueError as e:
        print(f"Caught expected exception: {e}")

    try:
        print("Attempting to create a task with identical source and target zones...")
        Task("Task-Invalid", "pending", None, cargo, zone_a, zone_a)
    except ValueError as e:
        print(f"Caught expected exception: {e}")


if __name__ == "__main__":
    main()
