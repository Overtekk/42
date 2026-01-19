from typing import Any, Dict, Self
from datetime import datetime
from enum import Enum
import sys


try:
    from pydantic import BaseModel, Field, ValidationError, model_validator
except ModuleNotFoundError as e:
    print(f"\n{type(e).__name__}: missing dependency {e.name}.\nTry to install"
          " it first using 'pip install pydantic'", file=sys.stderr)
    exit(2)


class ContactType(Enum):
    """
    Enumeration defining the allowed methods of contact.
    """
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    """
    Inherits from BaseModel and define a AlienContact class with specific
    types.

    contact_id: (str), 5-15 characters.
    timestamp: (DateTime).
    location: (str), 3-100 characters.
    contact_type: (ContactType).
    signal_strength: (float), 0.0-10.0.
    duration_minutes: (int), 1-1440 minutes.
    witness_count: (int), 1-100 people.
    message_received: (Optional), (str), 500 characters max.
    is_verified: (bool), defaults to False.

    """
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(min_length=0, max_length=500,
                                         default=None)
    is_verified: bool = False

    @model_validator(mode='after')
    def verification(self) -> Self:
        """Perform custom validation checks on the model attributes. This
        function will be called everytime we tried to create an AlienContact
        object.

        === Returns ===
            - Self: The object itself if all validations pass.
        """

        if not self.contact_id.startswith('AC'):
            raise ValueError("Contact ID must start with \"AC\""
                             "(Alien Contact)")

        if self.contact_type == ContactType.PHYSICAL:
            if not self.is_verified:
                raise ValueError("Physical contact reports must be verified")

        if self.contact_type == ContactType.TELEPATHIC:
            if not self.witness_count >= 3:
                raise ValueError("Telepathic contact requires at least "
                                 "3 witnesses")

        if self.signal_strength > 7.0:
            if self.message_received is None:
                raise ValueError("Strong signals (> 7.0) should include "
                                 "received messages")
        return self


def contact_report(data: Dict[str, Any]) -> AlienContact | None:
    """"Create a contact report using a dictionary.

    === Args ===
        - data (Dict[str, Any]): A dictionary containing contact data. Keys
          must match the AlienContact field names.

    === Returns ===
        - AlienContact: the object if data are validated.
        - None: none if data are not validated.
    """
    try:
        report_result = AlienContact(**data)
        return report_result
    except (ValidationError, ValueError) as e:
        print(f"Invalid contact report\n{type(e).__name__}", end=" - ")
        for item in e.errors():
            print(f"{item['loc']}: {item['msg']}")
        return None


def print_result(report: AlienContact) -> None:
    """"Print informations about the AlienContact.

    === Args ===
        - report (AlienContact): The AlienContact object and validated.
    """
    print("Valid contact report:")
    print(f"ID: {report.contact_id}")
    print(f"Last contact: {report.timestamp}")
    print(f"Type: {report.contact_type}")
    print(f"Location: {report.location}")
    print(f"Signal: {report.signal_strength}/10")
    print(f"Duration: {report.duration_minutes} minutes")
    print(f"Witnesses: {report.witness_count}")
    if report.message_received is not None:
        print(f"Message: {report.message_received}")
    print(f"Report verified: {report.is_verified}")


def main() -> None:
    print("Alien Contact Log Validation")
    print("======================================")

    # Good values
    contact1 = {
        'contact_id': 'AC_2024_001',
        'timestamp': '2003-04-23T22:42:06Z',
        'contact_type': ContactType.RADIO,
        'location': 'Area 51, Nevada',
        'signal_strength': 8.5,
        'duration_minutes': 45,
        'witness_count': 5,
        'message_received': 'Greetings from Zeta Reticuli',
        'is_verified': True
    }

    # Good values (without message and verified)
    contact1_bis = {
        'contact_id': 'AC_2024_001',
        'timestamp': '2003-04-23T22:42:06Z',
        'contact_type': ContactType.RADIO,
        'location': 'Area 51, Nevada',
        'signal_strength': 2.5,
        'duration_minutes': 45,
        'witness_count': 5,
    }

    # Bad values
    contact2 = {
        'contact_id': 'uwu',
        'timestamp': 29122025,
        'contact_type': 'radio',
        'location': 41,
        'signal_strength': 10.1,
        'duration_minutes': -45,
        'witness_count': 102,
        'message_received': False,
    }

    # Bad values (validation rules - ID)
    contact3 = {
        'contact_id': '2024_001',
        'timestamp': '2003-04-23T22:42:06Z',
        'contact_type': ContactType.RADIO,
        'location': 'Area 51, Nevada',
        'signal_strength': 8.5,
        'duration_minutes': 45,
        'witness_count': 5,
        'message_received': 'Greetings from Zeta Reticuli',
        'is_verified': True
    }

    # Bad values (validation rules - Physical contact)
    contact4 = {
        'contact_id': 'AC_2024_001',
        'timestamp': '2003-04-23T22:42:06Z',
        'contact_type': ContactType.PHYSICAL,
        'location': 'Area 51, Nevada',
        'signal_strength': 8.5,
        'duration_minutes': 45,
        'witness_count': 5,
        'message_received': 'Greetings from Zeta Reticuli',
        'is_verified': False
    }

    # Bad values (validation rules - Telepathic contact)
    contact5 = {
        'contact_id': 'AC_2024_001',
        'timestamp': '2003-04-23T22:42:06Z',
        'contact_type': ContactType.TELEPATHIC,
        'location': 'Area 51, Nevada',
        'signal_strength': 8.5,
        'duration_minutes': 45,
        'witness_count': 1,
        'message_received': 'Greetings from Zeta Reticuli',
        'is_verified': True
    }

    # Bad values (validation rules - Strong signals)
    contact6 = {
        'contact_id': 'AC_2024_001',
        'timestamp': '2003-04-23T22:42:06Z',
        'contact_type': ContactType.TELEPATHIC,
        'location': 'Area 51, Nevada',
        'signal_strength': 7.2,
        'duration_minutes': 45,
        'witness_count': 1,
        'is_verified': False
    }

    print("-- Contact 1 --")
    report = contact_report(contact1)
    if report is not None:
        print_result(report)

    print("\n-- Contact 1_bis --")
    report = contact_report(contact1_bis)
    if report is not None:
        print_result(report)

    print("\n-- Contact 2 --")
    report = contact_report(contact2)
    if report is not None:
        print_result(report)

    print("\n-- Contact 3 --")
    report = contact_report(contact3)
    if report is not None:
        print_result(report)

    print("\n-- Contact 4 --")
    report = contact_report(contact4)
    if report is not None:
        print_result(report)

    print("\n-- Contact 5 --")
    report = contact_report(contact5)
    if report is not None:
        print_result(report)

    print("\n-- Contact 6 --")
    report = contact_report(contact6)
    if report is not None:
        print_result(report)


if __name__ == "__main__":
    main()
