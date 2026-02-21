import json
from abc import ABC, abstractmethod
from pathlib import Path


class VehicleGenerator(ABC):
    @abstractmethod
    def to_dict(self) -> dict:
        pass

    def to_json(self, vehicles: list, file_path: str):
        try:
            path = Path(file_path)
            path.parent.mkdir(parents=True, exist_ok=True)

            with open(file_path, "w") as json_file:
                json.dump(vehicles, json_file, indent=4)
        except Exception as e:
            print(f"Error writing to JSON file: {e}")
