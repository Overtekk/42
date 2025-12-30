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

    def validate(self, data: Any) -> bool:

        try:
            isinstance(data, list)
        except ValueError:
            print("ERROR: Data send is not a list")
            return False

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

        sum_txt = f"sum={sum}, "
        avg_txt = f"avg={avg}"

        return sum_txt + avg_txt


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

    data_num = [1, 2, 3, 4, 5]
    processor = NumericProcessor()
    result = processor.process(data_num)
    print(result)

if __name__ == "__main__":
    main()
