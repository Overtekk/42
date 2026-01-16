from typing import Any, Dict, Self
from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from enum import Enum


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(min_length=0, max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def verification(self) -> Self:
        if not self.contact_id.startswith('AC'):
            raise ValueError("Contact ID must start with \"AC\""
                                  "(Alien Contact)")
        return self


def contact_report(data: Dict[str, Any]) -> AlienContact | None:
    try:
        report_result = AlienContact(**data)
        return report_result
    except ValidationError as e:
        print(f"Invalid contact report\n{type(e).__name__}", end=" - ")
        for item in e.errors():
            print(f"{item['loc']}: {item['msg']}")
        return None


def print_result(report: AlienContact) -> None:
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
        'signal_strength': 2,
        'duration_minutes': 45,
        'witness_count': 1,
        'is_verified': False
    }

    print("-- Contact 1 --")
    report = contact_report(contact1)
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
