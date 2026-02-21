from datetime import datetime
from pathlib import Path

import click
from car_generator import CarGenerator


def create_file_name_with_path(base_dir: str, format_ext: str) -> str:
    timestamp = datetime.now().time().isoformat()
    filename = f"log_{timestamp}.{format_ext}"
    return str(Path(base_dir) / filename)


@click.command()
@click.option(
    "--path",
    default="./logs",
    prompt="Path to create log file",
    type=click.STRING,
    help="The path to create log file.",
)
@click.option(
    "--count",
    default=1,
    prompt="Count of vehicles to generate",
    type=click.INT,
    help="The count of vehicles to generate in JSON.",
)
def main(path: str, count: int):
    file_path = create_file_name_with_path(path, "json")

    car = CarGenerator()
    vehicles = []

    for _ in range(count):
        vehicles.append(car.to_dict())
    car.to_json(vehicles, file_path)

    click.echo(f"Log file generated at: {file_path}")


if __name__ == "__main__":
    main()
