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
                                   if item == criteria]
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


def main() -> None:
    """
    Program entry point.
    """

    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    #  === Sensor Stream ===
    print("Initializing Sensor Stream...")

    data_sensor = ["temp:22.5", "humidity:65", "pressure:1013"]
    formatted_data = ", ".join(data_sensor)

    processor = SensorStream(stream_id="SENSOR_001")
    stats = processor.get_stats()
    result = processor.process_batch(data_sensor)

    print(f"Stream ID: {stats.get('id')}, Type: {stats.get('type')}")
    print(f"Processing sensor batch: [{formatted_data}]")
    print(result)

    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
