from typing import Callable
from flow import Flow
import network


class FlowExamples:
    """
    Une collection de flots pour tests
    """

    def __init__(self, Flow: Callable) -> None:
        self.Flow = Flow
        self.network_examples = network.examples

    def empty_flow(self) -> Flow:
        return Flow(self.network_examples.example1(), 0, 6, check=False)

    def example1(self) -> Flow:
        return Flow(
            self.network_examples.example1(),
            0,
            6,
            flow=self.network_examples.example2(),
            check=False,
        )

    def wrong_in_out(self) -> Flow:
        return Flow(
            self.network_examples.example1(),
            0,
            6,
            flow=self.network_examples.example3(),
            check=False,
        )

    def wrong_capacity(self) -> Flow:
        return Flow(
            self.network_examples.example1(),
            0,
            6,
            flow=self.network_examples.example4(),
            check=False,
        )

    def small_example(self) -> Flow:
        return Flow(self.network_examples.small_example(), 0, 3)

    def small_example2(self) -> Flow:
        return Flow(
            self.network_examples.small_example2(),
            0,
            3,
            flow=self.network_examples.small_example2_flow(),
        )


flow_examples = FlowExamples(Flow)
