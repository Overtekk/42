from enum import Enum
from typing import Any, Dict, List, Self
from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime


class Rank(Enum):
    """Enumeration defining the allowed ranks for crew members."""
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    """
    Inherits from BaseModel and defines a CrewMember with specific attributes.

    member_id: (str), 3-10 characters.
    name: (str), 2-50 characters.
    rank: (Rank).
    age: (int), 18-80 years.
    specialization: (str), 3-30 characters.
    years_experience: (int), 0-50 years.
    is_active: (bool), defaults to True.

    """
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    """
    Inherits from BaseModel and defines a SpaceMission containing a list of
    CrewMembers.

    mission_id: (str), 5-15 characters.
    mission_name: (str), 3-100 characters.
    destination: (str), 3-50 characters.
    launch_date: (DateTime).
    duration_days: (int), 1-3650 days.
    crew: (List[CrewMember]), 1-12 members.
    mission_status: (str), defaults to "planned".
    budget_millions: (float), 1.0-10000.0 million dollars.

    """
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validation(self) -> Self:
        """Perform custom validation checks on the mission and crew.

        === Returns ===
        - Self: The object itself if all validations pass.
        """
        if not self.mission_id.startswith('M'):
            raise ValueError("Mission ID must start with \"M\"")

        valid_rank = False
        for crew in self.crew:
            if crew.rank == Rank.CAPTAIN or crew.rank == Rank.COMMANDER:
                valid_rank = True
        if valid_rank is False:
            raise ValueError("Must have at least one Commander or Captain")

        active_crew = 0
        for crew in self.crew:
            if crew.is_active:
                active_crew += 1
        if active_crew != len(self.crew):
            raise ValueError("All crew members must be active")

        xp_crew_count = 0
        if self.duration_days > 365:
            for crew in self.crew:
                if crew.years_experience >= 5:
                    xp_crew_count += 1
        if xp_crew_count < len(self.crew) / 2:
            raise ValueError("Long missions (> 365 days) need 50% experienced "
                             "crew (5+ years)")
        return self


def create_mission(data: Dict[str, Any]) -> SpaceMission | None:
    """"Create a space mission using a dictionary.

    === Args ===
        - data (Dict[str, Any]): A dictionary containing mission data. Keys
          must match the SpaceMission field names, and 'crew' must be a list
          of dictionaries matching CrewMember fields.

    === Returns ===
        - SpaceMission: the object if data are validated.
        - None: none if data are not validated.
    """
    try:
        mission = SpaceMission(**data)
        return mission
    except (ValidationError, ValueError) as e:
        print(f"Invalid mission\n{type(e).__name__}", end=" - ")
        for item in e.errors():
            print(f"{item['loc']}: {item['msg']}")
        return None


def print_information(data: SpaceMission) -> None:
    """"Print information about the SpaceMission and its Crew.

    === Args ===
        - data (SpaceMission): The SpaceMission object validated.
    """
    print("Valid mission created:")
    print(f" Mission: {data.mission_name}")
    print(f"ID: {data.mission_id}")
    print(f"Destination: {data.destination}")
    print(f"Duration: {data.duration_days} days")
    print(f"Launch date: {data.launch_date}")
    print(f"Mission status : {data.mission_status}")
    print(f"Budget: ${data.budget_millions}M")
    print(f"Crew size: {len(data.crew)}")
    print("Crew members:")
    for crew in data.crew:
        print(f"- {crew.name} ({crew.rank.value}) - {crew.specialization}")


def main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")

    # Good values
    mission1 = {
        'mission_id': 'M2024_Mars',
        'mission_name': 'Mars Colony Establishment',
        'destination': 'Mars',
        'launch_date': datetime.now(),
        'duration_days': 900,
        'crew': [
            {
                'member_id': 'Saconnor',
                'name': 'Sarah Connor',
                'rank': Rank.COMMANDER,
                'age': 35,
                'specialization': 'Mission Command',
                'years_experience': 12,
                'is_active': True
            },
            {
                'member_id': 'Josmith',
                'name': 'John Smith',
                'rank': Rank.LIEUTENANT,
                'age': 65,
                'specialization': 'Navigation',
                'years_experience': 9,
                'is_active': True
            },
            {
                'member_id': 'Aljohnson',
                'name': 'Alice Johnson',
                'rank': Rank.OFFICER,
                'age': 23,
                'specialization': 'Engineering',
                'years_experience': 5,
                'is_active': True
            }
        ],
        'mission_status': 'in progress',
        'budget_millions': 2500.0
    }
    # Wrong values (Mission ID)
    mission2 = {
        'mission_id': '2024_Mars',
        'mission_name': 'Mars Colony Establishment',
        'destination': 'Mars',
        'launch_date': datetime.now(),
        'duration_days': 900,
        'crew': [
            {
                'member_id': 'Saconnor',
                'name': 'Sarah Connor',
                'rank': Rank.COMMANDER,
                'age': 35,
                'specialization': 'Mission Command',
                'years_experience': 12,
                'is_active': True
            },
            {
                'member_id': 'Josmith',
                'name': 'John Smith',
                'rank': Rank.LIEUTENANT,
                'age': 65,
                'specialization': 'Navigation',
                'years_experience': 9,
                'is_active': True
            },
            {
                'member_id': 'Aljohnson',
                'name': 'Alice Johnson',
                'rank': Rank.OFFICER,
                'age': 23,
                'specialization': 'Engineering',
                'years_experience': 5,
                'is_active': True
            }
        ],
        'mission_status': 'in progress',
        'budget_millions': 2500.0
    }
    # Wrong values (No Commander or Captain)
    mission3 = {
        'mission_id': 'M2024_Mars',
        'mission_name': 'Mars Colony Establishment',
        'destination': 'Mars',
        'launch_date': datetime.now(),
        'duration_days': 900,
        'crew': [
            {
                'member_id': 'Eulafrance',
                'name': 'Eude Lafrance',
                'rank': Rank.CADET,
                'age': 69,
                'specialization': 'Cleaning',
                'years_experience': 12,
                'is_active': True
            },
            {
                'member_id': 'Josmithju',
                'name': 'John Smith Junior',
                'rank': Rank.LIEUTENANT,
                'age': 68,
                'specialization': 'Navigation',
                'years_experience': 9,
                'is_active': True
            },
            {
                'member_id': 'Aljohnson',
                'name': 'Alice Johnson',
                'rank': Rank.OFFICER,
                'age': 23,
                'specialization': 'Engineering',
                'years_experience': 5,
                'is_active': True
            }
        ],
        'mission_status': 'in progress',
        'budget_millions': 2500.0
    }
    # Wrong values (No experienced)
    mission4 = {
        'mission_id': 'M2024_Mars',
        'mission_name': 'Mars Colony Establishment',
        'destination': 'Mars',
        'launch_date': datetime.now(),
        'duration_days': 900,
        'crew': [
            {
                'member_id': 'roandrie',
                'name': 'Romain Andrieux',
                'rank': Rank.CAPTAIN,
                'age': 24,
                'specialization': 'Mission Command',
                'years_experience': 1,
                'is_active': True
            },
            {
                'member_id': 'Rruiz',
                'name': 'Remy Ruiz',
                'rank': Rank.OFFICER,
                'age': 18,
                'specialization': 'Navigation',
                'years_experience': 0,
                'is_active': True
            },
            {
                'member_id': 'Anacharp',
                'name': 'Ana Charpentier',
                'rank': Rank.CADET,
                'age': 23,
                'specialization': 'Engineering',
                'years_experience': 0,
                'is_active': True
            }
        ],
        'mission_status': 'in progress',
        'budget_millions': 2500.0
    }
    # Wrong values (Crew not active)
    mission5 = {
        'mission_id': 'M2024_Mars',
        'mission_name': 'Mars Colony Establishment',
        'destination': 'Mars',
        'launch_date': datetime.now(),
        'duration_days': 900,
        'crew': [
            {
                'member_id': 'Saconnor',
                'name': 'Sarah Connor',
                'rank': Rank.COMMANDER,
                'age': 35,
                'specialization': 'Mission Command',
                'years_experience': 12,
                'is_active': False
            },
            {
                'member_id': 'Josmith',
                'name': 'John Smith',
                'rank': Rank.LIEUTENANT,
                'age': 65,
                'specialization': 'Navigation',
                'years_experience': 9,
                'is_active': True
            },
            {
                'member_id': 'Aljohnson',
                'name': 'Alice Johnson',
                'rank': Rank.OFFICER,
                'age': 23,
                'specialization': 'Engineering',
                'years_experience': 5,
                'is_active': True
            }
        ],
        'mission_status': 'in progress',
        'budget_millions': 2500.0
    }

    print("Mission 1:")
    mission = create_mission(mission1)
    if mission is not None:
        print_information(mission)

    print("\nMission 2:")
    mission = create_mission(mission2)
    if mission is not None:
        print_information(mission)

    print("\nMission 3:")
    mission = create_mission(mission3)
    if mission is not None:
        print_information(mission)

    print("\nMission 4:")
    mission = create_mission(mission4)
    if mission is not None:
        print_information(mission)

    print("\nMission 5:")
    mission = create_mission(mission5)
    if mission is not None:
        print_information(mission)


if __name__ == "__main__":
    main()
