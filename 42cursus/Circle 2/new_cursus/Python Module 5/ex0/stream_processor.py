from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataProcessor(ABC):
    """
    Abstract base class defining the interface for all data processors.
    Enforces a consistent structure for processing different data types.
    """

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """
        Validates if the input data is suitable for this processor.

        == Args ==
            - data (Any): The input data to check.

        == Returns ==
            - bool: True if data is valid, False otherwise.
        """
        pass

    @abstractmethod
    def process(self, data: Any) -> str:
        """
        Processes the input data and returns a formatted result string.

        == Args ==
            - data (Any): The input data to process.

        == Returns ==
            - str: The processed and formatted output.
        """
        pass

    def format_output(self, result: str) -> str:
        """
        Formats the processing result with a standard prefix.

        == Args ==
            - result (str): The raw result string from processing.

        == Returns ==
            - str: The formatted string ready for display.
        """
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    """
    Specialized processor for handling lists of numeric values.
    """

    def validate(self, data: List[int]) -> bool:
        """
        Checks if data is a non-empty list of numbers.
        """
        if not isinstance(data, list):
            print("ERROR: Data send is not a list")
            return False

        if len(data) == 0:
            print("ERROR: Data is empty")
            return False

        for number in data:
            try:
                float(number)
            except (ValueError, TypeError):
                print("ERROR: Data send is not numeric")
                return False

        print("Validation: Numeric data verified")
        return True

    def process(self, data: List[int]) -> str:
        """
        Calculates sum and average of the numeric list.
        """
        if not self.validate(data):
            result_str = "Error detected. Stopping."
            return self.format_output(result_str)

        total = 0
        for number in data:
            total += number

        avg = total / len(data)

        result_str = (f"Processed {len(data)} numeric values, sum={total}, "
                      f"avg={avg}")
        return self.format_output(result_str)


class TextProcessor(DataProcessor):
    """
    Specialized processor for handling text.
    """

    def validate(self, data: str) -> bool:
        """
        Checks if data is a string.
        """

        try:
            str(data)
        except (ValueError, TypeError):
            print("ERROR: Data send a text")
            return False

    def process(self, data: List[int]) -> str:
        """
        Calculates characters and words of a string.
        """

        result_str = "lol"

        return result_str

class LogProcessor(DataProcessor):
    """Class for log"""
    pass


def errors_tester(tester: str) -> None:
    """
    Function to test errors handling for invalid data.

    == Arguments ==
        - tester (str): The name of the processor to test.

    == Returns ==
        - None: This function only print to stdout.
    """

    print(f"\n=== Testing errors for {tester} processor ===\n")

    # === Testing Numeric Processor === #
    if tester == "numeric":
        # Invalid data
        print("Initializing Numeric Processor (*invalid data*)...")
        data_num = [1, 2, "abc", 4, 5]
        print(f"Processing data: {data_num}")
        processor = NumericProcessor()
        result = processor.process(data_num)
        print(f"{result}\n")

        # Empty data
        print("Initializing Numeric Processor (*empty list*)...")
        data_num = []
        print(f"Processing data: {data_num}")
        processor = NumericProcessor()
        result = processor.process(data_num)
        print(f"{result}\n")

        # Not sending list
        print("Initializing Numeric Processor (*not a list*)...")
        data_num = "bonjour toi"
        print(f"Processing data: {data_num}")
        processor = NumericProcessor()
        result = processor.process(data_num)
        print(f"{result}")

    # === Testing Text Processor === #
    elif tester == "text":
        # Invalid data
        print("\nInitializing Text Processor (*invalid data*)...")
        data_txt = [1, 2, "abc", 4, 5]
        print(f"Processing data: {data_txt}")
        processor = TextProcessor()
        result = processor.process(data_txt)
        print(f"{result}\n")

    else:
        print("Invalid name. Please use: 'numeric', 'text', 'log' or "
              "'polymorphic'.")


def main() -> None:
    """
    Program entry point.
    """

    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    # === Testing Numeric Processor === #

    print("Initializing Numeric Processor...")
    data_num = [1, 2, 3, 4, 5]
    print(f"Processing data: {data_num}")
    processor = NumericProcessor()
    result = processor.process(data_num)
    print(f"{result}")

    # If you want to test errors, remove the comment from the function call.
    # errors_tester("numeric")

    # === Testing Text Processor === #

    print("\nInitializing Text Processor...")
    data_txt = "Hello Nexus World"
    print(f"Processing data: {data_txt}")
    processor = TextProcessor()
    result = processor.process(data_txt)
    print(f"{result}")

    # If you want to test errors, remove the comment from the function call.
    errors_tester("text")


if __name__ == "__main__":
    main()
