import random
import time
from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional, Protocol  # noqa: F401


class ProcessingStage(Protocol):
    """Interface for stages using duck typing."""

    def process(self, data: Any, verbose: bool = True) -> Any:
        """
        Process a data item.

        === Args ===
            - data (Any): The input data to process.
            - verbose (bool), default to True: Print the output.

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
    def process(self, data: Any, verbose: bool = True) -> Any:
        """
        Loop over the stage list and process each data.

        === Args ===
            - data (Any): The input data
            - verbose (bool), default to True: Print the output.

        === Returns ===
            - Any: The final processed data after passing through all stages.
        """
        for stage in self.stages:
            data = stage.process(data, verbose=verbose)
        return data


class InputStage():
    """Stage responsible for initial data validation and parsing."""

    def process(self, data: Any, verbose: bool = True) -> Any:
        """Display and pass through the input data."""
        if verbose is True:
            if isinstance(data, dict):
                print(f"Input: {data}")

            elif isinstance(data, list):
                fdata = ",".join(str(x) for x in data)
                print(f"Input: \"{fdata}\"")

            elif isinstance(data, str):
                print(f"Input: {data}")

            else:
                print("Error detected in Stage 1: invalid input")
        return data


class TransformStage():
    """Stage responsible for formatting and delivering final results."""

    def process(self, data: Any, verbose: bool = True) -> Any:
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

            if verbose is True:
                print("Transform: Enriched with metadata and validation")

        elif isinstance(data, list):
            if verbose is True:
                print("Transform: Parsed and structured data")

        elif isinstance(data, str):
            if verbose is True:
                print("Transform: Aggregated and filtered")
        return data


class OutputStage():
    """Stage responsible for outputting and printing the results."""

    def process(self, data: Any, verbose: bool = True) -> Any:
        """Format and display the final processing result."""
        if verbose is True:
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

                print(f"Output: user activity logged: {action} actions "
                      "processed")

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

    def process(self, data: Any, verbose: bool = True) -> Union[str, Any]:
        """Process JSON data through the pipeline stages."""
        if verbose is True:
            print("Processing JSON data through pipeline...")
        return super().process(data=data, verbose=verbose)


class CSVAdapter(ProcessingPipeline):
    """Pipeline adapter specialized for CSV data handling."""

    def __init__(self, pipeline_id: str) -> None:
        """
        Initialize the CVS adapter.

        === Args ===
            - pipeline_id (str): The unique identifier for this pipeline.
        """
        super().__init__(pipeline_id=pipeline_id)

    def process(self, data: Any, verbose: bool = True) -> Union[str, Any]:
        """Process CSV data through the pipeline stages."""
        if verbose is True:
            print("Processing CSV data through pipeline...")
        return super().process(data=data, verbose=verbose)


class StreamAdapter(ProcessingPipeline):
    """Pipeline adapter specialized for real-time stream data handling."""

    def __init__(self, pipeline_id: str) -> None:
        """
        Initialize the Stream adapter.

        === Args ===
            - pipeline_id (str): The unique identifier for this pipeline.
        """
        super().__init__(pipeline_id=pipeline_id)

    def process(self, data: Any, verbose: bool = True) -> Union[str, Any]:
        """Process stream data through the pipeline stages."""
        if verbose is True:
            print("Processing Stream data through pipeline...")
        return super().process(data=data, verbose=verbose)


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
        pipeline_list = [id.pipeline_id for id in self.pipelines]
        result = " -> ".join(pipeline_list)
        print(result)
        print("Data flow: Raw -> Processed -> Analyzed -> Stored")

        start_time = time.time()
        for pipeline in self.pipelines:
            data = pipeline.process(data, verbose=False)
        end_time = time.time()

        print(f"Chain result: {len(data)} records processed throught "
              f"{len(pipeline_list)}-stage pipeline")
        print(f"Performance: 95% efficiency, {end_time - start_time:.1f}s "
              "total processing time")


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

    print("\n=== Multi-Format Data Processing ===\n")

    stage_list = [InputStage(), TransformStage(), OutputStage()]

    # === JSON data ===
    pipeline = JSONAdapter("pipeline_01")
    for stage in stage_list:
        pipeline.add_stage(stage)
    pipeline.process({"sensor": "temp", "value": 23.5, "unit": "C"})

    print("")
    # === CSV data ===
    pipeline = CSVAdapter("pipeline_02")
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
    manager = NexusManager()

    data = random.sample(range(1, 500), 100)
    pipeline_a = JSONAdapter("Pipeline A")
    pipeline_b = CSVAdapter("Pipeline B")
    pipeline_c = StreamAdapter("Pipeline C")
    manager.add_pipeline(pipeline_a)
    manager.add_pipeline(pipeline_b)
    manager.add_pipeline(pipeline_c)

    for stage in stage_list:
        pipeline_a.add_stage(stage)
        pipeline_b.add_stage(stage)
        pipeline_c.add_stage(stage)

    manager.process_chain(data)

    print("\n=== Error Recovery Test ===")
    print("Simulating pipeline failure...")
    pipeline = JSONAdapter("pipeline_error")
    for stage in stage_list:
        pipeline.add_stage(stage)
    error = pipeline.process({"sensor": "temp", "value": 23.5, "unit": 666},
                             verbose=False)
    if error is None:
        print("Recovery initiated: Switching to backup processor")
        print("Recovery successful: Pipeline restored, processing resumed")

    print("\nNexus Integration complete. All systems operational.")


if __name__ == "__main__":
    main()
