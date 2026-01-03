from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    """
    Abstract base class representing a generic data stream.

    This class defines the interface that all specialized streams must
    implement.
    It provides a structure for processing data batches, filtering content,
    and retrieving stream statistics.
    """

    def __init__(self, stream_id: str, stream_type: str) -> None:
        """
        Initialize the DataStream instance.

        === Args ===
            stream_id (str): The unique identifier for the stream.
            stream_type (str): The category/type of the stream.
        """
        self.stream_id = stream_id
        self.stream_type = stream_type

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """
        Process a batch of data. This method must be overridden by subclasses.

        === Args ===
            data_batch (List[Any]): A list of any data items to process.

        === Returns ===
            str: A formatted string summarizing the processing result.
        """
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """
        Filter the data batch based on a specific criteria.

        === Args ===
            data_batch (List[Any]): The original list of data.
            criteria (Optional[str]): The keyword to filter by.
            Defaults to None.

        === Returns ===
            List[Any]: The filtered list of data.
        """
        if criteria is not None:
            data_batch_filtered = [item for item in data_batch
                                   if criteria in item]
            return data_batch_filtered

        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """
        Retrieve statistics and metadata about the stream.

        === Returns ===
            Dict[str, Union[str, int, float]]: A dictionary containing
            the stream ID and type.
        """
        stat = {"id": self.stream_id, "type": self.stream_type}
        return stat


class SensorStream(DataStream):
    """
    Specialized stream handler for environmental sensor data.
    """

    def __init__(self, stream_id: str) -> None:
        """
        Initialize a SensorStream with a fixed type 'Environmental Data'.

        === Args ===
            stream_id (str): The unique identifier for the sensor.
        """
        super().__init__(stream_id=stream_id, stream_type="Environmental Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        """
        Process sensor data to extract temperature readings.

        === Args ===
            data_batch (List[Any]): List of strings (e.g., 'temp:22.5').

        === Returns ===
            str: Analysis string with the count and average temperature.
        """
        temperature = None

        for word in data_batch:
            if word.startswith("temp"):
                word_parts = word.split(":")
                if len(word_parts) == 2:
                    try:
                        temperature = float(word_parts[1])
                    except ValueError:
                        pass
                break

        if temperature is not None:
            return (f"Sensor analysis: {len(data_batch)} readings processed, "
                    f"avg temp: {temperature}°C")
        else:
            return (f"Sensor analysis: {len(data_batch)} readings processed, "
                    f"avg temp: data not found")


class TransactionStream(DataStream):
    """
    Specialized stream handler for transaction data.
    """

    def __init__(self, stream_id: str) -> None:
        """
        Initialize a TransactionStream with a fixed type 'Financial Data'.

        === Args ===
            stream_id (str): The unique identifier for the sensor.
        """
        super().__init__(stream_id=stream_id, stream_type="Financial Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        """
        Process transaction data to calcule net flow and operations.

        === Args ===
            data_batch (List[Any]): List of strings (e.g., 'buy:100').

        === Returns ===
            str: Analysis string with the operations and the net flow.
        """

        total = 0
        operations = ["buy", "sell"]
        valid_operation = 0

        if len(data_batch) == 0:
            return "Transaction analysis: 0 operations, net flow: +0 unit"

        for word in data_batch:
            word_parts = word.split(":")
            if len(word_parts) == 2:
                if word_parts[0] in operations:
                    valid_operation += 1
                try:
                    if word_parts[0] == "buy":
                        total += float(word_parts[1])
                    elif word_parts[0] == "sell":
                        total -= float(word_parts[1])
                except ValueError:
                    valid_operation -= 1

        if total >= 0:
            sign = "+"
        else:
            sign = ""

        return (f"Transaction analysis: {valid_operation} operations, net "
                f"flow: {sign}{total:.0f} units")


class EventStream(DataStream):
    """
    Specialized stream handler for event data.
    """

    def __init__(self, stream_id: str) -> None:
        """
        Initialize a EventStream with a fixed type 'System Events'.

        === Args ===
            stream_id (str): The unique identifier for the sensor.
        """
        super().__init__(stream_id=stream_id, stream_type="System Events")

    def process_batch(self, data_batch: List[Any]) -> str:
        """
        Process system data to calcule how many events and error.

        === Args ===
            data_batch (List[Any]): List of strings (e.g., 'login').

        === Returns ===
            str: Analysis string with number of events and error.
        """

        event_type = ["login", "error", "logout", "warn", "info"]
        event_count = 0
        error_count = 0

        for event in data_batch:
            if event in event_type:
                event_count += 1
            if event == "error":
                error_count += 1

        if error_count == 1:
            return (f"Event analysis: {event_count} events, {error_count}"
                    " error detected")
        elif error_count > 1:
            return (f"Event analysis: {event_count} events, {error_count}"
                    " errors detected")
        else:
            return (f"Event analysis: {event_count} events, no error detected")


class StreamProcessor():
    """
    Manager class to handle multiple DataStream instances polymorphically.
    """

    def __init__(self):
        """
        Initialize the StreamProcessor with an empty list of streams.
        """
        self.streams = []

    def add_streams(self, stream: DataStream) -> None:
        """
        Add a DataStream object to the processor's list.

        === Args ===
            stream (DataStream): The stream instance to add.
        """
        self.streams.append(stream)

    def process(self, batch_data: Dict[str, List[any]]) -> None:
        """
        Process a batch of mixed data types for all registered streams.

        === Args ===
            batch_data (Dict[str, List[any]]): Dictionary where keys are
            the stream ID and values are list of data to process.
        """
        print("Batch 1 Results:")

        for stream in self.streams:
            stream_data = batch_data.get(stream.stream_id)
            if stream_data is not None:
                result = stream.process_batch(stream_data)
                print(f"- {result}")
            else:
                print(f"- No data found for stream {stream.stream_id}")


def error_tester(tester: str) -> None:
    """
    Function to test errors handling for invalid data.

    == Arguments ==
        - tester (str): The name of the processor to test.

    == Returns ==
        - None: This function only print to stdout.
    """

    print(f"\n=== Testing errors for {tester} processor ===\n")

    # === Testing Sensor Stream ===
    if tester == "sensor":
        print("Testing with empty list")
        data_sensor = []
        formatted_data = ", ".join(data_sensor)

        processor = SensorStream(stream_id="SENSOR_002")
        stats = processor.get_stats()
        result = processor.process_batch(data_sensor)

        print(f"Stream ID: {stats.get('id')}, Type: {stats.get('type')}")
        print(f"Processing sensor batch: [{formatted_data}]")
        print(result)

        print("\nTesting with no 'temp'")
        data_sensor = ["humidity:65", "pressure:1013"]
        formatted_data = ", ".join(data_sensor)

        processor = SensorStream(stream_id="SENSOR_003")
        stats = processor.get_stats()
        result = processor.process_batch(data_sensor)

        print(f"Stream ID: {stats.get('id')}, Type: {stats.get('type')}")
        print(f"Processing sensor batch: [{formatted_data}]")
        print(result)

        print("\nTesting with bad 'temp' value")
        data_sensor = ["temp:hey", "humidity:65", "pressure:1013"]
        formatted_data = ", ".join(data_sensor)

        processor = SensorStream(stream_id="SENSOR_004")
        stats = processor.get_stats()
        result = processor.process_batch(data_sensor)

        print(f"Stream ID: {stats.get('id')}, Type: {stats.get('type')}")
        print(f"Processing sensor batch: [{formatted_data}]")
        print(result)

        print("\n=== Errors Testing Completed ===")

    # === Testing Transaction Stream ===
    elif tester == "transaction":
        print("Testing with empty list")
        data_transac = []
        formatted_data = ", ".join(data_transac)

        processor = TransactionStream(stream_id="TRANS_002")
        stats = processor.get_stats()
        result = processor.process_batch(data_transac)

        print(f"Stream ID: {stats.get('id')}, Type: {stats.get('type')}")
        print(f"Processing transaction batch: [{formatted_data}]")
        print(result)

        print("\nTesting with only sell")
        data_transac = ["sell:100", "sell:150", "sell:75"]
        formatted_data = ", ".join(data_transac)

        processor = TransactionStream(stream_id="TRANS_003")
        stats = processor.get_stats()
        result = processor.process_batch(data_transac)

        print(f"Stream ID: {stats.get('id')}, Type: {stats.get('type')}")
        print(f"Processing transaction batch: [{formatted_data}]")
        print(result)

        print("\nTesting with bad data")
        data_transac = ["temp:22.5", "humidity:65", "pressure:1013"]
        formatted_data = ", ".join(data_transac)

        processor = TransactionStream(stream_id="TRANS_004")
        stats = processor.get_stats()
        result = processor.process_batch(data_transac)

        print(f"Stream ID: {stats.get('id')}, Type: {stats.get('type')}")
        print(f"Processing transaction batch: [{formatted_data}]")
        print(result)

        print("\nTesting with no numbers")
        data_transac = ["buy:abc", "sell:abc", "buy:75"]
        formatted_data = ", ".join(data_transac)

        processor = TransactionStream(stream_id="TRANS_005")
        stats = processor.get_stats()
        result = processor.process_batch(data_transac)

        print(f"Stream ID: {stats.get('id')}, Type: {stats.get('type')}")
        print(f"Processing transaction batch: [{formatted_data}]")
        print(result)

        print("\n=== Errors Testing Completed ===")

    # === Testing Event Stream ===
    elif tester == "event":
        print("Testing with empty list")
        data_event = []
        formatted_data = ", ".join(data_event)

        processor = EventStream(stream_id="EVENT_002")
        stats = processor.get_stats()
        result = processor.process_batch(data_event)

        print(f"Stream ID: {stats.get('id')}, Type: {stats.get('type')}")
        print(f"Processing event batch: [{formatted_data}]")
        print(result)

        print("\nTesting with bad data")
        data_event = ["buy:100", "temp:22.2"]
        formatted_data = ", ".join(data_event)

        processor = EventStream(stream_id="EVENT_003")
        stats = processor.get_stats()
        result = processor.process_batch(data_event)

        print(f"Stream ID: {stats.get('id')}, Type: {stats.get('type')}")
        print(f"Processing event batch: [{formatted_data}]")
        print(result)

        print("\nTesting with mixed data")
        data_event = ["buy:100", "temp:22.2", "error", "logout"]
        formatted_data = ", ".join(data_event)

        processor = EventStream(stream_id="EVENT_003")
        stats = processor.get_stats()
        result = processor.process_batch(data_event)

        print(f"Stream ID: {stats.get('id')}, Type: {stats.get('type')}")
        print(f"Processing event batch: [{formatted_data}]")
        print(result)

        print("\nTesting with multiple errors")
        data_event = ["error", "error", "error", "logout", "error"]
        formatted_data = ", ".join(data_event)

        processor = EventStream(stream_id="EVENT_003")
        stats = processor.get_stats()
        result = processor.process_batch(data_event)

        print(f"Stream ID: {stats.get('id')}, Type: {stats.get('type')}")
        print(f"Processing event batch: [{formatted_data}]")
        print(result)

        print("\n=== Errors Testing Completed ===")

    else:
        print("Invalid name. Please use: 'numeric', 'text', 'log' or "
              "'polymorphic'.")


def main() -> None:
    """
    Program entry point.
    """

    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    #  === Sensor Stream ===
    print("Initializing Sensor Stream...")

    data_sensor = ["temp:22.5", "humidity:65", "pressure:1013"]
    formatted_data = ", ".join(data_sensor)

    processor_sensor = SensorStream(stream_id="SENSOR_001")
    stats = processor_sensor.get_stats()
    result = processor_sensor.process_batch(data_sensor)

    print(f"Stream ID: {stats.get('id')}, Type: {stats.get('type')}")
    print(f"Processing sensor batch: [{formatted_data}]")
    print(result)

    # error_tester("sensor")

    # === Transaction Stream ===
    print("\nInitializing Transaction Stream...")
    data_transac = ["buy:100", "sell:150", "buy:75"]
    formatted_data = ", ".join(data_transac)

    processor_transaction = TransactionStream(stream_id="TRANS_001")
    stats = processor_transaction.get_stats()
    result = processor_transaction.process_batch(data_transac)

    print(f"Stream ID: {stats.get('id')}, Type: {stats.get('type')}")
    print(f"Processing transaction batch: [{formatted_data}]")
    print(result)

    # error_tester("transaction")

    # === Event Stream ===
    print("\nInitializing Event Stream...")
    data_event = ["login", "error", "logout"]
    formatted_data = ", ".join(data_event)

    processor_event = EventStream(stream_id="EVENT_001")
    stats = processor_event.get_stats()
    result = processor_event.process_batch(data_event)

    print(f"Stream ID: {stats.get('id')}, Type: {stats.get('type')}")
    print(f"Processing event batch: [{formatted_data}]")
    print(result)

    # error_tester("event")

    # === Polymorphic Stream Processing ===
    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")

    processor = StreamProcessor()
    processor.add_streams(processor_sensor)
    processor.add_streams(processor_transaction)
    processor.add_streams(processor_event)

    batch_data = {
        "SENSOR_001": ["temp:22.5", "humidity:65"],
        "TRANS_001": ["buy:100", "sell:150", "buy:75", "buy:20"],
        "EVENT_001": ["login", "error", "logout"]
    }

    processor.process(batch_data=batch_data)

    print("\nStream filtering active: High-priority data only")
    crit_sensors = processor_sensor.filter_data(batch_data["SENSOR_001"])
    large_trans = processor_transaction.filter_data(batch_data["TRANS_001"],
                                                    criteria="150")
    print(f"Filtered results: {len(crit_sensors)} critical sensor alerts, "
          f"{len(large_trans)} large transaction")

    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
