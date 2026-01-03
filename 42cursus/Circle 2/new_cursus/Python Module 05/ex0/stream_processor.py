from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional  # noqa: F401


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

        try:
            if not isinstance(data, list):
                raise ValueError
        except ValueError:
            print("[ERROR] Data send is not a list")
            return False

        if len(data) == 0:
            print("[ERROR] Data is empty")
            return False

        for number in data:
            try:
                float(number)
            except (ValueError, TypeError):
                print("[ERROR] Data send is not numeric")
                return False

        return True

    def process(self, data: List[int]) -> str:
        """
        Calculates sum and average of the numeric list.
        """
        if not self.validate(data):
            return self.format_output("Error detected. Stopping.")

        total = 0
        for number in data:
            total += float(number)

        avg = total / len(data)

        result_str = (f"Processed {len(data)} numeric values, sum={total}, "
                      f"avg={avg}")
        return self.format_output(result_str)

    def format_output(self, result: str) -> str:
        """
        Formats the output specifically for Numeric data.
        """
        return f"Output: {result}"


class TextProcessor(DataProcessor):
    """
    Specialized processor for handling text.
    """

    def validate(self, data: str) -> bool:
        """
        Checks if data is a string.
        """

        try:
            if not isinstance(data, str):
                raise ValueError
        except ValueError:
            print("ERROR: Data is not a string")
            return False

        return True

    def process(self, data: str) -> str:
        """
        Calculates characters and words of a string.
        """

        if not self.validate(data):
            result_str = "Error detected. Stopping."
            return self.format_output(result_str)

        characters_count = len(data)
        words_count = len(data.split())

        result_str = (f"Processed text: {characters_count} characters, "
                      f"{words_count} words")

        return self.format_output(result_str)

    def format_output(self, result: str) -> str:
        """
        Formats the output specifically for Text data.
        """
        return f"Output: {result}"


class LogProcessor(DataProcessor):
    """Class for log"""

    def validate(self, data: str) -> bool:
        """
        Checks if data is a string.
        """

        try:
            if not isinstance(data, str):
                raise ValueError
        except ValueError:
            print("ERROR: Data is not a string")
            return False

        if ":" not in data:
            print("ERROR: Invalid format. Missing ':' separator. Please use: "
                  "'LOGTYPE': [msg]\nValid 'LOGTYPE' = 'ERROR','WARN','INFO',"
                  "'DEBUG','LOG'")
            return False

        valid_logtype = ["ERROR", "INFO", "WARN", "DEBUG", "LOG"]
        alert = data.split(":")
        log_type = alert[0].strip()
        if log_type not in valid_logtype:
            print("ERROR: Data is not log type. Please use: 'LOGTYPE': [msg]"
                  "\nValid 'LOGTYPE' = 'ERROR','WARN','INFO','DEBUG','LOG'")
            return False

        return True

    def process(self, data: str) -> str:
        """
        Proceed correct log entry.
        """

        if not self.validate(data):
            result_str = "Error detected. Stopping."
            return self.format_output(result_str)

        alert = data.split(":")
        logtype_alert = ["ERROR", "WARN"]

        if alert[0] in logtype_alert:
            alert_type = "[ALERT]"
        else:
            alert_type = "[INFO]"

        result_str = f"{alert_type} {alert[0]} level detected:{alert[1]}"

        return self.format_output(result_str)

    def format_output(self, result: str) -> str:
        """
        Formats the output specifically for Log data.
        """
        return f"Output: {result}"


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

        print("Validation", end=": ")
        if processor.validate(data_num):
            print("Numeric data verified")
            print(processor.process(data_num))
        else:
            print(processor.format_output("Error detected. Stopping.\n"))

        # Empty data
        print("Initializing Numeric Processor (*empty list*)...")
        data_num = []
        print(f"Processing data: {data_num}")
        processor = NumericProcessor()

        print("Validation", end=": ")
        if processor.validate(data_num):
            print("Numeric data verified")
            print(processor.process(data_num))
        else:
            print(processor.format_output("Error detected. Stopping.\n"))

        # Not sending list
        print("Initializing Numeric Processor (*not a list*)...")
        data_num = "bonjour toi"
        print(f"Processing data: {data_num}")
        processor = NumericProcessor()

        print("Validation", end=": ")
        if processor.validate(data_num):
            print("Numeric data verified")
            print(processor.process(data_num))
        else:
            print(processor.format_output("Error detected. Stopping."))

    # === Testing Text Processor === #
    elif tester == "text":
        # Invalid data
        print("Initializing Text Processor (*invalid data*)...")
        data_txt = [1, 2, 'abc', 4, 5]
        print(f"Processing data: {data_txt}")
        processor = TextProcessor()

        print("Validation", end=": ")
        if processor.validate(data_txt):
            print("Text data verified")
            print(processor.process(data_txt))
        else:
            print(processor.format_output("Error detected. Stopping.\n"))

        # Empty string (Valid)
        print("Initializing Text Processor (*empty data*)...")
        data_txt = ""
        print(f"Processing data: {data_txt}")
        processor = TextProcessor()

        print("Validation", end=": ")
        if processor.validate(data_txt):
            print("Text data verified")
            print(processor.process(data_txt))
        else:
            print(processor.format_output("Error detected. Stopping.\n"))

    # === Testing Log Processor === #
    elif tester == "log":
        # Invalid data
        print("Initializing Log Processor (*invalid data*)...")
        data_log = [1, 2, 'abc', 4, 5]
        print(f"Processing data: {data_log}")
        processor = LogProcessor()

        print("Validation", end=": ")
        if processor.validate(data_log):
            print("Log entry verified")
            print(processor.process(data_log))
        else:
            print(processor.format_output("Error detected. Stopping.\n"))

        # Invalid Log Type
        print("Initializing Log Processor (*invalid log type*)...")
        data_log = "\"EROR: Hello Word\""
        print(f"Processing data: {data_log}")
        processor = LogProcessor()

        print("Validation", end=": ")
        if processor.validate(data_log):
            print("Log entry verified")
            print(processor.process(data_log))
        else:
            print(processor.format_output("Error detected. Stopping.\n"))

        # No Log Type
        print("Initializing Log Processor (*no log type*)...")
        data_log = ""
        print(f"Processing data: {data_log}")
        processor = LogProcessor()

        print("Validation", end=": ")
        if processor.validate(data_log):
            print("Log entry verified")
            print(processor.process(data_log))
        else:
            print(processor.format_output("Error detected. Stopping.\n"))

        # Bad log type
        print("Initializing Log Processor (*bad log type*)...")
        data_log = " ERROR Connection timeout"
        print(f"Processing data: {data_log}")
        processor = LogProcessor()

        print("Validation", end=": ")
        if processor.validate(data_log):
            print("Log entry verified")
            print(processor.process(data_log))
        else:
            print(processor.format_output("Error detected. Stopping.\n"))

    else:
        print("Invalid name. Please use: 'numeric', 'text' or 'log'.")


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
    print("Validation", end=": ")
    if processor.validate(data_num):
        print("Numeric data verified")
        result = processor.process(data_num)
        print(result)
    else:
        print(processor.format_output("Error detected. Stopping."))

    # If you want to test errors, remove the comment from the function call.
    # errors_tester("numeric")

    # === Testing Text Processor === #

    print("\nInitializing Text Processor...")
    data_txt = "Hello Nexus World"
    print(f"Processing data: \"{data_txt}\"")
    processor = TextProcessor()
    print("Validation", end=": ")
    if processor.validate(data_txt):
        print("Text data verified")
        result = processor.process(data_txt)
        print(result)
    else:
        print(processor.format_output("Error detected. Stopping."))

    # If you want to test errors, remove the comment from the function call.
    # errors_tester("text")

    # === Testing Log Processor === #

    print("\nInitializing Log Processor...")
    data_log = "ERROR: Connection timeout"
    print(f"Processing data: \"{data_log}\"")
    processor = LogProcessor()

    print("Validation", end=": ")
    if processor.validate(data_log):
        print("Log entry verified")
        result = processor.process(data_log)
        print(result)
    else:
        print(processor.format_output("Error detected. Stopping."))

    # If you want to test errors, remove the comment from the function call.
    # errors_tester("log")

    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")

    data = [
        (NumericProcessor(), [3, 2, 1]),
        (TextProcessor(), "Hey Mouse!!!"),
        (LogProcessor(), "INFO: System ready")
    ]

    i = 1
    for processor, data in data:
        result = processor.process(data)
        print(f"Result {i}: {result}")
        i += 1

    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
