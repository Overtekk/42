from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum


class ContactType(Enum):
    pass


class AlienContact(BaseModel):
    contact_id = str = Field(min_length=5, max_length=15)
    timestamp = datetime
    location = str = Field(min_length=3, max_length=100)
    contact_type = ContactType


def main() -> None:
    print("Alien Contact Log Validation")
    print("======================================")


if __name__ == "__main__":
    main()
