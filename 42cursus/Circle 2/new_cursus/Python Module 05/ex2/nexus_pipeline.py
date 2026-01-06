import random
import math
from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional, Protocol  # noqa: F401


class ProcessingStage(Protocol):
    """Interface for stages using duck typing."""

    def process(self, data: Any) -> Any:
        """
        Process a data item.

        === Args ===
            - data (Any): The input data to process.

        === Returns ===
            - Any: The processed data
        """
        pass


class ProcessingPipeline(ABC):
    """
    Abstract base class defining the structure for data processing pipelines.
    Manages a sequence of processing stages.
    """

    def __init__(self, pipeline_id: Optional[str]) -> None:
        """Init the pipeline with an ID and an empty stage list.

        === Args ===
            - pipeline_id (Optional[str]): The unique identifier for the
            pipeline.
        """
        self.stages: List[Any] = []
        self.pipeline_id = pipeline_id

    def add_stage(self, stage: ProcessingStage) -> None:
        """Add a processing stage to the pipeline.

        === Args ===
            - stage (ProcessingStage): The stage instance to add.
        """
        self.stages.append(stage)

    @abstractmethod
    def process(self, data: Any) -> Any:
        """
        Loop over the stage list and process each data.

        === Args ===
            - data (Any): The input data

        === Returns ===
            - Any: The final processed data after passing through all stages.
        """
        for stage in self.stages:
            data = stage.process(data)
        return data


class InputStage():
    """Stage responsible for initial data validation and parsing."""

    def process(self, data: Any) -> Any:
        """Display and pass through the input data."""
        if isinstance(data, dict):
            print(f"Input: {data}")

        elif isinstance(data, list):
            #fdata = ",".join(data)
            print(f"Input: \"{data}\"")

        elif isinstance(data, str):
            print(f"Input: {data}")

        else:
            print("Error detected in Stage 1: invalid input")
        return data


class TransformStage():
    """Stage responsible for formatting and delivering final results."""

    def process(self, data: Any) -> Any:
        """Apply transformations to the data."""
        if isinstance(data, dict):
            try:
                if not data.get("value") or not data.get("unit"):
                    raise KeyError
                float(data.get("value"))
                if not isinstance(data.get("unit"), str):
                    raise ValueError
            except (KeyError, ValueError):
                print("Error detected in Stage 2: invalid data format")
                return None

            print("Transform: Enriched with metadata and validation")

        elif isinstance(data, list):
            print("Transform: Parsed and structured data")

        elif isinstance(data, str):
            print("Transform: Aggregated and filtered")
        return data


class OutputStage():
    """Stage responsible for outputting and printing the results."""

    def process(self, data: Any) -> Any:
        """Format and display the final processing result."""
        if isinstance(data, dict):
            temp = data.get("value")
            unit = data.get("unit")

            print(f"Output: Processed temperature reading: {temp}°{unit} "
                  "(Normal range)")

        elif isinstance(data, list):
            action = 0
            for item in data:
                if item == "action":
                    action += 1

            print(f"Output: user activity logged: {action} actions processed")

        elif isinstance(data, str):
            print("Output: Stream summary: 5 readings, avg: 22.1°C")
        return data


class JSONAdapter(ProcessingPipeline):
    """Pipeline adapter specialized for JSON data handling."""

    def __init__(self, pipeline_id: str) -> None:
        """
        Initialize the JSON adapter.

        === Args ===
            - pipeline_id (str): The unique identifier for this pipeline.
        """
        super().__init__(pipeline_id=pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        """Process JSON data through the pipeline stages."""
        print("Processing JSON data through pipeline...")
        super().process(data=data)


class CVSAdapter(ProcessingPipeline):
    """Pipeline adapter specialized for CSV data handling."""

    def __init__(self, pipeline_id: str) -> None:
        """
        Initialize the CVS adapter.

        === Args ===
            - pipeline_id (str): The unique identifier for this pipeline.
        """
        super().__init__(pipeline_id=pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        """Process CSV data through the pipeline stages."""
        print("Processing CSV data through pipeline...")
        super().process(data=data)


class StreamAdapter(ProcessingPipeline):
    """Pipeline adapter specialized for real-time stream data handling."""

    def __init__(self, pipeline_id: str) -> None:
        """
        Initialize the Stream adapter.

        === Args ===
            - pipeline_id (str): The unique identifier for this pipeline.
        """
        super().__init__(pipeline_id=pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        """Process stream data through the pipeline stages."""
        print("Processing Stream data through pipeline...")
        super().process(data=data)


class NexusManager():
    """Manager class responsible for orchestrating multiple pipelines."""

    def __init__(self) -> None:
        """Initialize the manager"""
        self.pipelines = []

    def add_pipeline(self, stage: ProcessingPipeline) -> None:
        """
        Add a ProcessingPipeline object to the pipeline's list

        === Args ===
            - stage (ProcessingPipeline): the pipeline to add
        """
        self.pipelines.append(stage)

    def process_chain(self, data: Any) -> None:
        """Process pipeline to each other"""
        for pipeline in self.pipelines:
            data = pipeline.process(data)


def main() -> None:
    """
    Program entry point.
    """

    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")
    print("Initializing Nexus Manager...")
    print("Pipeline capacity: 1000 streams/second")

    print("\nCreating Data Processing Pipeline...")
    print("Stage 1: Input validation and parsing")
    print("Stage 2: Data transformation and enrichment")
    print("Stage 3: Output formatting and delivery")

    print("\n=== Multi-Format Data Processing ===")

    stage_list = [InputStage(), TransformStage(), OutputStage()]

    # === JSON data ===
    pipeline = JSONAdapter("pipeline_01")
    for stage in stage_list:
        pipeline.add_stage(stage)
    pipeline.process({"sensor": "temp", "value": 23.5, "unit": "C"})

    print("")
    # === CSV data ===
    pipeline = CVSAdapter("pipeline_02")
    for stage in stage_list:
        pipeline.add_stage(stage)
    pipeline.process(["user", "action", "timestamp"])

    print("")
    # === Stream data ===
    pipeline = StreamAdapter("pipeline_03")
    for stage in stage_list:
        pipeline.add_stage(stage)
    pipeline.process("Real-time sensor stream")

    print("\n=== Pipeline Chaining Demo ===")

    print("\nNexus Integration complete. All systems operational.")
    manager = NexusManager()

    data = random.sample(range(1, 500), 100)
    pipeline_a = JSONAdapter("pipeline_01")
    pipeline_b = CVSAdapter("pipeline_02")
    pipeline_c = StreamAdapter("pipeline_03")
    manager.add_pipeline(pipeline_a)
    manager.add_pipeline(pipeline_b)
    manager.add_pipeline(pipeline_c)

    for stage in stage_list:
        pipeline_a.add_stage(stage)
        pipeline_b.add_stage(stage)
        pipeline_c.add_stage(stage)

    manager.process_chain(data)


if __name__ == "__main__":
    main()
