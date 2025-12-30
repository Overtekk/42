from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataProcessor(ABC):
    """Abstract base class"""

    @abstractmethod
    def process(self, data: Any) -> str:
        """Abstract method for processing"""
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Abstract method for validating input"""
        pass

    def format_output(self, result: str) -> str:
        """Format method ouput"""
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    """Class for numeric"""

    def validate(self, data: List[int]) -> bool:

        try:
            isinstance(data, list)
        except ValueError:
            print("ERROR: Data send is not a list")
            return False

        try:
            len(data)
        except ValueError:
            print("ERROR: Data is empty")

        try:
            for number in data:
                number = int(number)
        except ValueError:
            print("ERROR: Data send is not numeric")
            return False

        print("Validation: Numeric data verified")
        return True

    def process(self, data: Any) -> str:

        if not self.validate(data):
            return "[ERROR] Error detected. Stopping."

        sum = 0
        for number in data:
            sum += number

        avg = sum / len(data)

        return f"Processed {len(data)} numeric values, sum={sum}, avg={avg}"

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class TextProcessor(DataProcessor):
    """Class for text"""
    pass


class LogProcessor(DataProcessor):
    """Class for log"""
    pass


def main() -> None:
    """
    Program entry point.
    """

    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    print("Initializing Numeric Processor...")
    data_num = [1, 2, 3, 4, 5]
    print(f"Processing data: {data_num}")
    processor = NumericProcessor()
    result = processor.process(data_num)
    print(result)

if __name__ == "__main__":
    main()
