from typing import Any, List
from pydantic import BaseModel, Field, ValidationError
from datetime import datetime


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
    notes: str | None = Field(min_length=0, max_length=200)


def create_station(data: List[Any]) -> SpaceStation | None:
    """"Create a station if data are valids.

    === Args ===
        - data (List[Any]): a list (7-8 objects) containing data about the
          space station.

    === Returns ===
        - SpaceStation: the object if data are validated.
        - None: none if data are not validated.
    """
    if len(data) == 7:
        note = None
    elif len(data) == 8:
        note = data[7]
    else:
        print(f"Error: List must have 7 or 8 objects (yours {len(data)})")
        return None
    try:
        station = SpaceStation(station_id=data[0],
                               name=data[1],
                               crew_size=data[2],
                               power_level=data[3],
                               oxygen_level=data[4],
                               last_maintenance=data[5],
                               is_operational=data[6],
                               notes=note
                               )
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
    station_list = ('ISS001', 'International Space Station', 6, 85.5,
                    92.3, date, True)

    # Good values (with note)
    station_list2 = ('AMG_001', 'Polux Spaceship', 10, 66.6,
                     23.3, date_amg, False, "There are 2 imposteurs among us")

    # Wrong Values
    wrong_station = ('id_0123456789', 'I', 21, 105.00,
                     -01.00, date_wrong, "hey", 123)
    # Specific Wrong Values
    almost_wrong_station = ('ERR002', 12, 1, 01.00,
                            100.00, date_wrong, False, "test")

    # Wrong list
    bad_list = ()

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

    print("\n- Creating ERR003 -")
    station = create_station(bad_list)
    if station is not None:
        print_informations(station)


if __name__ == "__main__":
    main()
