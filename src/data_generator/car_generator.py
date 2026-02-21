from faker import Faker
from vehicle_generator import VehicleGenerator


class CarGenerator(VehicleGenerator):
    def to_dict(self) -> dict:
        try:
            fake = Faker()
            fake_car = {
                "vin": fake.bothify(
                    text="???###???", letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                ),
                "brand": fake.random_element(
                    elements=("Tesla", "BMW", "Ford", "Toyota")
                ),
                "model": fake.random_element(
                    elements=("Model 3", "Model S", "Model X", "Model Y")
                ),
                "metadata": {
                    "year": fake.random_int(min=2020, max=2024),
                    "factory": fake.random_element(
                        elements=("Giga Berlin", "Giga Texas", "Giga New York")
                    ),
                },
                "technical_specs": {
                    "engine": {
                        "type": fake.random_element(elements=("Electric", "Hybrid")),
                        "horsepower": fake.random_int(min=200, max=500),
                    }
                },
                "features": [fake.word() for _ in range(fake.random_int(min=1, max=5))],
            }
        except Exception as e:
            print(f"Error generating car data: {e}")
            return {}
        return fake_car
