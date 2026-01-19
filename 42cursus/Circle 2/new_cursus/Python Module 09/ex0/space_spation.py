from typing import Any, Dict
from datetime import datetime
import sys


try:
    from pydantic import BaseModel, Field, ValidationError
except ModuleNotFoundError as e:
    print(f"\n{type(e).__name__}: missing dependency {e.name}.\nTry to install"
          " it first using 'pip install pydantic'", file=sys.stderr)
    exit(2)


class SpaceStation(BaseModel):
    """
    Inherits from BaseModel and define a SpaceStation class with specific
    types.

    station_id: (str), 3-10 characters.
    name: (str), 1-50 characters.
    crew_size: (int), 1-20 people.
    power_level: (float), 0.0-100.0 percent.
    oxygen_level: (float), 0.0-100.0 percent.
    last_maintenance: (DateTime).
    is_operational: (bool), defaults to True.
    notes: (Optional), (str), 200 characters max.

    """
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50, description="Name of ship")
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: str | None = Field(min_length=0, max_length=200, default=None)


def create_station(data: Dict[str, Any]) -> SpaceStation | None:
    """"Create a station using a dictionary.

    === Args ===
        - data (Dict[str, Any]): A dictionary containing station data. Keys
          must match the SpaceStation field names.

    === Returns ===
        - SpaceStation: the object if data are validated.
        - None: none if data are not validated.
    """
    try:
        # '**data' unpack the dict, so key and value become key='value'
        station = SpaceStation(**data)
        return station

    except ValidationError as e:
        print("Invalid station created:")
        print(f"{type(e).__name__}", end=" - ")
        for item in e.errors():
            print(f"{item['loc']}: {item['msg']}")
        return None


def print_informations(station: SpaceStation) -> None:
    """"Print informations about the SpaceStation.

    === Args ===
        - station (SpaceStation): The SpaceStation object and validated.
    """
    print("Valid station created:")
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    print(f"Datetime: {station.last_maintenance}")
    if not station.is_operational:
        print("Status: False")
    else:
        print("Status: True")
    if station.notes is not None:
        print(f"Notes: {station.notes}")


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")

    date = datetime.now()
    date_amg = '2023-04-23T10:01:06Z'
    date_wrong = 'oui baguette'

    # Good values
    station_list = {
        'station_id': 'ISS001',
        'name': 'International Space Station',
        'crew_size': 6,
        'power_level': 85.5,
        'oxygen_level': 92.3,
        'last_maintenance': date,
        'is_operational': True
    }
    # Good values (with note)
    station_list2 = {
        'station_id': 'AMG_001',
        'name': 'Polux Spaceship',
        'crew_size': 10,
        'power_level': 66.6,
        'oxygen_level': 23.3,
        'last_maintenance': date_amg,
        'is_operational': False,
        'notes': "There are 2 imposteurs among us"
    }
    # Wrong Values
    wrong_station = {
        'station_id': 'id_0123456789',
        'name': 'I',
        'crew_size': 21,
        'power_level': 105.00,
        'oxygen_level': -01.00,
        'last_maintenance': date_wrong,
        'is_operational': "hey",
        'notes': 123
    }
    # Wrong Values
    almost_wrong_station = {
        'name': 'No ID Station',
        'crew_size': 5
    }

    print("- Creating ISS001 -")
    station = create_station(station_list)
    if station is not None:
        print_informations(station)

    print("\n- Creating AMG_001 -")
    station = create_station(station_list2)
    if station is not None:
        print_informations(station)

    print("\n- Creating ERR001 -")
    station = create_station(wrong_station)
    if station is not None:
        print_informations(station)

    print("\n- Creating ERR002 -")
    station = create_station(almost_wrong_station)
    if station is not None:
        print_informations(station)


if __name__ == "__main__":
    main()
